from sqlite.Sqlite import Sqlite
from Decrypter import Decrypter
from urllib.request import urlopen
import json
from pprint import pprint
import sys

from urllib.error import URLError, HTTPError

class ManageMessage:

    _file_db = 'db/1'
    _Sqlite = None
    _messages = []
    _Decrypter = None

    def __init__(self):
        self._Sqlite = Sqlite(self._file_db)
        self._Decrypter = Decrypter()

    def getMessages(self):
        query = "SELECT * FROM messages;"
        cursor = self._Sqlite.getInfo(query)
        for line in cursor.fetchall():
            jsonObj = json.loads(line[1])
            self._messages.append(self.parseMediaToBase64(jsonObj))
        return self._messages

    def parseMediaToBase64(self, message):
        if 'clientUrl' in message and 'mediaKey' in message and 'type' in message:
            try:
                self._Decrypter.getMediaContent(message['clientUrl'], message['mediaKey'], message['type'])
                if(message['type'] == "sticker"):
                    self._Decrypter.salvar('C:\\Users\\wictor\\Documents\\Wictor\\Workspace\\Github\\WhatsappApiPython3\\midias\\' + message['id'] +'.jpg')
                if (message['type'] == "image"):
                    self._Decrypter.salvar('C:\\Users\\wictor\\Documents\\Wictor\\Workspace\\Github\\WhatsappApiPython3\\midias\\' + message['id'] + '.jpg')
                message['filebase64'] = self._Decrypter.getBase64File()
                return message
            except HTTPError as e:
                #print e.code
                #print e.msg
                return message
        return message

ManageMessage = ManageMessage()
pprint(ManageMessage.getMessages())
