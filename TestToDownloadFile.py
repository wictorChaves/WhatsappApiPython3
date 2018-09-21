from ManageMessage import ManageMessage
from Decrypter import Decrypter
from pprint import pprint
import urllib2
import sys

ManageMessage = ManageMessage()
Decrypter = Decrypter()
for message in ManageMessage.getMessages():
    if 'clientUrl' in message and 'mediaKey' in message and 'type' in message:
        try:
            Decrypter.getMediaContent(message['clientUrl'], message['mediaKey'], message['type'])
            pprint(Decrypter.getBase64File())
            pprint(message['clientUrl'])
        except urllib2.HTTPError, e:
            print e.code
            print e.msg
            pprint(message)
            sys.exit(1)
