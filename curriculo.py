from flask import Flask

app = Flask(__name__)

@app.route("/")
def curriculo():
    return """
    <html>
    <head>
        <title>Currículo - Arthur Ferraz Nascimento</title>

        
    </head>

    <body>

        <div class="curriculo">

            <h1>Arthur Ferraz Nascimento</h1>

            <p><b>Cidade:</b> Belo Horizonte - MG</p>
            <p><b>Área de Interesse:</b> Desenvolvimento de Sistemas e Tecnologia</p>

            <h2>Objetivo</h2>

            <p>
                Buscar oportunidades para desenvolver experiência prática
                na área de programação e tecnologia, aprimorando conhecimentos
                em desenvolvimento web, banco de dados e lógica de programação.
            </p>

            <h2>Formação</h2>

            <ul>
                <li>Ensino Médio Técnico em Informática - Em andamento</li>
            </ul>

            <h2>Conhecimentos</h2>

            <ul>
                <li>Python</li>
                <li>MySQL</li>
                <li>PHP + PDO</li>
                <li>CRUD</li>
                <li>HTML e CSS</li>
                <li>Lógica de Programação</li>
                <li>Montagem e manutenção de computadores</li>
            </ul>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)