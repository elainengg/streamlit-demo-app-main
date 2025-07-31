import streamlit as st

def sidebar_chat_manager():
    with st.sidebar:
        # Top of the Screen
        st.header("Front Office Assistant")
        st.write("### Recent Chats")
        st.write("#### Older")

        # Defaults to just having chat 1 - hard coded
        if "chats" not in st.session_state:
            st.session_state.chats = {"Chat 1": []}
            st.session_state.current_chat = "Chat 1"

        # Adding chats
        if st.button("➕ New Chat"):
            new_name = f"Chat {len(st.session_state.chats) + 1}"
            st.session_state.chats[new_name] = []
            st.session_state.current_chat = new_name

        # Radio chat names (should remove radio later)
        chat_names = list(st.session_state.chats.keys())
        selected_chat = st.radio("Select a chat:", chat_names, index=chat_names.index(st.session_state.current_chat))
        st.session_state.current_chat = selected_chat
