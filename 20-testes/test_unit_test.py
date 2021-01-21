"""
Para executar:

python test_unit_test.py

Para executar com verbosidade

python test_unit_test.py -v

"""

import unittest

from atividade_unit_tests import (
    comer,
    dormir
)


class AtividadesUnitTests(unittest.TestCase):

    # Executado sempre antes de cada teste
    def setUp(self):
        # Configurações do setup
        print('Executei o setup')
        self.comida = 'quiabo'  # Esta variável fica disponível para todos os testes

    # Por convenção, todos os testes devem iniciar com test_
    def test_comer_saudavel(self):
        self.assertEqual(
            comer(self.comida, True),
            f'Estou comendo {self.comida} porque é saudável'
        )

        # Mesmo que tenha dois testes dentro do mesmo método, o python só irá contabilizar 1 no report final
        self.assertEqual(
            comer(self.comida, True),
            f'Estou comendo {self.comida} porque é saudável'
        )

    def test_comer_nao_saudavel(self):
        self.assertEqual(
            comer(self.comida, False),
            'Comida não saudável'
        )

    def test_dormir(self):
        self.assertEqual(
            dormir(),
            'Estou dormindo'
        )

    def tearDown(self) -> None:
        print('tearDown() sendo executado')


if __name__ == '__main__':
    unittest.main()

