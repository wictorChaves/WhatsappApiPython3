from urllib.request import urlopen
from axolotl.kdf.hkdfv3 import HKDFv3
from axolotl.util.byteutil import ByteUtil
import binascii
from Crypto.Cipher import AES
from pprint import pprint
import base64


class Decrypter():
    __arrayDeBytes = None

    def getBase64File(self):
        return base64.b64encode(bytearray(self.__arrayDeBytes))

    def getByteArray(self):
        return bytearray(self.__arrayDeBytes)

    def salvar(self, caminho):
        with open(caminho, 'wb') as f:
            f.write(bytearray(self.__arrayDeBytes))
            f.close()

    def decrypt(self, encimg, refkey, tipo="image"):
        cryptKeys = self.getCryptKeys(tipo)
        refkey = base64.b64decode(refkey)

        derivative = HKDFv3().deriveSecrets(refkey, binascii.unhexlify(cryptKeys), 112)
        parts = ByteUtil.split(derivative, 16, 32)
        iv = parts[0]
        cipherKey = parts[1]
        e_img = encimg[:-10]
        cr_obj = AES.new(key=cipherKey, mode=AES.MODE_CBC, IV=iv)
        return cr_obj.decrypt(e_img)

    def getMediaContent(self, url, mediaKey, tipo="image"):
        data = urlopen(url).read()
        data = self.decrypt(data, mediaKey, tipo)
        self.__arrayDeBytes = data

    def getCryptKeys(self, tipo):
        if tipo == "image":
            return '576861747341707020496d616765204b657973'
        if tipo == "audio" or tipo == "ptt":
            return '576861747341707020417564696f204b657973'
        if tipo == "video":
            return '576861747341707020566964656f204b657973'
        if tipo == "document":
            return '576861747341707020446f63756d656e74204b657973'
        return None
