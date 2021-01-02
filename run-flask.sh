#!/bin/bash
### BEGIN INIT INFO
#Provides: run-flask
#Required-Start: $all
#Default-Start: 2 3 4 5
#Short-Description: run flask...
### END INIT INFO
# Carry out specific functions when asked to by the system
case "$1" in 
 start)
echo "App is running..."
export FLASK_APP=/root/web/WebInterface.py
export FLASK_RUN_HOST='0.0.0.0'
flask run
;;
 *)
echo "How to run this App: ./run-flask.sh start"
exit 1
;;
esac
exit 0

