# DestinationRule

Este YAML define um `DestinationRule` no Istio, que é usado para configurar como o tráfego é roteado para um serviço dentro da malha de serviço (service mesh). Vamos detalhar cada configuração:

- `apiVersion: networking.istio.io/v1alpha3`: Especifica a versão da API do Istio que está sendo usada.
- `kind: DestinationRule`: Indica que o tipo de recurso é um DestinationRule, utilizado para definir políticas aplicadas ao tráfego após a rota ter sido determinada.
- `metadata`: Contém metadados sobre o DestinationRule.
  - `namespace: ns-canary-istio`: O namespace no Kubernetes onde este DestinationRule será aplicado.
  - `name: my-app`: O nome do DestinationRule.
- `spec`: Especificações do DestinationRule.
  - `host: '*'`: Define para qual host as regras serão aplicadas. Neste caso, '*' significa que as regras serão aplicadas a todos os hosts.
  - `subsets`: Define os subconjuntos de serviços para os quais as regras de tráfego específicas serão aplicadas.
    - `name: ds-v1`: Nome do primeiro subconjunto.
      - `labels`: Define os rótulos usados para identificar as instâncias do serviço dentro deste subconjunto.
        - `version: v1.0.0`: Especifica que este subconjunto consiste em instâncias com a etiqueta `version` igual a `v1.0.0`.
      - `trafficPolicy`: Política de tráfego para este subconjunto.
        - `loadBalancer`: Define a política de balanceamento de carga.
          - `consistentHash`: Usa um hash consistente para o balanceamento de carga.
            - `httpCookie`: Define que o hash será baseado em um cookie HTTP.
              - `name: user`: Nome do cookie usado para o hash.
              - `ttl: 0s`: Tempo de vida do cookie. `0s` significa que o cookie é temporário e não será armazenado.
    - `name: ds-v2`: Nome do segundo subconjunto.
      - `labels`: Define os rótulos para este subconjunto.
        - `version: v2.0.0`: Este subconjunto consiste em instâncias com a etiqueta `version` igual a `v2.0.0`.
      - `trafficPolicy`: Política de tráfego para este subconjunto.
        - `loadBalancer`: Define a política de balanceamento de carga.
          - `simple`: Usa uma política de balanceamento de carga simples.
            - `LEAST_REQUEST`: O balanceamento de carga será feito direcionando as novas solicitações para a instância com o menor número de solicitações pendentes.

Em resumo, este `DestinationRule` define políticas de roteamento e balanceamento de carga para duas versões de um serviço (`v1.0.0` e `v2.0.0`). Para o subconjunto `ds-v1`, o balanceamento de carga é feito com base em um hash consistente de um cookie chamado `user`, o que é útil para garantir que um usuário específico seja sempre direcionado para a mesma instância do serviço. Para o subconjunto `ds-v2`, o balanceamento de carga é feito escolhendo a instância com o menor número de solicitações pendentes (`LEAST_REQUEST`), o que pode ajudar a distribuir o tráfego de maneira mais uniforme entre as instâncias.