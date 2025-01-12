from flask import Flask, request, Response
from flask_cors import CORS  # Importa CORS
from lxml import etree

app = Flask(__name__)
CORS(app)  # Habilita CORS para todo el servidor

@app.route('/soap', methods=['POST'])
def soap_service():
    try:
        # Leer el cuerpo de la solicitud SOAP
        body = request.data
        # Analizar el cuerpo de la solicitud con lxml
        root = etree.fromstring(body)

        # Extraer el mensaje enviado en la solicitud
        message = root.xpath('//soapenv:Body//web:say_hello/text()', namespaces={
            'soapenv': 'http://schemas.xmlsoap.org/soap/envelope/',
            'web': 'http://example.com/soap'
        })

        # Si el mensaje fue recibido, devolver un "Hola Mundo"
        if message:
            response_text = f"Hola Mundo {message[0]}"
        else:
            response_text = "Hola Mundo"

        # Construir la respuesta SOAP
        response_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
        <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://example.com/soap">
            <soapenv:Header/>
            <soapenv:Body>
                <web:say_helloResponse>
                    <web:message>{response_text}</web:message>
                </web:say_helloResponse>
            </soapenv:Body>
        </soapenv:Envelope>'''

        return Response(response_xml, content_type="text/xml")

    except Exception as e:
        return Response(f"Error: {str(e)}", content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
