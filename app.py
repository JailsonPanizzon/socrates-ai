import time
import streamlit as st
from baml_client.sync_client import b
from baml_client.async_client import b as b_async
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Socretes AI Mentor GPT - PBL", layout="centered")

st.title("🧠 Socretes AI Mentor GPT - PBL")

# Inicializar o histórico de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico de mensagens
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do usuário
if prompt := st.chat_input("Descreva o problema:"):
    # Adiciona a pergunta ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Exibe a pergunta do usuário
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara o bloco do assistente
    with st.chat_message("assistant"):
        response_placeholder = st.empty()  # Placeholder para o stream
        full_response = ""
        response_placeholder.markdown("Pensando...")
        time.sleep(1)

        try:
            # Inicia o stream BAML
            stream = b.stream.AskHeuristicQuestion(prompt)
            
            # Processa cada chunk
            for chunk in stream:
                full_response = chunk
                response_placeholder.markdown(full_response)  # Atualiza dinamicamente
                time.sleep(0.1)

        except Exception as e:
            full_response = f"⚠️ Erro: {str(e)}"
            response_placeholder.markdown(full_response)

    # Adiciona a resposta FINAL ao histórico (após o loop)
    st.session_state.messages.append({"role": "assistant", "content": full_response})