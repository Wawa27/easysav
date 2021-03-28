import json
import unittest

from EasySAV.Controllers.interventionController import app
from EasySAV.Serializers.interventionSerializer import InterventionSerializer


class InterventionControllerTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.app = app.test_client()
        self.assertEqual(app.debug, True)

    def test_get_interventions(self):
        response = self.app.get('/api/interventions/', follow_redirects=False)
        interventions = json.loads(response.data)
        self.assertEqual(len(interventions), 1)


if __name__ == '__main__':
    unittest.main()
