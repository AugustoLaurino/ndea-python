import requests
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

db_password = os.getenv("DATABASE_PASSWORD")

client = MongoClient('mongodb+srv://admin:' + db_password + '@cluster0.w9iiuwu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ceps_validados'] 
collection = db['cep']  

def obter_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
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
    cep = input('Digite o CEP a ser consultado: ')

    if '-' not in cep:
        cep_com_hifen = f"{cep[:5]}-{cep[5:]}"
    else:
        cep_com_hifen = cep

    endereco = obter_endereco(cep_com_hifen)

    if endereco:
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

        if collection.find_one({'cep': cep_com_hifen}) is None:
            collection.insert_one(endereco)
            print('CEP gravado com sucesso!')
        else:
            print('Este CEP já está registrado na coleção.')
    else:
        print('CEP INVÁLIDO.')

if __name__ == '__main__':
    main()
