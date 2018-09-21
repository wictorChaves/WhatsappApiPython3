from ManageMessage import ManageMessage
from Decrypter import Decrypter
import sys

ManageMessage = ManageMessage()
Decrypter = Decrypter()
for message in ManageMessage.getMessages():
    if 'clientUrl' in message:
        if message['type']:
            Decrypter.getMediaContent(message['clientUrl'], message['mediaKey'], message['type'])
            Decrypter.salvar('teste.jpg')
            sys.exit(1)