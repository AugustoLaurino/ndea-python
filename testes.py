from validador_cep import validar_cep


def teste_validar_cep():
    assert validar_cep('012345') == False
    assert validar_cep('9999999') == False
    assert validar_cep('121426') == False
    assert validar_cep('352523') == False
    assert validar_cep('523563') == True
    assert validar_cep('123456') == True
    assert validar_cep('997531') == True

    print('Todos os testes passaram com sucesso!')


if __name__ == '__main__':
    teste_validar_cep()
