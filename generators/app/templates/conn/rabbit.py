""" AMQP Client / RabbitClient
"""
import random
import time
from logzero import logger
import pika
from pydantic import BaseModel
from helpers import Singleton
from utils import AppConfig


class RabbitClient(metaclass=Singleton):
    def __init__(self, config: AppConfig):
        self.cfg = config
        self.event_route = self.cfg.RB_EVENT_ROUTE
        self.prepare_argument()

    def prepare_argument(self):
        all_endpoints = []

        for endpoint in self.cfg.RB_URLS.split(','):
            all_endpoints.append(pika.URLParameters(endpoint))

        self.parameters = all_endpoints

    def consume(self, thread_handler):
        """ Consumer
        """
        while True:
            try:
                threads = []
                logger.info("Connecting...")
                random.shuffle(self.parameters)
                connection = pika.BlockingConnection(self.parameters)
                channel = connection.channel()
                channel.basic_qos(prefetch_count=3)
                channel.queue_declare(queue=self.cfg.RB_QUEUE_NAME,
                                      durable=True,
                                      exclusive=False,
                                      auto_delete=False)
                channel.queue_bind(self.cfg.RB_QUEUE_NAME,
                                   self.cfg.RB_EXCHANGE_NAME,
                                   routing_key=self.cfg.RB_ROUTING_KEY)
                callback = thread_handler(threads)
                channel.basic_consume(self.cfg.RB_QUEUE_NAME, callback)

                try:
                    channel.start_consuming()
                except KeyboardInterrupt:
                    channel.stop_consuming()
                    for t in threads:
                        t.join()

                    connection.close()
                    break
            except pika.exceptions.ConnectionClosedByBroker:
                sleep = random.randint(1, 5)
                logger.info("Connection was closed by broker, retrying... in %ss", sleep)
                time.sleep(sleep)
                continue
            # Do not recover on channel errors
            except pika.exceptions.AMQPChannelError as err:
                logger.error("Caught a channel error: {}, stopping...".format(err))
                break
            # Recover on all other connection errors
            except pika.exceptions.AMQPConnectionError:
                sleep = random.randint(1, 5)
                logger.info("Connection was closed, retrying... %ss", sleep)
                time.sleep(sleep)
                continue
