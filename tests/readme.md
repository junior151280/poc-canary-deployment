# Guia de Teste das Aplicações Demo com NGINX e Istio

Este documento fornece uma visão geral dos scripts `ngnix-test.py` e `istio-test.py`, explicando suas funcionalidades e como podem ser utilizados para testar aplicações demo utilizando NGINX e Istio, respectivamente.

## ngnix-test.py

### Descrição
O script `ngnix-test.py` é utilizado para testar a disponibilidade e o comportamento de uma aplicação web hospedada atrás de um servidor NGINX. Ele faz requisições HTTP para a aplicação e verifica o conteúdo da resposta para determinar a versão da aplicação que está sendo servida.

### Funcionalidades
- Faz requisições HTTP para um endereço web especificado.
- Verifica o título da página para determinar a versão da aplicação (AKS Versão 2.0 ou a versão padrão).
- Contabiliza e reporta diferentes tipos de erros de conexão e requisição, como timeouts de leitura e conexão, erros HTTP e erros desconhecidos.

### Como Usar
1. Execute o script passando o endereço IP da aplicação como argumento.
2. Opcionalmente, um segundo argumento pode ser fornecido para especificar um cabeçalho HTTP personalizado.
3. O script imprimirá mensagens coloridas no terminal para indicar o resultado de cada teste, incluindo a versão da aplicação detectada e um resumo dos erros encontrados.

## istio-test.py

### Descrição
O script `istio-test.py` é projetado para testar aplicações que estão sendo executadas em um ambiente Kubernetes gerenciado pelo Istio. Ele verifica a versão da aplicação respondendo às requisições HTTP, baseando-se na presença de strings específicas no corpo da resposta.

### Funcionalidades
- Realiza requisições HTTP para a aplicação, utilizando ou não cabeçalhos HTTP personalizados.
- Identifica a versão da aplicação com base no conteúdo da resposta (v1.0.0 ou v2.0.0).
- Registra e reporta erros de conexão, leitura, erros HTTP e exceções desconhecidas.

### Como Usar
1. Inicie o script com o endereço IP da aplicação como o primeiro argumento.
2. Se necessário, um cabeçalho HTTP personalizado pode ser especificado como o segundo argumento.
3. O script exibirá mensagens coloridas para indicar a versão da aplicação e um resumo dos erros encontrados durante o teste.

## Conclusão
Ambos os scripts são ferramentas úteis para testar a disponibilidade e o comportamento de aplicações web em diferentes ambientes de hospedagem. Eles automatizam o processo de teste e fornecem feedback visual imediato sobre o estado da aplicação, facilitando a identificação e a resolução de problemas.