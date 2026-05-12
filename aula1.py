from flask import Flask

app = Flask(__name__)

# Rota explicando o conceito de decorator
@app.route("/decorator")
def decorator():
    return """
    <h1>Decorator em Python</h1>

    <p>
    Um decorator é um recurso do Python usado para modificar ou adicionar
    funcionalidades a funções sem alterar o código original delas.
    </p>

    <p>
    Ele serve para reutilizar código, organizar melhor o programa
    e adicionar comportamentos extras, como autenticação,
    validação e registro de informações.
    </p>

    <p>
    No Flask, os decorators são utilizados para definir rotas.
    Por exemplo: <b>@app.route('/decorator')</b> indica que a função abaixo
    será executada quando o usuário acessar esse endereço no navegador.
    </p>
    """

if __name__ == "__main__":
    app.run(debug=True)