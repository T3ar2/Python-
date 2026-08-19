# preparar o ambiente o Python
1. Abrir o VS Code
2. No terminal do VSCode
- Criar o ambiente do python isolado dentro do projeto
Alternativa a:

''' python -m venv .venv '''

Alternativa b:

''' python -m venv .venv '''

Alternativa c:
python -m venv --upgrade-deps venv

- Ativar o ambiente isolado do pyth

''' .venv\Scripts\Activate '''

## Após instalar as dependências do projeto

''' pip freeze > requirements.txt '''

## A cada aula, baixe o requirements.txt e instale as dependências

''' pip install -r requirements.txt '''
