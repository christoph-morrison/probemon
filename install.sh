#!/usr/bin/env bash

ln -s probemon.service /etc/systemd/system/probemon.service
systemctl daemon-reload