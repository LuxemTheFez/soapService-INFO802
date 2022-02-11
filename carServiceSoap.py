from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode, AnyDict
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
from spyne.protocol.json import JsonDocument
import json
import os

port = int(os.environ.get('PORT', 33507))


carStat = [
        {
            'model': 'Dacia spring Electric',
            'range' : 170,
            'fastChargeTime' : 40,
            'chargeTime' :  300
        },
        {
            'model': 'Renault Twingo Electric',
            'range' : 130,
            'fastChargeTime' : 0,
            'chargeTime' :  75
        },
        {
            'model': 'Fiat 500e Hatchback',
            'range' : 135,
            'fastChargeTime' : 24,
            'chargeTime' :  150
        },
        {
            'model': 'Tesla Model 3 Performance',
            'range' : 470,
            'fastChargeTime' : 25,
            'chargeTime' :  495
        }
        ]
class carService(ServiceBase):
    @rpc(_returns=Unicode)
    def get_car(ctx):
        return json.dumps(carStat)   

    
application = Application([carService], 'spyne.examples.hello.soap',
                            in_protocol=Soap11(validator='lxml'),
                            out_protocol=Soap11())
wsgi_application = WsgiApplication(application)


def main():
    server = make_server('0.0.0.0', port, wsgi_application)
    print(f"Listening on port {port}...")
    server.serve_forever()

if __name__ == '__main__':
    main()