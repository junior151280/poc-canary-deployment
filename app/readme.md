# Projeto Flask com Prometheus Metrics

Este repositório contém um exemplo de aplicação Flask que é instrumentada para expor métricas para o Prometheus, utilizando a biblioteca `prometheus_client` para gerar métricas customizadas. A aplicação inclui uma rota de exemplo que pode simular falhas para demonstrar a coleta de métricas de erros, além de rotas para verificações de liveness e para expor as métricas coletadas.

## Arquivos no Repositório

### `app.py`

Este é o arquivo principal da aplicação Flask. Ele define três rotas principais:

- `/example`: Uma rota de exemplo que incrementa contadores de métricas para solicitações bem-sucedidas e erros simulados.
- `/live`: Uma rota de liveness probe que sempre retorna "OK".
- `/metrics`: Uma rota que expõe as métricas coletadas para o Prometheus.

A aplicação utiliza a biblioteca `prometheus_client` para definir e incrementar as métricas. Esta biblioteca facilita a criação de métricas customizadas que podem ser coletadas pelo Prometheus.

### `Dockerfile`

Este arquivo contém as instruções para construir a imagem Docker da aplicação Flask. Aqui estão os passos principais:

1. Usa a imagem base `python:3.8-slim`.
2. Define `/app` como o diretório de trabalho.
3. Copia os arquivos do projeto para o diretório de trabalho no container.
4. Instala as dependências necessárias (`Flask` e `prometheus_client`) usando `pip`.
5. Expõe as portas `8080` para a aplicação Flask e `9101` para as métricas do Prometheus.
6. Define a variável de ambiente `FLASK_RUN_PORT` para `8080`.
7. Define o comando para iniciar a aplicação Flask.

## Como Usar

Para construir e executar a aplicação em um container Docker, siga estes passos:

1. Construa a imagem Docker:
2. Execute o container:

A aplicação estará acessível na porta `8080`, e as métricas do Prometheus estarão disponíveis na porta `9101` no caminho `/metrics`.

## Coleta de Métricas

Para coletar métricas desta aplicação usando o Prometheus, configure o Prometheus para raspar as métricas da porta `9101` no caminho `/metrics` do seu container.