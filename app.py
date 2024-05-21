import streamlit as st
from utils import chatBot, text
import streamlit_chat
from streamlit_chat import message


def main():

    st.set_page_config(
        page_title='LGPDNOW GPT',
        page_icon='utils/lgpd_logo_verde.png',
        layout="centered"
    )

    # Create session state variables for conversation history and user input
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # Logo "centralizada"
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.empty()
    col2.image('utils/Logo-lgpd-com-nome.png', width=475)
    col3.empty()
    col4.empty()
    col5.empty()
    col6.empty()
    col7.empty()
    st.header(':green[Converse com um especialista em LGPD] ')

    user_question = st.text_input("Em que posso te ajudar hoje?", key="user_input")
    st.session_state.user_input = user_question  # Store user input

    # Handle conversation creation and retrieval
    try:
        if not st.session_state.conversation:
            st.session_state.conversation = chatBot.create_conversation_chain()
    except:
        st.warning("An error occurred while creating the conversation chain. Retrying...")
        st.session_state.conversation = chatBot.create_conversation_chain()

    # Process user input and update conversation history
    if user_question:
        response = st.session_state.conversation(user_question)
        #response = st.session_state.conversation.get_response(user_question)
        st.session_state.conversation.append({
            "is_user": True,
            "content": user_question
        })
        st.session_state.conversation.append({
            "is_user": False,
            "content": response["chat_output"]
        })

    # Display chat history
    for i, message_data in enumerate(st.session_state.conversation):
        if message_data["is_user"]:
            message(message_data["content"], is_user=True, key=str(i) + '_user')
        else:
            message(message_data["content"], is_user=False, key=str(i) + '_bot')
    

    with st.sidebar:

        st.subheader('Seus arquivos')

        # ------ INICIO HABILITAR O PROCESSAMENTO DE ARQUIVOS PDF ----#

        # pdf_docs = st.file_uploader(
        #     "Carregue os seus arquivos, em formato PDF, aqui", accept_multiple_files=True)
        # print(type(pdf_docs))

        # if st.button('Processar'):
        #     all_files_text = text.process_file(pdf_docs)

        #     chunks = text.create_text_chunks(all_files_text)

        #     vectorstore = chatBot.create_vectorstore(chunks)
        #     # print(vectorstore)
        #     st.session_state.conversation = chatBot.create_conversation_chain(
        #         vectorstore)

        # _____ FIM HABILITAR O PROCESSAMENTO DE ARQUIVOS PDF ____#

        st.header('Seu Chatbot pessoal treinado pela LGPDNOW! ', divider='green')
        st.write("")
        st.caption(""" <p style='text-align:justify'>
        A Lei Geral de Proteção de Dados Pessoais (LGPD) foi promulgada em 2018 com o objetivo de garantir os direitos à liberdade, privacidade e personalidade dos indivíduos. Ela se aplica a qualquer pessoa, seja física ou jurídica, incluindo empresas e órgãos públicos.
<p style='text-align:justify'>
A LGPD define regras claras para a coleta, armazenamento, uso e compartilhamento de dados pessoais. Isso significa que você tem mais controle sobre suas informações e pode saber como elas estão sendo utilizadas.
<p style='text-align:justify'>
Com a LGPD em vigor desde 2020, empresas e órgãos que não se adequarem à lei podem ser punidos com multas.
        </p>""", unsafe_allow_html=True)
        st.markdown("")

        with st.expander("Legislação utilizada no modelo: "):
            st.write("LEI No 13.709, DE 14 DE AGOSTO DE 2018")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

        # def clear_chat_history():
        #     st.session_state.conversation = None
        # st.markdown("")
        # st.sidebar.button('Limpar Chat', on_click=clear_chat_history)
        # st.divider()

        st.caption("<p style='text-align:center'> Made by LGPDNOW </p>",
                   unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.empty()
        col2.empty()
        col3.image('utils/lgpd_logo_verde.png', width=40)
        col4.empty()
        col5.empty()
        # for index, col in enumerate(st.columns(5)):
        #     if index==3:
        #         st.image('utils/download.png', width=50)
        #     else:
        #         st.empty()

        # with open("normas/lgpd.pdf", "rb") as f:
        #     pdf_bytes = f.read()

        # all_files_text = text.process_file(pdf_bytes)
        # chunks = text.create_text_chunks(all_files_text)
        # vectorstore = chatBot.create_vectorstore(chunks)
        # print(vectorstore)

        # vectorstore = "vectorstore/._index.faiss"
        st.session_state.conversation = chatBot.create_conversation_chain()


if __name__ == '__main__':

    main()
