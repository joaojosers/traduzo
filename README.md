# traduzo

## Contexto
- Implementar uma API utilizando arquitetura em camadas MVC.
- Utilizar o Docker para projetos Python e Orientação a Objetos no desenvolvimento WEB.
- Escrever testes para APIs para garantir a implementação dos endpoints.
- Interagir com um banco de dados não relacional MongoDB.
- Desenvolver páginas web Server Side.


## Tecnologias usadas

### Back-end:
- Desenvolvido usando: Python
## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Executando aplicação
* Database e Flask pelo Docker:
```
docker compose up translate
```
* Database pelo Docker e Flask localmente pelo ambiente virtual
```
docker compose up -d mongodb

python3 src/app.py
```

## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
## Arquivos desenvolvidos pela Trybe
* src:
  - dev-requirements.txt
  - requirements.txt