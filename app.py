import streamlit as st
from streamlit_chat import message
import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

st.set_page_config(
    page_title="Chatbot",
    page_icon=":robot:"
)


st.header("Chatbot Demo using `Streamlit and GPT-4`")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if 'total_conversation' not in st.session_state:
    st.session_state['total_conversation'] = [{'role':'system','content':'I want you to act as a travel guide Murphy. I will write you my location and you will suggest a place to visit near my location. In some cases, I will also give you the type of places I will visit. You will also suggest me places of similar type that are close to my first location. Do not make answers longer than 50 words. Your tone is friendly'}]

def query(user_text):
    response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=st.session_state.total_conversation
    )
    
    message = response.choices[0].message.content
    # Adding bot response to the 
    st.session_state.total_conversation.append({'role':'system','content':message})
    return message

def get_text():
    input_text = st.text_input("You: ","Hello, How are you?", key="input")
    return input_text 


user_input = get_text()

if user_input:
    output = query(st.session_state.total_conversation.append({'role':'user','content':user_input}))

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
