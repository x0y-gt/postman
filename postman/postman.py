from postman.transport import Transport
from postman.message import Message

__ALL__ = ['Postman']


class Postman:

    def __init__(self, transport: Transport):
        self.transport = transport

    def send(self, msg: Message):
        return self.transport.send(msg)
