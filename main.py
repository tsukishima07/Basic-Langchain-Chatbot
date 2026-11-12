
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

load_dotenv()

# Initialize LLM
model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Remember the conversation context."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

# Create basic chain
chain = prompt | model

# Store conversation histories
store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]

# Add conversation history to chain
chatbot = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

session_id = "user_1"

print("===== Memory Enabled Chatbot =====")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = chatbot.invoke(
        {"question": user_input},
        config={"configurable": {"session_id": session_id}}
    )

    print("AI:", response.content)
