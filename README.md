# Projeto Final - Fundamentos de Programação em Python
# Aluno: Victor Alexandre Medeiros Araújo Aires
# Turma: SPI P1 - Noite

## Objetivo Geral
Desenvolver uma aplicação web interativa utilizando o framework Flask para criar um site informativo sobre os fundamentos da programação em Python. O projeto inclui uma funcionalidade de perguntas e respostas integrada com a API do Gemini e um dicionário interativo de termos de programação com persistência em arquivo de texto.

## Requisitos do Projeto
1. **Estrutura Flask:**
   - Utilização do framework Flask para criação de rotas, uso de templates e manipulação de dados via formulários.
2. **Página sobre a Equipe:**
   - Página dedicada apresentando os membros da equipe, nomes, links para redes sociais profissionais e outras informações relevantes.
3. **Conteúdo do Site:**
   - Seções informativas sobre fundamentos da programação em Python, incluindo conceito, aplicação e exemplo de código para:
     - Estruturas de seleção
     - Estruturas de repetição
     - Vetores e matrizes
     - Funções e procedimentos
     - Tratamento de exceções
4. **Seção de Tirar Dúvidas (API Gemini):**
   - Funcionalidade para submeter perguntas e exibir respostas integradas à API do Gemini.
5. **Dicionário de Termos:**
   - Visualização de termos e definições
   - Adição de novos termos
   - Alteração de definições
   - Remoção de termos
6. **Persistência de Dados:**
   - Os termos do dicionário são armazenados em um arquivo de texto simples, com operações de leitura, escrita, atualização e exclusão.
7. **Interface de Usuário:**
   - Navegação clara e design amigável, incluindo as funcionalidades do dicionário.

## Estrutura do Site
- **Página Inicial:** Apresentação do projeto e navegação para as demais seções.
- **Sobre a Equipe:** Informações sobre os integrantes do grupo.
- **Conteúdo Python:** Seções didáticas sobre os principais fundamentos da linguagem.
- **Chatbot (Tirar Dúvidas):** Interface para perguntas e respostas via API Gemini.
- **Glossário:** Dicionário interativo de termos de programação.
- **Adicionar/Editar/Remover Termos:** Funcionalidades para gerenciar o glossário.

## Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Framework Web:** Flask
- **Templates:** Jinja2 (HTML)
- **Front-end:** HTML, CSS
- **Persistência:** Arquivo de texto CSV (`bd_glossario.csv`)
- **API Externa:** Gemini (para perguntas e respostas)

## Integração com a API do Gemini
A integração é feita via requisições HTTP para a API do Gemini. O usuário envia uma pergunta pelo formulário, a aplicação Flask processa a requisição, envia para a API e exibe a resposta recebida na interface do site.
**Para terceiros, será necessário inserir sua Api_key**

## Principais Partes do Código Python
- **`app.py`:**
  - Define as rotas do site (index, sobre, conteúdo, chatbot, glossário, adicionar/editar/remover termo).
  - Gerencia a lógica de leitura e escrita do arquivo de glossário.
  - Implementa a integração com a API do Gemini.
- **`bd_glossario.csv`:**
  - Arquivo de texto que armazena os termos e definições do dicionário.
- **`templates/`:**
  - Contém os arquivos HTML das páginas do site, utilizando Jinja2 para renderização dinâmica.
- **`static/`:**
  - Arquivos estáticos como imagens e estilos CSS.

## Observações Finais
- O design deve priorizar a usabilidade e clareza das informações.

---

Desenvolvido por Victor Alexandre M. A. Aires, para a disciplina de Fundamentos de Programação em Python.
