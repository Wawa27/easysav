import logging
from EasySAV.Repository.connection_bdd import start


class InterventionRepository:
    def __init__(self):
        self.database = start()

    def get_interventions(self):
        cursor = self.database.cursor()
        cursor.execute("SELECT * FROM intervention")
        response = cursor.fetchall()
        print(response)
        return response

    def get_intervention(self, id):
        cursor = self.database.cursor()
        cursor.execute(f"SELECT * FROM intervention WHERE id={id}")
        response = cursor.fetchall()

        return response

    def add_intervention(self, intervention):
        cursor = self.database.cursor()
        cursor.execute(
            f"INSERT INTO intervention (id, client_id, piece, problem) VALUES ('{intervention.code}', '{intervention.ref_client}', '{intervention.piece}', '{intervention.probleme}')")
        try:
            self.database.commit()
            logging.info('Modification successfully made')

        except:
            logging.error('Modification has failed')
