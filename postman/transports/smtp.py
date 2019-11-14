import yagmail
from postman.transport import Transport
from postman.message import Message

__ALL__ = ['SmtpTransport']

class SmtpTransport(Transport):

    def __init__(self, user=None, password=None, host=None, port=587):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connect()

    def connect(self):
        self.smtp = yagmail.SMTP(
            user=self.user,
            password=self.password,
            host=self.host
        )

    def send(self, msg: Message):
        self.smtp.send(
            to=",".join(msg._to),
            subject=msg._subject,
            contents = [msg.render()]
        )

