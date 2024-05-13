from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

load_dotenv()  # Isso carrega as variáveis de ambiente do arquivo .env


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.load(texts=chunks, embedding=embeddings)

    return vectorstore

def create_conversation_chain(vectorstore=None):
    if (not vectorstore):
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.load_local(
                'vectorstore', embeddings=embeddings, allow_dangerous_deserialization=True)

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7)

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain