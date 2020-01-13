#! /usr/bin/python3
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import mysql.connector as db_connector
import ssl
import argparse

def on_connect(client, userdata, flags, rc):
  mqtt_client.subscribe(args.mqtt_topic, 0)

def on_message(client, userdata, message):
    pass

def on_subscribe(mosq, obj, mid, granted_qos):
    pass

def main():
    global topic

    parser = argparse.ArgumentParser(description=DESCRIPTION)

    # MQTT arguments
    parser.add_argument('--mqtt-broker',    default='localhost', help="MQTT broker host, default localhost")
    parser.add_argument('--mqtt-port',      default='1883', help="MQTT broker port, default 1883")
    parser.add_argument('--mqtt-user',      default='', help="MQTT broker user")
    parser.add_argument('--mqtt-password',  default='', help="MQTT broker password")
    parser.add_argument('--mqtt-topic',     default='probemon/request', help="mqtt topic to subscribe to")
    parser.add_argument('--mqtt-ka',        default="60", help="MQTT connection keep-alive between two messages")

    parser.add_argument('--db-port',        default='3306', help="Database server port, default 3306")
    parser.add_argument('--db-user',        default='', help="Database server user")
    parser.add_argument('--db-password',    default='', help="Database server password")
    parser.add_argument('--db-host',        default='localhost', help="Database server host, default localhost")
    parser.add_argument('--db',             default='probemon', help="Database, default probemon")

    parser.add_argument('--pid',            default='', help="PID File")
    args = parser.parse_args()

    # check prerequisits: db host and mqtt broker
    if not args.db_host:
        print("Database server host not set, aborting.")
        sys.exit()

    if not args.mqtt_broker:
        print("MQTT broker not specified, aborting.")
        sys.exit()

    # save pid
    if args.pid:
        if os.path.isfile(args.pid):
            print("%s already exists, exiting" % args.pid)
            sys.exit()

        pid = str(os.getpid())
        open(args.pid, 'w').write(pid)

    # connect to database
    try :
        db = db_connector.connect(
            host = args.db_host,
            user = args.db_user,
            password = args.db_password,
            database = args.db
        )
    except db_connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        sys.exit()

    cursor = db.cursor()

    # connect to mqtt
    try :
        mqtt_client = mqtt.Client()

        if args.mqtt_user and args.mqtt_password:
            mqtt_client.username_pw_set(args.mqtt_user, args.mqtt_password)

        if args.mqtt_broker:
            mqtt_client.connect(args.mqtt_broker, int(args.mqtt_port), int(args.mqtt_ka))

    except mqtt_client.Error as err:
        print('Error: %s [%s]', err, err.errno)
        sys.exit()

    db.close()


"""

def on_message(mosq, obj, msg):
  # Prepare Data, separate columns and values
  msg_clear = msg.payload.translate(None, '{}""').split(", ")
  msg_dict =    {}
  for i in range(0, len(msg_clear)):
    msg_dict[msg_clear[i].split(": ")[0]] = msg_clear[i].split(": ")[1]

  # Prepare dynamic sql-statement
  placeholders = ', '.join(['%s'] * len(msg_dict))
  columns = ', '.join(msg_dict.keys())
  sql = "INSERT INTO pws ( %s ) VALUES ( %s )" % (columns, placeholders)

  # Save Data into DB Table
  try:
      cursor.execute(sql, msg_dict.values())
  except mariadb.Error as error:
      print("Error: {}".format(error))
  mariadb_connection.commit()
"""