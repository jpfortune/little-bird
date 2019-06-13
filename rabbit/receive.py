#!/usr/bin/env python
import pika

cred = pika.PlainCredentials("test", "test")
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        # host="127.0.0.1", port=5672, virtual_host="/", credentials=cred
        host="127.0.0.1",
        # port=5672,
        credentials=cred,
    )
)
channel = connection.channel()

channel.queue_declare(queue="hello")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)

print(" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()
