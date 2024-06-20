# Visão Geral da Configuração do Kubernetes para AKS

Este README fornece uma visão geral dos arquivos de configuração do Kubernetes utilizados para configurar serviços no Azure Kubernetes Service (AKS). Cada arquivo tem um propósito específico e, juntos, eles configuram um ambiente robusto para hospedar uma aplicação web.

## deployment.yaml

- **Finalidade**: Define o deployment da versão 1 da aplicação web.
- **Recursos Criados**:
    - Um `Deployment` chamado `aks-helloworld` no namespace `hello-web-app-routing`, com 3 réplicas da aplicação.
    - Um `Service` do tipo `ClusterIP` chamado `aks-helloworld`, que expõe a aplicação na porta 80.

## deployment-v2.yaml

- **Finalidade**: Define o deployment da versão 2 da aplicação web.
- **Recursos Criados**:
    - Um `Deployment` chamado `aks-helloworld-v2` no namespace `hello-web-app-routing`, com 1 réplica da aplicação.
    - Um `Service` do tipo `ClusterIP` chamado `aks-helloworld-v2`, que expõe a aplicação na porta 80.

## ingress.yaml

- **Finalidade**: Configura o ingress para a versão 1 da aplicação web, permitindo acesso externo.
- **Recursos Criados**:
    - Um `Ingress` chamado `aks-helloworld` no namespace `hello-web-app-routing`, configurado para usar a classe de ingress `webapprouting.kubernetes.azure.com` e direcionar o tráfego para o serviço `aks-helloworld`.

## ingress-v2.yaml

- **Finalidade**: Configura o ingress para a versão 2 da aplicação web como um canário, direcionando uma porcentagem do tráfego para esta versão.
- **Recursos Criados**:
    - Um `Ingress` chamado `aks-helloworld-v2` no namespace `hello-web-app-routing`, com anotações para configurá-lo como um canário, direcionando 10% do tráfego para o serviço `aks-helloworld-v2`.

## nginx-public-controller.yaml

- **Finalidade**: Define um controlador de ingress Nginx personalizado para gerenciar o acesso externo às aplicações.
- **Recursos Criados**:
    - Um `NginxIngressController` chamado `nginx-public`, configurado para usar a classe de ingress `nginx-public` e um prefixo de nome de controlador `nginx-public`.

Ao aplicar esses arquivos em um cluster AKS, você configurará dois deployments da aplicação web, cada um com seu próprio serviço. O ingress para a versão 1 permitirá acesso externo total, enquanto o ingress para a versão 2 direcionará uma fração do tráfego como teste canário. O controlador de ingress Nginx personalizado gerencia o acesso externo a essas aplicações.