from langchain_openai.embeddings import OpenAIEmbeddings
# from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import CTransformers

load_dotenv()  # Isso carrega as variáveis de ambiente do arquivo .env


def create_vectorstore(chunks):
    embeddings = OpenAIEmbeddings()
    new_vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    vectorstore = FAISS.load_local('vectorstore', embeddings)
    vectorstore.merge_from(new_vectorstore)
    return vectorstore


# O none aqui deixa o artributo como opcional
def create_conversation_chain(vectorstore=None):
    if (not vectorstore):
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(
            'vectorstore', embeddings, allow_dangerous_deserialization=True)

    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7)

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def create_conversation_chain_multi_model(llm_model, vectorstore=None):
    if llm_model == "Chat GPT 3.5":
        llm = ChatOpenAI(
                model="gpt-3.5-turbo-0125", 
                temperature=0.7
                )
        embeddings = OpenAIEmbeddings()
    elif llm_model == "Llama2 13B":
        llm = CTransformers(
                model = "utils/llama-2-7b-chat.ggmlv3.q8_0.bin",
                model_type="llama",
                max_new_tokens = 512,
                temperature = 0.5
                )
        embeddings = HuggingFaceEmbeddings(
                        model_name='sentence-transformers/all-MiniLM-L6-v2', 
                        model_kwargs={'device': 'cpu'}
                        )

    if (not vectorstore):
        vectorstore = FAISS.load_local(
            'vectorstore', embeddings, allow_dangerous_deserialization=True)

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain
