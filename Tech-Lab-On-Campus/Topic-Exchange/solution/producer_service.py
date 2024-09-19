import sys
import pika

def read():
    ticker = sys.argv[0]
    price = sys.argv[1]
    sector = sys.argv[2]

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare the topic exchange
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    # Set the routing key and publish a message with that topic exchange:
    routing_key = "google"
    message = ticker + " is " + price + " " + sector 
    channel.basic_publish(
        exchange='topic_logs', routing_key=routing_key, body=message)
    
    print(f" [x] Sent {routing_key}:{message}")