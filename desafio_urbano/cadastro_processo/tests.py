from django.test import TestCase
from desafio_urbano.cadastro_processo.forms import PlanilhaForm

# Create your tests here.

class CadastrarProcessoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """Get / must return status code 200"""

        self.assertEqual(200, self.resp.status_code)


class CadastrarProcessoPostTest(TestCase):
    def setUp(self):
        data = dict(nome='Matheus', clinte='Farias',
                    arquivo='uploads/processos.csv')
        self.resp = self.client.post('/', data)
    
    def test_post(self):
        self.assertEqual(200, self.resp.status_code)
