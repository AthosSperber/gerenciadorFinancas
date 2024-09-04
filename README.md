# Gerenciador de Finanças com Visualização de Dados e Reconhecimento de Recibos

Este projeto é um **Gerenciador de Finanças Pessoais** desenvolvido com Django, que oferece funcionalidades avançadas, como visualização de dados financeiros e reconhecimento de recibos. O aplicativo é dividido em módulos que facilitam a organização e a extensão do projeto.

## Funcionalidades Principais

### 1. Gerenciamento de Finanças Pessoais
- **Adicionar Transações**: Permite a inserção de receitas e despesas, registrando todas as transações financeiras.
- **Exibição de Saldo e Transações**: Visualize o saldo total e todas as transações em uma interface intuitiva.

### 2. Visualização de Dados
- **Gráficos Interativos**: Visualize suas receitas e despesas através de gráficos interativos.  
  - **Tecnologia utilizada**: ![Python](https://img.shields.io/badge/-Matplotlib-3776AB?logo=python&logoColor=white) ![Seaborn](https://img.shields.io/badge/-Seaborn-3776AB?logo=python&logoColor=white)

### 3. Web Scraping
- **Coleta de Dados Externos**: Realiza a extração de informações financeiras externas, como cotações de moedas e ações, e exibe esses dados no painel do usuário.
  - **Tecnologia utilizada**: ![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup-FFD700?logo=python&logoColor=white) ![Requests](https://img.shields.io/badge/-Requests-FFD700?logo=python&logoColor=white)

### 4. Reconhecimento de Recibos
- **OCR para Recibos**: Implementa reconhecimento de texto em imagens de recibos, automatizando a entrada de dados financeiros.
  - **Tecnologia utilizada**: ![Tesseract OCR](https://img.shields.io/badge/-Tesseract%20OCR-32CD32?logo=python&logoColor=white) ![pytesseract](https://img.shields.io/badge/-pytesseract-32CD32?logo=python&logoColor=white)

## Tecnologias Utilizadas
- ![Django](https://img.shields.io/badge/-Django-092E20?logo=django&logoColor=white): Framework principal para o desenvolvimento do aplicativo web.
- ![Matplotlib](https://img.shields.io/badge/-Matplotlib-3776AB?logo=python&logoColor=white) e ![Seaborn](https://img.shields.io/badge/-Seaborn-3776AB?logo=python&logoColor=white): Bibliotecas utilizadas para gerar gráficos de visualização de dados.
- ![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup-FFD700?logo=python&logoColor=white) e ![Requests](https://img.shields.io/badge/-Requests-FFD700?logo=python&logoColor=white): Utilizados para web scraping de informações financeiras.
- ![Tesseract OCR](https://img.shields.io/badge/-Tesseract%20OCR-32CD32?logo=python&logoColor=white): Ferramenta de reconhecimento óptico de caracteres para extração de dados de recibos.
- ![SQLite](https://img.shields.io/badge/-SQLite-003B57?logo=sqlite&logoColor=white): Banco de dados para armazenamento local das transações financeiras.
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white): Linguagem principal utilizada para o desenvolvimento do projeto.

## Como Executar o Projeto

### Pré-requisitos
- ![Python](https://img.shields.io/badge/-Python%203.x-3776AB?logo=python&logoColor=white)
- ![Django](https://img.shields.io/badge/-Django%203.x-092E20?logo=django&logoColor=white)
- [![](https://img.shields.io/badge/-Tesseract%20OCR-32CD32?logo=python&logoColor=white)](https://github.com/tesseract-ocr/tesseract)

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/AthosSperber/gerenciadorFinancas.git
2. Navegue até o diretório do projeto:
   ```bash
    cd gerenciadorFinancas
3. Crie um ambiente virtual (Para evitar conflitos de dependências, é recomendável criar um ambiente virtual):
  ```bash
    python -m venv venv
  ```
  ```
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
  ```
4. Instale as Dependências:
   ```bash
   pip install -r requirements.txt
   
5. Realize as migrações e execute o servidor:
  ```bash
python manage.py migrate
python manage.py runserver
  ```
Acesse o aplicativo em http://127.0.0.1:8000 e comece a gerenciar suas finanças!
