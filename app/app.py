from flask import Flask, Response, request
from prometheus_client import Counter, generate_latest

# Criar a aplicação Flask
app = Flask(__name__)

# Definir um contador de métricas para falhas/erros
REQUEST_ERRORS = Counter('app_request_errors_total', 'Total de requests com erro')
REQUEST_EXAMPLES = Counter('app_request_examples_total', 'Total de requests para a rota de exemplo')

# Rota de exemplo que pode falhar
@app.route('/example')
def example_route():
    REQUEST_EXAMPLES.inc()
    if request.args.get('fail'):
        # Simular uma falha
        REQUEST_ERRORS.inc()  # Incrementar o contador de erros
        return "Erro simulado", 500
    return "Sucesso", 200

# Rota para o probe de readiness
@app.route('/live')
def liveness_probe():
    return "OK", 200

# Rota para expor as métricas para o Prometheus
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9101)