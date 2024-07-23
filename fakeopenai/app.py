from openai import OpenAI
# streamlit app framework
import streamlit as st

# go ahead and create a client

client = OpenAI(api_key='jhjhjh1234', base_url="http://localhost:8000/v1")


st.title('OpenAI Server App')

prompt = st.chat_input('Pass your prompt here')

if prompt:
    st.chat_message('user').markdown(prompt)


    response = client.chat.completions.create(
            model='models/mistral-7b-instruct-v0.1.Q4_0.gguf', 
            messages=[{
            'role': 'user',
            'content': prompt
            
        }],
        stream=True
    )

    with st.chat_message('ai'):
        completed_message = ""
        message = st.empty()

    # streaming response in CLI
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            completed_message += chunk.choices[0].delta.content 
            message.markdown(completed_message)
            print(chunk.choices[0].delta.content, flush=True, end='')
