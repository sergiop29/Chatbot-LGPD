import streamlit as st
from utils import chatBot, text
from streamlit_chat import message
from streamlit_image_coordinates import streamlit_image_coordinates

def main():

    st.set_page_config(page_title='LGPDNOW GPT', page_icon=':books:', layout="centered")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.empty()
    col2.empty()
    col3.image('utils/download.png', width=95)
    col4.empty()
    col5.empty()

    # value = streamlit_image_coordinates("utils/download.png/200/300")
    # st.write(value)
    
    st.header(':violet[Converse com um especialista] 💬')
    user_question = st.text_input("Em que posso te ajudar hoje?")

    if ('conversation' not in st.session_state):
        st.session_state.conversation = None

    if (user_question):

        response = st.session_state.conversation(user_question)['chat_history']

        for i, text_message in enumerate(response):

            if (i % 2 == 0):
                message(text_message.content,
                        is_user=True, key=str(i) + '_user')

            else:
                message(text_message.content,
                        is_user=False, key=str(i) + '_bot')

    with st.sidebar:

        st.header('Seu Chatbot pessoal treinado pela Bravonix! ', divider='violet')
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

        def clear_chat_history():
            st.session_state.messages = [{"role": "assistant", "content": "Como posso te ajudar?"}]
        st.markdown("")
        st.sidebar.button('Limpar Chat', on_click=clear_chat_history)
        st.divider()

        st.caption("<p style='text-align:center'> Made by Bravonix </p>", unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.empty()
        col2.empty()
        col3.image('utils/download.png', width=50)
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

        vectorstore = "vectorstore/index.faiss"
        st.session_state.conversation = chatBot.create_conversation_chain(
            vectorstore)
        


if __name__ == '__main__':

    main()
