# VirtualService

Este YAML define um `VirtualService` no Istio, que é usado para configurar o roteamento de tráfego de entrada para diferentes serviços dentro da malha de serviço (service mesh). Vamos detalhar cada configuração:

- `apiVersion: networking.istio.io/v1alpha3`: Especifica a versão da API do Istio que está sendo usada.
- `kind: VirtualService`: Indica que o tipo de recurso é um VirtualService, utilizado para definir como o tráfego é roteado para um ou mais serviços.
- `metadata`: Contém metadados sobre o VirtualService.
  - `namespace: ns-canary-istio`: O namespace no Kubernetes onde este VirtualService será aplicado.
  - `name: vs-my-app`: O nome do VirtualService.
- `spec`: Especificações do VirtualService.
  - `hosts`: Define para quais hosts as regras de roteamento serão aplicadas. Neste caso, '*' significa que as regras serão aplicadas a todos os hosts.
  - `gateways`: Lista dos gateways que este VirtualService está associado. Aqui, `istio-http-gateway` indica que o tráfego de entrada através deste gateway será roteado conforme definido neste VirtualService.
  - `http`: Define as regras de roteamento para o tráfego HTTP.
    - `route`: Lista de regras de roteamento.
      - `destination`: Define o destino do tráfego.
        - `host: svc-my-app`: O nome do serviço de destino.
        - `subset: ds-v1`: O subconjunto do serviço de destino. Neste caso, direciona para o subconjunto `ds-v1`.
        - `port`: Especifica a porta do serviço de destino.
          - `number: 80`: A porta de destino é a 80.
        - `weight: 0`: O peso atribuído a este destino. Um peso de `0` significa que, sob condições normais, este destino não receberá tráfego.
      - `destination`: Define outro destino para o tráfego.
        - `host: svc-my-app`: O nome do serviço de destino, igual ao anterior.
        - `subset: ds-v2`: O subconjunto do serviço de destino, neste caso, `ds-v2`.
        - `port`: Especifica a porta do serviço de destino.
          - `number: 80`: A porta de destino é a 80, igual ao anterior.
        - `weight: 100`: O peso atribuído a este destino. Um peso de `100` significa que todo o tráfego será direcionado para este destino, já que o outro destino tem peso `0`.

Em resumo, este `VirtualService` define regras de roteamento para todo o tráfego de entrada através do gateway `istio-http-gateway`, direcionando 100% do tráfego para o subconjunto `ds-v2` do serviço `svc-my-app` na porta 80. O subconjunto `ds-v1` tem um peso de `0`, o que significa que, por padrão, ele não receberá tráfego. Este tipo de configuração é comumente usado em estratégias de implantação como canary, onde uma nova versão do serviço (`ds-v2`) é gradualmente exposta ao tráfego de produção enquanto monitora seu desempenho e estabilidade.