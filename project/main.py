import requests

from acesso_cep import BuscaEndereco

cep = 25870145
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

r = requests.get("https://viacep.com.br/ws/01001000/json/")
print(r)
