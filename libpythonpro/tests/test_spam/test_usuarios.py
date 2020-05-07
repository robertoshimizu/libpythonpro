from libdjango.spam.modelos import Usuario

# A fixture é transformada em um generator, que só roda quando a função for executada.
# vc pode setar que o fixture rode por função, por modulo ou por sessaao. Neste caso como a fixture é chamada duas vezes
# para criar a mesma conexao no db, otimiza-se o escopp por modulo e assim só chama 1 vez


# Pytest introspectao argumento conexao do teste abaixo, em seguida busca se há uma fixture de nome conexão
# Se houver (como de fato há acima), o PyTest executa a fixture, produz o objeto Conexao() e injeta no teste
# O TearDown eliminou bastante o codigo, em caso de duvidas acompanhar no
# https://www.python.pro.br/modulos/pytools/topicos/setup-e-tear-down-com-fixture

# Note que as fixtures estao "nested", o teste invoca a fixture sessao, que por sua vez invoca a fixture
# conexao.


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Renzo', email='renzo@python.pro.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Renzo', email='renzo@python.pro.br'),
                Usuario(nome='Luciano', email='renzo@python.pro.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
