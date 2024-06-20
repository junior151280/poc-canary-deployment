# Gateway

Este YAML define um `Gateway` no Istio, que é usado para configurar um ponto de entrada para o tráfego de entrada na malha de serviço (service mesh). Vamos detalhar cada configuração:

- `apiVersion: networking.istio.io/v1alpha3`: Especifica a versão da API do Istio que está sendo usada.
- `kind: Gateway`: Indica que o tipo de recurso é um Gateway, utilizado para configurar um ponto de entrada para o tráfego de entrada.
- `metadata`: Contém metadados sobre o Gateway.
  - `namespace: ns-canary-istio`: O namespace no Kubernetes onde este Gateway será aplicado.
  - `name: istio-http-gateway`: O nome do Gateway.
- `spec`: Especificações do Gateway.
  - `selector`: Define quais instâncias do ingress gateway este Gateway se aplica. 
    - `istio: aks-istio-ingressgateway-external`: Seleciona o ingress gateway com a etiqueta [`istio`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FProjetos%2Fpoc-canary-deployment%2Fistio%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Projetos\poc-canary-deployment\istio") igual a `aks-istio-ingressgateway-external`. Isso geralmente se refere a um conjunto específico de pods que estão configurados para atuar como um gateway de entrada.
  - `servers`: Define as configurações dos servidores no Gateway.
    - `port`: Configurações da porta para o servidor.
      - `number: 80`: A porta na qual o servidor está escutando. Neste caso, é a porta 80, comumente usada para tráfego HTTP.
      - `name: http`: O nome da porta, que pode ser usado para referência em outras configurações.
      - `protocol: HTTP`: O protocolo usado na porta. Aqui, especifica que o servidor aceitará tráfego HTTP.
    - `hosts`: Define para quais hosts o servidor irá responder.
      - `"*"`: Um caractere curinga que indica que o servidor responderá a qualquer host. Isso significa que o gateway aceitará tráfego para qualquer domínio que seja roteado para ele.

Em resumo, este `Gateway` no Istio configura um ponto de entrada para tráfego HTTP na porta 80 para qualquer host, utilizando um ingress gateway específico identificado pela etiqueta `istio: aks-istio-ingressgateway-external`. Isso permite que o tráfego de entrada seja gerenciado pela malha de serviço do Istio, onde políticas adicionais de roteamento, segurança e observabilidade podem ser aplicadas.