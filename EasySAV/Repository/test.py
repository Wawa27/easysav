import json
from EasySAV.Domain.Intervention import Intervention
from EasySAV.Repository.interventionRepository import InterventionRepository
from EasySAV.Serializers.interventionSerializer import InterventionSerializer
from EasySAV.controllers.interventionController import app

#test = InterventionRepository()
#test.get_interventions()

#intervention3 = Intervention(3, 2, "joint", "fuite")
#test.add_intervention(intervention3)

#test.get_interventions()
app.config["TESTING"] = True
app.config["DEBUG"] = True
app = app.test_client()
response = app.get('/api/interventions/', follow_redirects=False)
interventions = InterventionSerializer().make_intervention_obj(json.loads(response.data))
print(interventions)