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


def test_home(client):
    rv = client.get('/')
    assert rv.data == b'Hello world !'
