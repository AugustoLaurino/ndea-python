import re


def validar_cep(cep):
    if not (100000 < int(cep) < 999999):
        return False

    if re.search(r'(\d)(?=\d\1)', cep):
        return False

    return True


def main():
    cep = input('Digite o CEP a ser validado: ')
    if validar_cep(cep):
        print('CEP válido!')
    else:
        print('CEP inválido!')


if __name__ == '__main__':
    main()
