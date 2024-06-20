# Visão Geral dos Arquivos de Configuração do Kubernetes

Este README fornece uma visão geral dos arquivos de configuração do Kubernetes incluídos nesta configuração, seu propósito e os recursos que serão criados quando aplicados a um cluster do Azure Kubernetes Service (AKS).

## namespace.yaml

- **Finalidade**: Cria um novo namespace Kubernetes para organizar recursos relacionados ao deployment canário com Istio.
- **Recursos Criados**:
  - Um namespace chamado `ns-canary-istio` com um rótulo `istio.io/rev: asm-1-20` indicando a revisão do Istio pretendida para uso com este namespace.

## app-v1.yaml

- **Finalidade**: Implanta a versão 1 da aplicação, semelhante ao `app-v2.yaml`, mas para a versão inicial da aplicação.
- **Recursos Criados**:
  - Um `Deployment` chamado `deployment-my-app-v1` no namespace `ns-canary-istio`, com uma única réplica do pod da aplicação rotulado `version: v1.0.0`. Também inclui sondas de vivacidade e prontidão, solicitações de recursos e um gancho de ciclo de vida de pré-parada.

## app-v2.yaml

- **Finalidade**: Implanta a versão 2 da aplicação, incluindo configurações para escalonamento, verificações de saúde e monitoramento do Prometheus.
- **Recursos Criados**:
  - Um `Deployment` chamado `deployment-my-app-v2` no namespace `ns-canary-istio`, com uma única réplica do pod da aplicação rotulado `version: v2.0.0`. Inclui configurações para sondas de vivacidade e prontidão, solicitações de recursos e um gancho de ciclo de vida de pré-parada.

## service.yaml

- **Finalidade**: Define um Serviço Kubernetes para a aplicação. Este serviço atua como um balanceador de carga interno para distribuir o tráfego entre os pods da aplicação.
- **Recursos Criados**:
  - Um serviço `ClusterIP` chamado `svc-my-app` no namespace `ns-canary-istio`, direcionando pods com o rótulo `app: my-app` na porta 80.

## istio.yaml

- **Finalidade**: Configura recursos do Istio para gerenciar o tráfego de entrada e regras de roteamento para deployments canários.
- **Recursos Criados**:
  - Um `Gateway` Istio chamado `istio-http-gateway` no namespace `ns-canary-istio` para lidar com o tráfego HTTP de entrada.
  - Um `VirtualService` chamado `vs-my-app` para rotear o tráfego para diferentes versões da aplicação com base em pesos.
  - Uma `DestinationRule` chamada `my-app` definindo subconjuntos (`ds-v1` e `ds-v2`) para rotear o tráfego para diferentes versões dos pods da aplicação.

## hpa.yaml

- **Finalidade**: Define Horizontal Pod Autoscalers (HPA) para escalar automaticamente os pods da aplicação com base na utilização da CPU.
- **Recursos Criados**:
  - Dois HPAs, `hpa-my-app-v1` e `hpa-my-app-v2`, direcionando os deployments `deployment-my-app-v1` e `deployment-my-app-v2` respectivamente, no namespace `ns-canary-istio`. Ambos estão configurados para escalar entre 1 e 10 réplicas com base em uma utilização de CPU alvo de 80%.

Aplicar esses arquivos a um cluster AKS configurará um namespace para a aplicação, implantará duas versões da aplicação com escalonamento automático baseado no uso da CPU e configurará o Istio para gerenciar o tráfego de entrada e o roteamento para deployments canários.