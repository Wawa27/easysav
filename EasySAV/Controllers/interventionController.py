from flask import Flask, jsonify, request

from EasySAV.Repository.interventionRepository import InterventionRepository
from EasySAV.Serializers.interventionSerializer import InterventionSerializer

app = Flask(__name__)


@app.route('/api/interventions/', methods=['GET'])
def get_all():
    interventions = InterventionRepository().get_interventions()

    return jsonify(InterventionSerializer().interventions_json(interventions))


@app.route('/api/intervention/<id>', methods=['GET'])
def get_intervention_by_id(id):
    interventions = InterventionRepository().get_intervention(id)

    return jsonify(InterventionSerializer().interventions_json(interventions))


@app.route('/api/add/intervention', methods=['POST'])
def add_intervention():
    intervention = InterventionSerializer.make_intervention_obj(request.json)

    return jsonify(InterventionSerializer().interventions_json(InterventionRepository().add_intervention(intervention)))