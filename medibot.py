
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage,HumanMessage
from database import get_message_history,save_message_history
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore")
import os
#Step 1: Setting API
os.environ['GROQ_API_KEY']="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"


# Step 2: Generate embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 3: Create a FAISS vectorstore
vectorstore = FAISS.load_local("Disease", embeddings, allow_dangerous_deserialization=True)
retreiver=vectorstore.as_retriever()


prompt=ChatPromptTemplate.from_messages([("system",'''
You are a cautious and friendly AI medical assistant. 
You will receive previous conversation history and the user's current message.
Use the conversation history to maintain context, remember what the user said earlier, 
and give consistent answers. Reply in the user's language.
When a user describes a symptom, follow these rules strictly:

1. Never jump to a disease name immediately.
2. If the user mentions only one or two symptoms, ask 1–2 follow-up questions to collect more details.
   Example: “Can you tell if you also have fever, cough, or body pain?”
3. Only suggest possible conditions **if three or more symptoms clearly match** a known pattern.
4. Always remind the user that you are not a doctor.
5. Avoid assuming serious diseases (like TB, cancer, or HIV) unless multiple strong symptoms are described.
6. If the message contains words related to masturbation, sleep, energy, or normal daily issues,
   reply with general wellness advice instead of disease prediction.
7. Keep your tone caring and conversational.
{context}

'''),
MessagesPlaceholder("chat_history"),
("human","{input}")]) # Changed {query} to {input} to match the input key


llm = ChatGroq(model="llama-3.3-70b-versatile")
#llm=ChatGroq(model="llama-3.1-8b-instant") # Example valid model - replace with your desired Groq model
history_aware_retreiver=create_history_aware_retriever(llm,retreiver,prompt)
qa_chain=create_stuff_documents_chain(llm,prompt) # Corrected function name
rag_chain=create_retrieval_chain(history_aware_retreiver,qa_chain)


def give_response(user_input,phno):
    chat_history=get_message_history(phno)

    if user_input.lower() in ["bye", "exit", "quit"]:
        return "🤖 Medical Bot: Goodbye! Take care."
    ans = rag_chain.invoke({
        "input": user_input,"chat_history":chat_history,"context":'''.'''
    })

    bot_response=ans['answer']

    chat_history.extend([
        f"User: {user_input}",
        f"Bot: {bot_response}"
    ])

    save_message_history(phno,chat_history)

    return bot_response