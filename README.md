# Earnings Simulator

Sistema que estima o valor necessário a ser acumulado com corridas como motorista de aplicativo para atingir um valor desejado, descontando os gastos com combustível.

O usuário precisa informar o valor que deseja receber, a quantidade de horas que pretende trabalhar e o consumo do veículo em km/l (gasolina) e/ou km/l (álcool).

O sistema simula a distância percorrida, calcula o consumo de combustível por quilômetro, o custo total e retorna o valor necessário a acumular.

## Tecnologias
- Flask
- pytest

## Executando a Aplicação
1. Clone o repositório:
````bash
git clone https://github.com/devnatanaelsantos/earnings-simulator.git
````
2. Instale as dependências:
````bash
pip install -r requirements.txt
````

3. Inicie a aplicação:
````bash
python run.py 
````

## Testes Unitários
Desenvolvi testes unitários para validar diferentes cenários com combinações variadas de parâmetros para o método `simulate`.

Para executar os testes:

````bash
pytest -v
````

## Endpoints
### Simular valor necessário

**Método:** POST

**URL:** http://127.0.0.1:5000/simualtor

**Corpo da requisição (JSON):**
````json
{
    "val_almejado": 2000, 
    "hr_trabalhadas": 36,
    "km/l_g": 11.5,
    "km/l_a": 7.9
}
````
**Resposta (JSON):**
````json
{
    "custo_alc": 349.1,
    "custo_gas": 378.66,
    "val_necessario_alc": 2349.1,
    "val_necessario_gas": 2378.66
}
````
