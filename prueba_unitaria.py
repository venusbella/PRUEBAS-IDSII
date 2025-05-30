import unittest
import json
from backend import app

class PruebaSimple(unittest.TestCase):
    def setUp(self):
        # Crear un cliente de prueba
        self.client = app.test_client()

    def test_crear_producto(self):
        # Enviar una solicitud POST a la ruta /productos
        respuesta = self.client.post('/productos', data=json.dumps({
            "nombre": "Producto de prueba",
            "precio": 9.99,
            "descripcion": "Este es un test"
        }), content_type='application/json')

        # Verificar que el código de estado sea 200 (éxito)
        self.assertEqual(respuesta.status_code, 200)

        # Verificar que el mensaje de éxito esté en la respuesta
        datos = json.loads(respuesta.data)
        self.assertIn("mensaje", datos)
        self.assertEqual(datos["mensaje"], "Producto guardado correctamente")

if __name__ == '__main__':
    unittest.main()