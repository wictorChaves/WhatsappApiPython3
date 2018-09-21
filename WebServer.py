import web
import json
from ManageMessage import ManageMessage

ManageMessage = ManageMessage()

urls = (
    '/', 'index',
    '/get/messages', 'messages',
    '/teste', 'test',
    '/del/(\d+)', 'Delete'
)

class messages:
    def GET(self):
        return json.dumps(ManageMessage.getMessages())

class test:
    def GET(self):
        return "Teste ok"

class index:
    def GET(self):
        return "Pagina home"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()