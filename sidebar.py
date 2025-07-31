import streamlit as st

def sidebar_chat_manager():

    with st.sidebar:
        # Top of the Screen
        st.header("Front Office Assistant")
        st.write("### Recent Chats")

        # Defaults to just having chat 1
        if "chats" not in st.session_state:
            st.session_state.chats = {"Chat 1": []}
            st.session_state.current_chat = "Chat 1"

        # Add new chat
        if st.button("➕ New Chat"):
            new_name = f"Chat {len(st.session_state.chats) + 1}"
            st.session_state.chats[new_name] = []
            st.session_state.current_chat = new_name
        
        st.write("#### Older")

        chat_names = list(st.session_state.chats.keys())
        selected_chat = st.radio("", chat_names, index=chat_names.index(st.session_state.current_chat))

        if selected_chat != st.session_state.current_chat:
            st.session_state.current_chat = selected_chat
            st.session_state.messages = st.session_state.chats[selected_chat]
