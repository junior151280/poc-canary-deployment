# Prova de Conceito: Canary Deployment em AKS

Este repositório é uma coleção de arquivos e configurações destinados a facilitar o deploy e a gestão de aplicações em um ambiente Kubernetes, especificamente no Azure Kubernetes Service (AKS). Ele inclui exemplos de configurações para deploy canário, monitoramento com Prometheus, roteamento com Istio, e a infraestrutura necessária provisionada através de Bicep para testes de deploy canário no Azure.

## Estrutura do Repositório

A estrutura do repositório é organizada por diretórios, cada um contendo componentes específicos para a configuração e o deploy de aplicações e infraestrutura:

- `agic/`: Contém arquivos de configuração para o Application Gateway Ingress Controller no AKS.
- `app/`: Inclui o código fonte de uma aplicação Flask instrumentada para expor métricas para o Prometheus, juntamente com um Dockerfile para containerização.
- `bicep/`: Armazena arquivos Bicep para provisionar a infraestrutura Azure necessária, como Azure Container Registry, Azure Kubernetes Service, e Azure Key Vault.
- `grafana/`: Contém configurações para visualizar métricas no Grafana.
- `istio/`: Inclui arquivos de configuração para o uso do Istio no AKS, facilitando o roteamento e deploy canário.
- `nginx/`: Armazena configurações para o uso do NGINX como ingress controller no AKS.
- `prometheus/`: Diretório destinado às configurações do Prometheus para coleta de métricas.
- `test-env/`: Contém arquivos para configuração de ambientes de teste.
- `tests/`: Diretório para armazenar testes automatizados.

## Descrição dos Arquivos Principais

- `app/readme.md`: Fornece uma visão geral da aplicação Flask, incluindo instruções para construir e executar a aplicação em um container Docker, e como coletar métricas com o Prometheus.
- `bicep/readme.md`: Descreve a finalidade de cada arquivo Bicep no diretório `bicep/`, explicando como eles provisionam a infraestrutura necessária no Azure para deploy canário.
- `istio/readme.md`: Oferece uma visão geral dos arquivos de configuração do Kubernetes incluídos para configurar o namespace, deployments, e serviços com Istio para deploy canário.
- `nginx/readme.md`: Explica a configuração do Kubernetes para AKS, detalhando os arquivos para deploy e ingress de aplicações web.

Este repositório é uma ferramenta abrangente para desenvolvedores e engenheiros de infraestrutura que buscam implementar práticas modernas de deploy, monitoramento e gestão de aplicações em ambientes Kubernetes, especialmente no Azure.
