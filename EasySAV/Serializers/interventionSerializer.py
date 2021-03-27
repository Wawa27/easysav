from EasySAV.Domain.Intervention import Intervention


class InterventionSerializer:
    def interventions_json(self, innterventions):
        interventions_json = []
        for intervention in innterventions:
            interventions_json.append(self.interventions_json(intervention))

        return interventions_json

    @staticmethod
    def make_intervention_obj(json):
        intervention = Intervention(
            json['id'],
            json['client_id'],
            json['piece'],
            json['problem']
        )
        return intervention