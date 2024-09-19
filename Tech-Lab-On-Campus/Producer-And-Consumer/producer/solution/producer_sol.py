from producer_interface import mqProducerInterface 

import pika
import os

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str):
        self.routing_key = routing_key
        self.exchange_name = exchange_name

        self.setupRMQConnection()
        

    def setupRMQConnection(self):
        con_params = pika.URLParameters(os.environ["AMQP_URL"])
        self.connection = pika.BlockingConnection(parameters=con_params)

        # channel.queue_declare(queue="Queue Name")
        # channel.queue_bind(
        #     queue= "Queue Name",
        #     routing_key= "Routing Key",
        #     exchange="Exchange Name",
        # )

        # channel.basic_consume(
        #     "Queue Name", Function Name, auto_ack=False
        # )

    def publishOrder(self, message: str):
        self.channel = self.connection.channel()

        exchange = self.channel.exchange_declare(exchange=self.exchange_name)
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message,
        )
        
        self.channel.close()
        self.connection.close()