import pytest

from libdjango.spam.enviador_de_email import Enviador, EmailInvalido


# criação de um programa de envio de mensagens de spam, a partir de endereços de um banco de dados.

# primeiro passo TDD é criar o objeto enviador da classe Enviador
def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

# gostaria de testar os dados de envio, em especial o destinatario
@pytest.mark.parametrize('destinatario', ['luciano@python.pro.br', 'john@doe.com'])
def teste_destinatario(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        'renzo@python.pro.br',
        destinatario,
        'Cursos Python Pro',
        'Primeira turma Guido Von Rossum aberta'
    )
    assert destinatario in resultado

# gostaria de testar a validade dos e-mails (exemplos quebrados, sem @ por exemplo)


@pytest.mark.parametrize('destinatario', ['lupro.br', 'john'])
def teste_destinatario_invalido(destinatario):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            'renzo@python.pro.br',
            destinatario,
            'Cursos Python Pro',
            'Primeira turma Guido Von Rossum aberta'
        )
