from easysav import app
from easysav.models.intervention import Intervention
from easysav.utils.list_serializer import serialize_list


@app.route('/interventions', methods=["GET"])
def get_interventions():
    return serialize_list(Intervention.query.all())
