#!/bin/sh
echo kemsu_flask | sudo -S nginx
. ./venv/bin/activate
flask run