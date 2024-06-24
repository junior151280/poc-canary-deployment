# Configuração do Prometheus para Métricas no AKS

Este guia fornece uma visão geral de como os arquivos de configuração `ama-metrics-settings-configmap.yaml` e `ama-metrics-prometheus-config-configmap.yaml` são usados para configurar o Prometheus para capturar métricas de aplicações que rodam no Azure Kubernetes Service (AKS).

## ama-metrics-settings-configmap.yaml

Este arquivo de configuração `ConfigMap` é usado para definir várias configurações relacionadas à coleta de métricas pelo agente de monitoramento no AKS. Ele inclui configurações como:

- **Versão do esquema e versão da configuração:** Identificadores usados pelo agente para interpretar o arquivo de configuração e pelo cliente para rastrear a versão do arquivo em seu controle de versão.
- **Configurações do coletor do Prometheus:** Define o alias do cluster e várias configurações de raspagem padrão para serviços específicos dentro do cluster, como `kubelet`, `cadvisor`, `nodeexporter`, entre outros.
- **Raspagem baseada em anotação de pod:** Utiliza uma expressão regular para determinar quais namespaces devem ser raspados com base em anotações de pod, permitindo uma coleta de métricas mais granular.
- **Lista de métricas a manter:** Especifica quais métricas devem ser mantidas para cada serviço monitorado.
- **Intervalos de raspagem:** Define intervalos de raspagem personalizados para cada serviço monitorado.
- **Modo de depuração:** Permite ativar o modo de depuração para facilitar a solução de problemas.

## ama-metrics-prometheus-config-configmap.yaml

Este arquivo `ConfigMap` contém a configuração específica do Prometheus, definindo como as métricas devem ser coletadas dentro do cluster AKS. As configurações incluem:

- **Intervalo global de raspagem:** Define o intervalo padrão para a coleta de métricas.
- **Configurações de raspagem:** Especifica os trabalhos de raspagem, incluindo o nome do trabalho, os alvos de raspagem (endereços dos serviços a serem monitorados) e quaisquer rótulos adicionais a serem aplicados às métricas coletadas.

## Como Usar

Para utilizar essas configurações no seu cluster AKS, siga os passos abaixo:

1. **Aplicar os ConfigMaps:**
    - Use o comando `kubectl apply -f ama-metrics-settings-configmap.yaml` para aplicar o ConfigMap de configurações do Prometheus.
    - Use o comando `kubectl apply -f ama-metrics-prometheus-config-configmap.yaml` para aplicar o ConfigMap de configuração específica do Prometheus.

2. **Verificar a Configuração:**
    - Após aplicar os ConfigMaps, verifique se eles foram corretamente aplicados usando `kubectl get configmap -n kube-system`.

3. **Monitoramento:**
    - Com as configurações aplicadas, o Prometheus começará a coletar métricas conforme definido nos arquivos de configuração. Você pode acessar o dashboard do Prometheus para visualizar as métricas coletadas.

Esses arquivos de configuração permitem um controle detalhado sobre o que é monitorado dentro do seu cluster AKS e como as métricas são coletadas, facilitando a observabilidade e o monitoramento de suas aplicações.