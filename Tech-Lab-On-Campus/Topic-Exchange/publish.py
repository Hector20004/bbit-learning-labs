# Copyright 2024 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import sys
import pika
import os

from solution.producer_sol import mqProducer  # pylint: disable=import-error


def main(ticker: str, price: float, sector: str) -> None:
    
    con_params = pika.URLParameters(os.environ["AMQP_URL"])
    connection = pika.BlockingConnection(parameters=con_params)
    channel = connection.channel()

    # Declare the topic exchange
    channel.exchange_declare(exchange="Tech Lab Topic Exchange", exchange_type='topic')

    # Set the routing key and publish a message with that topic exchange:
    routingKey = f"#.{sector}.#"
    


    producer = mqProducer(routing_key=routingKey,exchange_name="Tech Lab Topic Exchange")


    # Implement Logic To Create a message variable from the variable EG. "TSLA price is now $500" - Step 3
    #
    #                       WRITE CODE HERE!!!
    #

    message = ticker + " is " + price + " " + sector 
    channel.basic_publish(
    exchange="Tech Lab Topic Exchang", routing_key=routingKey, body=message)
    
    print(f" [x] Sent {routingKey}:{message}")
    
    
    producer.publishOrder(message)

if __name__ == "__main__":

    ticker = sys.argv[1]
    price = sys.argv[2]
    sector = sys.argv[3]

    sys.exit(main(ticker,price,sector))
