#!/bin/sh

#echo "Waiting for RabbitMQ..."

while ! nc -z 127.0.0.1 $RABBIT_PORT; do
#while ! nc -z $RABBIT_HOST $RABBIT_PORT; do
  sleep 0.1
done

echo "RabbitMQ started"

rabbitmqadmin import rabbit-backup.config
exec "$@"
