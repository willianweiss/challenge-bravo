# Challenge-Bravo

## Como rodar a aplicação

Para executar a aplicação, primeiro renomeie o arquivo `.env.example` para `.env`. Em seguida, execute o seguinte comando:

bashCopy code

`docker-compose up --build` 

A aplicação também pode ser executada utilizando os seguintes comandos e auxiliares:

Comando

Descrição

`make build`

Builda a aplicação e aplica migrations alembic

`make down`

Derruba a aplicação (api, banco de dados e coinbase_feeder)

`make up`

Inicia a aplicação (api, banco de dados e coinbase_feeder)

`make test-cov`

Executa testes unitários com cobertura de código

`make lint`

Aplica linters black e isort para formatação do código

`make stress_tests`

Executa testes de carga com locust

## Endpoints

A documentação extensa de todo tipo de input e output pode ser encontrada em [http://localhost:8000/docs](http://localhost:8000/docs) conforme indicação de como executar a aplicação.

Endpoint

Método

Retorno

`/currency`

GET

Retorna todas as moedas cadastradas

`/currency/{currency_code}`

GET

Retorna a cotação de uma moeda específica

`/currency`

POST

Cria uma moeda fictícia

`/currency/{currency_code}`

PUT

Atualiza a cotação de uma moeda específica

`/currency/{currency_code}`

DELETE

Deleta uma moeda específica

`/convert`

GET

Converte o valor de uma moeda para outra


## Testes

Foram criados testes unitários cobrindo todos endpoints da aplicação, convert/currency.

Para executá-los, utilize o seguinte comando:

bashCopy code

`make test-cov` 

O resultado do teste de cobertura será apresentado no terminal, assim como um relatório em formato xml, que pode ser encontrado no diretório `app`.
