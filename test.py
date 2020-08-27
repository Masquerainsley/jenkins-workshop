from api import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b"Hello World, it's wonderful to see you!"
