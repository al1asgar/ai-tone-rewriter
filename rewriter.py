import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("AI Tone Rewriter")
openai_api_key = st.sidebar.text_input("OpenAI APi key", type="password")

text = st.text_area("Enter Text to Rewrite:")
tone = st.selectbox("Tone:", ["Proffesional", "Friendly", "Consice", "Persuasive"])
creativity = st.slider("Creativity(Temperature)", 0.0, 1.0, 0.7)

def rewrite(text, tone, creativity):
    model = ChatOpenAI(temperature=creativity, api_key=openai_api_key)
    prompt = f"Rewrite the Following text in a {tone.lower()} tone. Return only the rewritten text.\n\n{text}"
    reply = model.invoke(prompt)
    return reply.content

if st.button("Rewrite"):
    if not openai_api_key.startswith("sk-"):
        st.warning("Enter API key in the sidebar first.", icon="⚠")
    else:
        st.write(rewrite(text, tone, creativity))

