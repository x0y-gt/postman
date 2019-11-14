# postman
Library to send email in python

# Example

```
mail = Message()
mail.to('')\
    .subject('bla bla')\
    .template('resources/templates/billing.html', {
        'order_id': 'asd',
        'name': 'NAME',
        'date': '2 de Marzo, 2019',
        'items': [{
            'name': 'Cafe Pacamara 1lb',
            'price': 50.00
        }],
        'total': 50
    })

postman = Postman(SmtpTransport(user={'':''}, password='', host="smtp.mailgun.org"))
postman.send(mail)

print('Emial sent')
```
