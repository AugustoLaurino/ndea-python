import requests

def obter_endereco(cep):
    url = 'https://viacep.com.br/ws/{cep}/json/'.format(cep=cep)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'erro' in data:
            return None
        else:
            return data
    else:
        return None

def main():
    cep = input('Digite o CEP a ser consultado: ').strip()
    endereco = obter_endereco(cep)
    if endereco:
        print(f'O CEP {cep} é válido\n')
        print('Detalhes do Endereço:')
        print('CEP:', endereco['cep'])
        print('Logradouro:', endereco['logradouro'])
        print('Complemento:', endereco['complemento'])
        print('Bairro:', endereco['bairro'])
        print('Localidade:', endereco['localidade'])
        print('UF:', endereco['uf'])
        print('IBGE:', endereco['ibge'])
        print('DDD:', endereco['ddd'])
        print('SIAFI:', endereco['siafi'])
    else:
        print('CEP inválido.')

if __name__ == '__main__':
    main()
