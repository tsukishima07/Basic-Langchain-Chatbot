
import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

# Initialize model
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Answer clearly and simply."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

# Create chain
chain = prompt | model

# Streamlit page
st.set_page_config(
    page_title="LangChain Chatbot",
    page_icon="🤖"
)

st.title("🤖 LangChain AI Chatbot")
st.caption("Built using LangChain, Groq and Streamlit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Ask me anything..."):

    # Display user message
    st.chat_message("user").markdown(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Prepare conversation history
    history = []

    for message in st.session_state.messages[:-1]:
        history.append((
            "human" if message["role"] == "user" else "ai",
            message["content"]
        ))

    # Generate AI response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        for chunk in chain.stream({
            "history": history,
            "question": user_input
        }):
            full_response += chunk.content
            response_placeholder.markdown(full_response + "▌")

        response_placeholder.markdown(full_response)

    # Save AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })

# Clear conversation button
if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
