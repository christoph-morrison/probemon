CREATE TABLE `probe_requests` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `macaddress` varchar(255) DEFAULT NULL,
  `make` varchar(255) DEFAULT NULL,
  `rssi` varchar(255) DEFAULT NULL,
  `ssid` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL,
  `uppercaseSSID` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4;