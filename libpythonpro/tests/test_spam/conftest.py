import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='module')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj  # Este é o momento que o objeto é injetado no teste
    # EM seguida é feito o Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
