# Use uma imagem base oficial do Python.
FROM python:3.10-slim

# Defina o diretório de trabalho no contêiner.
WORKDIR /app

# Copie o arquivo de dependências para o diretório de trabalho.
COPY requirements.txt .

# Instale as dependências.
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos da aplicação para o diretório de trabalho.
COPY . .

# Exponha a porta que o Streamlit usa.
EXPOSE 8501

# Comando para rodar a aplicação.
# O healthcheck verifica se o Streamlit está respondendo.
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# O comando de entrada para rodar a aplicação Streamlit.
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
