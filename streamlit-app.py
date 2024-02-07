import streamlit as st

st.title("Markov Chain Mixtral Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

import openai

fw_client = openai.OpenAI(
  api_key=st.secrets.fireworks.api_key,
  base_url=st.secrets.fireworks.base_url,
)

def generate_response(prompt: str):
    response = fw_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model= st.secrets.model.llm_big_model,
        max_tokens=2048,
    )

    # print(response.choices[0].message.content)
    return response.choices[0].message.content 

# React to user input
with st.chat_message('assistant'):
    st.markdown("Hi, I'm an mixtral markov agent. I have no memory and behave like a markov chain, means I can interact only with the very last prompt.")
if prompt := st.chat_input("Scope of interest among Artificial Intelligence:"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = generate_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})