# Infraestrutura como Código para Testes de Deploy Canary

Este projeto contém um conjunto de arquivos Bicep projetados para provisionar a infraestrutura Azure necessária para executar testes de deploy canary. Cada arquivo serve a um propósito específico na configuração, criando um ambiente coeso onde os deploys canary podem ser testados efetivamente.

## Visão Geral dos Arquivos

### main.bicep

O arquivo `main.bicep` atua como o ponto de entrada para o deploy. Ele orquestra a criação do Azure Container Registry, do Serviço Kubernetes (AKS) e do Key Vault. Ele referencia outros módulos Bicep (`ContainerRegistry.bicep`, `Kubernetes.bicep`, `KeyVault.bicep`) para criar cada componente.

- **Azure Container Registry (ACR):** Usado para armazenar imagens Docker que serão implantadas no cluster AKS.
- **Azure Kubernetes Service (AKS):** O cluster Kubernetes onde as aplicações serão implantadas, permitindo testes canary.
- **Azure Key Vault:** Armazena segredos e certificados necessários pelas aplicações em execução no AKS.

### Kubernetes.bicep

O arquivo `Kubernetes.bicep` provisiona um cluster Azure Kubernetes Service (AKS). Ele inclui configurações para pools de nós, tamanhos de VM e vários complementos do Kubernetes como roteamento de aplicativos HTTP, Open Service Mesh, Istio Service Mesh e Kubernetes Event-Driven Autoscaling (KEDA).

### ContainerRegistry.bicep

O arquivo `ContainerRegistry.bicep` cria uma instância do Azure Container Registry (ACR). Este registro armazenará imagens Docker que podem ser implantadas no cluster AKS. Ele permite a especificação do SKU do registro, habilitando usuários administradores e definindo a localização do registro.

### KeyVault.bicep

O arquivo `KeyVault.bicep` configura um Azure Key Vault para armazenar segredos que as aplicações podem precisar. Ele configura políticas de acesso, ACLs de rede e provisiona segredos conforme definido nos parâmetros de entrada.

## Como Usar

Para implantar esta infraestrutura, siga estes passos:

1. **Pré-requisitos:**
    - Instale o Azure CLI e o Bicep CLI.
    - Faça login na sua conta Azure usando `az login`.

2. **Personalize os Parâmetros:**
    - Revise e personalize os parâmetros em `parameters.json` conforme necessário para o seu deploy.

3. **Deploy:**
    - Execute o seguinte comando para iniciar o deploy:
      ```bash
      az deployment group create --resource-group <SeuNomeDeGrupoDeRecursos> --template-file main.bicep --parameters parameters.json
      ```
    - Substitua `<SeuNomeDeGrupoDeRecursos>` pelo nome do seu grupo de recursos Azure.

4. **Verifique o Deploy:**
    - Uma vez que o deploy esteja completo, verifique os recursos no portal Azure ou usando o Azure CLI para garantir que tudo esteja configurado conforme esperado.

Esta configuração fornece uma base sólida para executar testes de deploy canary, permitindo que você implante gradualmente alterações para um pequeno subset de usuários antes de um rollout completo.