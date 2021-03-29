from easysav.models.intervention import Intervention
from easysav import db


def get_by_id(intervention_id):
    return Intervention.query.filter(Intervention.id == intervention_id).one()


def get_all():
    return Intervention.query.all()


def add(intervention):
    try:
        if not intervention.client_id or not intervention.piece or not intervention.problem:
            return intervention
        db.session.add(intervention)
        db.session.commit()
    except:
        db.session.rollback()
    else:
        return intervention
