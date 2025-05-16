import streamlit as st

st.set_page_config(page_title="LangGarph Agent UI",layout="wide")
st.title("AI Chatbot Agents")
st.write("Create and interact with AI Agents")
system_prompt = st.text_area("Define your AI Agent:",height=70,placeholder="Type your system prompt here...")

MODEL_NAME_GROQ=["llama-3.3-70b-versatile"]
MODEL_NAME_OPENAI=["gpt-4o-mini"]

provider=st.radio("Select provider:",("Groq","OpenAI"))

if provider=="Groq":
    selected_model=st.selectbox("Select Groq model:",MODEL_NAME_GROQ)
elif provider=="OpenAI":
    selected_model=st.selectbox("Select OpenAI model:",MODEL_NAME_OPENAI)

allow_web_search =  st.checkbox("Allow web search")
query=st.text_area("Enter your query",height=150,placeholder="Ask anything")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent:"):
    if query.strip():
        import requests
        payload={
            "model_name":selected_model,
            "model_provider":provider,
            "system_prompt":system_prompt,
            "messages":[query],
            "allow_search":allow_web_search
        }

        response=requests.post(API_URL,json=payload)
        if response.status_code==200:
            response_data=response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent response")
                st.markdown(f"final response:{response_data}")
            

