from EasySAV.Domain.Intervention import Intervention


class InterventionSerializer:
    def interventions_json(self, interventions):
        interventions_json = []
        for intervention in interventions:
            interventions_json.append(self.make_json(intervention))

        return interventions_json

    @staticmethod
    def make_json(intervention):
        return {
            'id': intervention[0],
            'client_id': intervention[1],
            'piece': intervention[2],
            'probleme': intervention[3]
        }

    @staticmethod
    def make_intervention_obj(json):

        intervention = Intervention(
            json[0]['id'],
            json[0]['client_id'],
            json[0]['piece'],
            json[0]['probleme']
        )
        return intervention
