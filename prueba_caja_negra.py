
import pytest
from backend import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_post_producto(client):
    response = client.post('/productos', json={
        'nombre': 'CajaNegraMock',
        'precio': 10.0,
        'descripcion': 'TipoSimulado'
    })

    assert response.status_code == 200
    assert b"guardado" in response.data
