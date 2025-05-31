import csv
from flask import Flask, render_template, url_for, request, redirect
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre-mim')
def sobreEquipe():
    return render_template('sobre-mim.html')


@app.route('/glossario')
def glossario():
    
    glossarioDeTermos = []

    with open('bd_glossario.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo, delimiter=';')
        for linha in reader:
            glossarioDeTermos.append(linha)

    return render_template('glossario.html', glossario=glossarioDeTermos)


@app.route('/novo-termo')
def novoTermo():
    return render_template('novo-termo.html')


@app.route('/conteudo-python')
def conteudoPython():
    return render_template('conteudo-python.html')


@app.route('/criarTermo', methods=['POST'])
def criarTermo():

    termo = request.form['termo']
    definicao = request.form['definicao']

    with open('bd_glossario.csv', 'a', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        writer.writerow([termo, definicao])

    return redirect(url_for('glossario')) 

# Configuração do Google Generative AI
api_key = os.environ.get('GOOGLE_GENAI_API_KEY')
if api_key:
    genai.configure(api_key=api_key)
else:
    print('AVISO: GOOGLE_GENAI_API_KEY não definida no ambiente.')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot_page():
    resposta = None
    if request.method == 'POST':
        pergunta = request.form.get('pergunta')
        if pergunta:
            try:
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content([pergunta])
                resposta = response.candidates[0].content.parts[0].text if response.candidates else 'Sem resposta do modelo.'
            except Exception as e:
                import traceback
                print('ERRO GEMINI:', traceback.format_exc())
                resposta = f"Erro ao consultar Gemini: {str(e)}\n{traceback.format_exc()}"
    return render_template('chatbot.html', resposta=resposta)


@app.route('/estrutura-de-selecao.html')
def estrutura_de_selecao():
    return render_template('estrutura-de-selecao.html')

@app.route('/estrutura-de-repeticao.html')
def estrutura_de_repeticao():
    return render_template('estrutura-de-repeticao.html')

@app.route('/vetores-matriz.html')
def vetores_matriz():
    return render_template('vetores-matriz.html')

@app.route('/funcoes.html')
def funcoes():
    return render_template('funcoes.html')

@app.route('/excecoes.html')
def excecoes():
    return render_template('excecoes.html')


app.run(debug=True, port=5001)