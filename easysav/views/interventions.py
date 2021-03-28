from easysav import app
from easysav import db
from easysav.models.intervention import Intervention
from easysav.utils.list_serializer import serialize_list
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import OperationalError
from flask import request


@app.route('/interventions', methods=["GET"])
def get_interventions():
    return serialize_list(Intervention.query.all())


@app.route('/interventions/<int:intervention_id>', methods=["GET"])
def get_intervention_by_id(intervention_id):
    try:
        intervention = Intervention.query.filter(Intervention.id == intervention_id).one()
    except NoResultFound:
        return "Intervention not found with id: " + str(intervention_id)
    return intervention.to_dict()


@app.route('/interventions', methods=["POST"])
def add_intervention():
    request_json = request.get_json()
    print(request_json)
    try:
        intervention = Intervention(
            client_id=request_json["client_id"],
            piece=request_json["piece"],
            problem=request_json["problem"]
        )
        db.session.add(intervention)
        db.session.commit()
        return intervention.to_dict()
    except AttributeError:
        return "Invalid body"
    except OperationalError:
        return "Invalid body"
