import os
import tempfile
import pytest
import json

from easysav import app
from easysav.repositories import intervention_repository
from easysav.models.intervention import Intervention


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


def test_add_intervention():
    intervention = Intervention(
        client_id=client_id,
        piece=piece,
        problem=problem
    )

    intervention_repository.add(intervention)
    print(intervention)
    global inserted_id
    inserted_id = intervention.id

    assert intervention.client_id == client_id
    assert intervention.piece == piece
    assert intervention.problem == problem


def test_get_intervention():
    intervention = intervention_repository.get_by_id(inserted_id)
    assert intervention.id == inserted_id
    assert intervention.client_id == client_id
    assert intervention.piece == piece
    assert intervention.problem == problem


def test_add_incomplete_intervention():
    intervention = Intervention(
        client_id=client_id,
        piece=piece,
    )

    intervention_repository.add(intervention)

    assert intervention.id is None


def test_add_bad_intervention():
    intervention = Intervention(
        client_id=-1,
        piece=piece,
        problem=problem
    )

    intervention_repository.add(intervention)

    assert intervention.id is None


def test_get_interventions():
    interventions = intervention_repository.get_all()
    assert len(interventions) >= 1
