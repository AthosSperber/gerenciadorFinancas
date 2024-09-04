# Gerenciador de Finanças com Visualização de Dados e Reconhecimento de Recibos

Este projeto é um **Gerenciador de Finanças Pessoais** desenvolvido com Django, que oferece funcionalidades avançadas, como visualização de dados financeiros e reconhecimento de recibos. O aplicativo é dividido em módulos que facilitam a organização e a extensão do projeto.

## ![#f03c15](https://via.placeholder.com/15/f03c15/000000?text=+) Funcionalidades Principais

### 1. Gerenciamento de Finanças Pessoais
- **Adicionar Transações**: Permite a inserção de receitas e despesas, registrando todas as transações financeiras.
- **Exibição de Saldo e Transações**: Visualize o saldo total e todas as transações em uma interface intuitiva.

### 2. Visualização de Dados
- **Gráficos Interativos**: Visualize suas receitas e despesas através de gráficos interativos.  
  - **Tecnologia utilizada**: ![#4169e1](https://via.placeholder.com/15/4169e1/000000?text=+) `Matplotlib` e `Seaborn`.

### 3. Web Scraping
- **Coleta de Dados Externos**: Realiza a extração de informações financeiras externas, como cotações de moedas e ações, e exibe esses dados no painel do usuário.
  - **Tecnologia utilizada**: ![#ff69b4](https://via.placeholder.com/15/ff69b4/000000?text=+) `BeautifulSoup` e ![#ff69b4](https://via.placeholder.com/15/ff69b4/000000?text=+) `Requests`.

### 4. Reconhecimento de Recibos
- **OCR para Recibos**: Implementa reconhecimento de texto em imagens de recibos, automatizando a entrada de dados financeiros.
  - **Tecnologia utilizada**: ![#32cd32](https://via.placeholder.com/15/32cd32/000000?text=+) `Tesseract OCR` (via biblioteca Python ![#32cd32](https://via.placeholder.com/15/32cd32/000000?text=+) `pytesseract`).

## ![#1e90ff](https://via.placeholder.com/15/1e90ff/000000?text=+) Tecnologias Utilizadas
- ![#f0e68c](https://via.placeholder.com/15/f0e68c/000000?text=+) **`Django`**: Framework principal para o desenvolvimento do aplicativo web.
- ![#4169e1](https://via.placeholder.com/15/4169e1/000000?text=+) **`Matplotlib`** e ![#4169e1](https://via.placeholder.com/15/4169e1/000000?text=+) **`Seaborn`**: Bibliotecas utilizadas para gerar gráficos de visualização de dados.
- ![#ff69b4](https://via.placeholder.com/15/ff69b4/000000?text=+) **`BeautifulSoup`** e ![#ff69b4](https://via.placeholder.com/15/ff69b4/000000?text=+) **`Requests`**: Utilizados para web scraping de informações financeiras.
- ![#32cd32](https://via.placeholder.com/15/32cd32/000000?text=+) **`Tesseract OCR`**: Ferramenta de reconhecimento óptico de caracteres para extração de dados de recibos.
- ![#ffa500](https://via.placeholder.com/15/ffa500/000000?text=+) **`SQLite`**: Banco de dados para armazenamento local das transações financeiras.
- ![#ff4500](https://via.placeholder.com/15/ff4500/000000?text=+) **`Python`**: Linguagem principal utilizada para o desenvolvimento do projeto.

## ![#32cd32](https://via.placeholder.com/15/32cd32/000000?text=+) Como Executar o Projeto

### Pré-requisitos
- ![#ff4500](https://via.placeholder.com/15/ff4500/000000?text=+) **`Python 3.x`**
- ![#f0e68c](https://via.placeholder.com/15/f0e68c/000000?text=+) **`Django 3.x`**
- [![](https://via.placeholder.com/15/32cd32/000000?text=+)](https://github.com/tesseract-ocr/tesseract) **`Tesseract OCR`**

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/AthosSperber/gerenciadorFinancas.git
