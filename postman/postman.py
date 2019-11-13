from postman.transport import Transport
from postman.message import Message

__ALL__ = ['Postman']


class Postman():

    def __init__(self, transport: Transport):
        self.transport = transport

    def send(self, msg: Message):
        return self.transport.send(msg)


#mail = Message()
#mail.to('EMAIL')\
#    .subject('bla bla')\
#    .template('resources/templates/billing.html', {
#        'order_id': 'asd',
#        'name': 'NAME',
#        'date': '2 de Marzo, 2019',
#        'items': [{
#            'name': 'Cafe Pacamara 1lb',
#            'price': 50.00
#        }],
#        'total': 50
#    })
#
#postman = Postman(SmtpTransport(user={'EMAIL':'NAME'}, password='PASS', host="smtp.mailgun.org"))
#postman.send(mail)
#
#print('Emial sent')
