from flask import Flask

app = Flask(__name__)


@app.route("/")
def Curriculo():
    return
    """
        <!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Currículo - Mateus Ricardo Ramos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 30px auto;
            background: #fff;
            padding: 40px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            border-radius: 8px;
        }
        header {
            text-align: center;
            border-bottom: 2px solid #0056b3;
            padding-bottom: 20px;
            margin-bottom: 25px;
        }
        h1 {
            margin: 0 0 10px 0;
            color: #111;
            font-size: 28px;
        }
        p.subtitle {
            margin: 0;
            color: #666;
            font-size: 16px;
            font-weight: bold;
        }
        .contact-info {
            margin-top: 10px;
            font-size: 14px;
        }
        .contact-info a {
            color: #0056b3;
            text-decoration: none;
        }
        section {
            margin-bottom: 25px;
        }
        h2 {
            color: #0056b3;
            font-size: 20px;
            border-bottom: 1px solid #ddd;
            padding-bottom: 5px;
            margin-top: 0;
        }
        .item {
            margin-bottom: 15px;
        }
        .item-title {
            font-weight: bold;
            color: #222;
        }
        .item-details {
            font-size: 14px;
            color: #666;
            font-style: italic;
            margin-bottom: 5px;
        }
        .skills-list {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding: 0;
            list-style: none;
        }
        .skills-list li {
            background: #eef2f7;
            padding: 6px 12px;
            border-radius: 4px;
            font-size: 14px;
            color: #444;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>Mateus Ricardo Ramos</h1>
        <p class="subtitle">Estagiário de Desenvolvimento Web</p>
        <div class="contact-info">
            E-mail: <a href="mailto:mateusricardoramos@email.com">mateusricardoramos@email.com</a> | 
            Telefone: (31) 98204-5440 | 
            Belo Horizonte - MG <br>
            <a href="https://linkedin.com" target="_blank">LinkedIn</a> | 
            <a href="https://github.com" target="_blank">GitHub (Portfólio)</a>
        </div>
    </header>

    <section>
        <h2>Objetivo Profissional</h2>
        <p>Estudante de desenvolvimento web em busca de oportunidade de estágio. Objetivo de aplicar conhecimentos teóricos em projetos reais, colaborar com a equipe e evoluir tecnicamente rumo a cargos de liderança no futuro.</p>
    </section>

    <section>
        <h2>Formação Acadêmica</h2>
        <div class="item">
            <div class="item-title">Ensino Médio Integrado ao Curso Técnico em Informática</div>
            <div class="item-details">Colégio Cotemig | 2024 – 2026 (Em andamento)</div>
        </div>
    </section>

    <section>
        <h2>Principais Competências</h2>
        <ul class="skills-list">
            <li>HTML5 & CSS3</li>
            <li>JavaScript (Básico)</li>
            <li>Desenvolvimento Web</li>
            <li>Manutenção de Hardware</li>
            <li>Gestão de Tempo</li>
            <li>Trabalho em Equipe</li>
            <li>Inglês Intermediário</li>
        </ul>
    </section>
</div>

</body>
</html>

    """


if __name__ == "__main__":
    app.run(debug=True)
