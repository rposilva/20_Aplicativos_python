import unittest
from unittest.mock import patch
from io import StringIO
import datetime
from organiza_fila01.organiza_fila01 import cadastro, atender, tempo_medio, mostrar_painel

class TestOrganizaFila(unittest.TestCase):

    @patch('builtins.input', side_effect=["João"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_cadastro(self, mock_stdout, mock_input):
        cadastro("João")
        output = mock_stdout.getvalue()
        self.assertIn("João, você recebeu a senha N° 1", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_atender_fila_vazia(self, mock_stdout):
        atender()
        output = mock_stdout.getvalue()
        self.assertIn("Fila vazia.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_atender_com_pessoa(self, mock_stdout):
        cadastro("Maria")
        atender()
        output = mock_stdout.getvalue()
        self.assertIn("🔔 ATENDENDO: Maria (Senha Nº 1)", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tempo_medio_sem_atendimentos(self, mock_stdout):
        tempo_medio()
        output = mock_stdout.getvalue()
        self.assertIn("Nenhum atendimento ainda.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_tempo_medio_com_atendimentos(self, mock_stdout):
        cadastro("Carlos")
        atender()
        tempo_medio()
        output = mock_stdout.getvalue()
        self.assertIn("⏱ Tempo médio de espera:", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_painel_sem_atendimentos(self, mock_stdout):
        mostrar_painel()
        output = mock_stdout.getvalue()
        self.assertIn("Nenhum atendimento realizado.", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_painel_com_atendimentos(self, mock_stdout):
        cadastro("Ana")
        atender()
        mostrar_painel()
        output = mock_stdout.getvalue()
        self.assertIn("📺 Última senha atendida: N° 1", output)

if __name__ == '__main__':
    unittest.main()