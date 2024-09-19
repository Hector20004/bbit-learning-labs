import pika
import pika.callback
import pika.connection
from consumer_interface import mqConsumerInterface
import os

class mqConsumer(mqConsumerInterface):
    
	def on_message_callback(
        self, channel, method_frame, header_frame, body
    ) -> None:
        # Acknowledge message

        #Print message (The message is contained in the body parameter variable)

		print(body)
		

	def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:

		self.binding_key = binding_key
		self.exchange_name = exchange_name
		self.queue_name = queue_name

		self.setupRMQConnection()
		return

	def setupRMQConnection(self) -> None:
		con_params = pika.URLParameters(os.environ["AMQP_URL"])
		self.connection = pika.BlockingConnection(parameters=con_params)
		self.channel = self.connection.channel()

		self.channel.queue_declare(queue=self.queue_name)
	
	def startConsuming(self) -> None:
		self.channel.basic_consume(queue=self.queue_name,on_message_callback=self.on_message_callback)
		
	def Del(self):
		self.channel.close()
		self.connection.close()

		

	
        
			

