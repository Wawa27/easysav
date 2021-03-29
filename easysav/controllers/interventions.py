from easysav import app
from easysav.models.intervention import Intervention
from easysav.repositories import intervention_repository
from sqlalchemy.orm.exc import NoResultFound
from flask import request
import json


@app.route('/interventions', methods=["GET"])
def get_interventions():
    try:
        interventions = intervention_repository.get_all()
        return json.dumps(list(map(lambda item: str(item.to_dict()), interventions)))
    except:
        return "Internal error", 500


@app.route('/interventions/<int:intervention_id>', methods=["GET"])
def get_intervention_by_id(intervention_id):
    try:
        intervention = intervention_repository.get_by_id(intervention_id)
        return intervention.to_dict()
    except NoResultFound:
        return "Intervention not found with id: " + str(intervention_id), 400
    except:
        return "Internal error", 500


@app.route('/interventions', methods=["POST"])
def add_intervention():
    try:
        request_json = request.get_json()
        client_id = request_json["client_id"]
        piece = request_json["piece"]
        problem = request_json["problem"]

        intervention = Intervention(client_id=client_id, piece=piece, problem=problem)
        return intervention_repository.add(intervention).to_dict()
    except KeyError:
        return "Invalid body", 400
    except:
        return "Internal error", 500
