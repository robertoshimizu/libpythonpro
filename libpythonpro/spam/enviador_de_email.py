# como parte da metodologia Baby Steps, no inicio pode-se até fazer um
# hard code do retorno da função para fazer o teste passar.


class Enviador():
    def __init__(self):
        self.qtd_email_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in destinatario:
            raise EmailInvalido(f'Email de destinatario invalido: {destinatario}')
        self.qtd_email_enviados += 1
        return destinatario


class EmailInvalido(Exception):
    pass
