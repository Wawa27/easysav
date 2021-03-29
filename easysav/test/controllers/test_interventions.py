import os
import tempfile
import pytest
import json

from easysav import app


@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])


client_id = 1
piece = "Lave-linge"
problem = "Fuite"
inserted_id = None


def test_add_intervention(client):
    rv = client.post('/interventions', json={'client_id': client_id, 'piece': piece, 'problem': problem})
    data = json.loads(rv.data)
    global inserted_id
    inserted_id = data["id"]
    assert data["client_id"] == client_id
    assert data["piece"] == piece
    assert data["problem"] == problem


def test_get_intervention(client):
    rv = client.get('/interventions/' + str(inserted_id))
    data = json.loads(rv.data)
    assert data["client_id"] == client_id
    assert data["piece"] == piece
    assert data["problem"] == problem


def test_get_interventions(client):
    rv = client.get('/interventions')
    data = json.loads(rv.data)
    assert len(data) >= 1


def test_add_incomplete_intervention(client):
    rv = client.post("/interventions", json={'client_id': 1, 'problem': "Fuite"})

    assert rv.status == '400 BAD REQUEST'


def test_add_bad_intervention(client):
    rv = client.post("/interventions", json={'client_id': -1, 'piece': 'Lave-linge', 'problem': "Fuite"})

    assert rv.status == '500 INTERNAL SERVER ERROR'
