import streamlit as st

# CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(layout="wide", 
                   page_title="DCM AI Chatbot")

# Welcome block
with st.container(key="welcome-to-chatbot"):
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/b8/TD_Securities_logo.svg" width="300">
            <h2>Welcome to DCM AI Chatbot</h2>
            <p>You are responsible for any output generated by your use of this generative AI powered tool. 
            <br>This means you must validate the content it produces for you and confirm that it is permitted to be used for your purpose prior to any business use, in compliance with any legal, regulatory, attribution or other requirements.</p>
            <p>You may direct Compliance or app related questions to <b>tdsaimlhub@tdsecurities.com</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

# No messages in current session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Message container
with st.container():
    st.markdown('<div id="chat-scroll">', unsafe_allow_html=True)
    # Going through session state array
    for msg in st.session_state.messages:
        role = msg["role"]
        bubble_color = "#00742A" if role == "user" else "#3ca1ff"
        if role == "user":
            align = "right"
        else:
            align = "left"

        st.markdown(
            f"""
        <div class="chat-message" style='text-align: {align};'>
            <div class="chat-bubble" style='background: {bubble_color};'>
                {msg["content"]}
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# CSS for removing padding around form container
st.markdown(
    """
<style> 
div[data-testid="stForm"] {
    border: none !important;
    box-shadow: none !important
    background-color: transparent !important
    padding: 0 !important;
    margin: 0 !important
}
</style>
""",
    unsafe_allow_html=True,
)

# User input bar

with st.container(key="user-input-container"):

    with st.form("chat_form", clear_on_submit=True):

        # User input
        col1, col2 = st.columns([10, 1])
        with col1:
            user_input = st.text_area(
                label="", height=100, label_visibility="collapsed"
            )

        with col2:
            st.write("")
            submitted = st.form_submit_button("📨")

        MAX_CHARS = 15000
        char_count = len(user_input)
        st.markdown(
            f"<div class='char-count'>{char_count}/{MAX_CHARS}</div>",
            unsafe_allow_html=True,
        )
        if char_count > MAX_CHARS:
            st.warning("Character limit exceeded!")

        if submitted and user_input.strip():
            st.session_state.messages.append(
                {"role": "user", "content": user_input.strip()}
            )
            # Mock response  ( to later implement )
            st.session_state.messages.append(
                {"role": "assistant", "content": "This is a sample response."}
            )
            st.rerun()  # Two avoid double tapping the send button

    # Disclaimer
    disclaimer_url = "https://github.com/elainengg/streamlit-demo-app-main"
    st.write(
        "Artificial intelligence can make mistakes. Fact-check important information before using. Read our " + "[disclaimer here](%s)" % disclaimer_url)
