# app_streamlit.py (Version 3.0 - With Debugging & Better Logic)

import streamlit as st
from chatguard import ChatGuard

# A simple function to simulate a chatbot's response
def get_bot_response(message):
    message = message.lower()
    if "hello" in message or "hi" in message:
        return "Hello there! How can I help you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif "price" in message or "buy" in message:
        return "Our prices start at $10. You can find more details on our website."
    else:
        return "I'm not sure how to answer that. Can you try asking another way?"

# --- Streamlit App ---

st.set_page_config(page_title="ChatGuard Demo", page_icon="🛡️")
st.title("🛡️ ChatGuard: AI Scam Detection")
st.write(
    "This is a demo of an AI-powered chatbot with real-time scam detection. "
    "Type a message below and the ChatGuard engine will analyze it for risks."
)

@st.cache_resource
def load_guard():
    guard = ChatGuard(model_path='chatguard_model.pkl')
    if not guard.model:
        st.error("Model 'chatguard_model.pkl' not found. Please run train_model.py first.")
        return None
    return guard

guard = load_guard()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    if guard:
        analysis = guard.analyze_message(prompt)

        # --- NEW & IMPORTANT: Display the model's raw output for debugging ---
        st.info(f"**Model Analysis:** `{analysis}`", icon="🔬")

        # --- IMPROVED LOGIC: Use the risk score directly with a threshold ---
        # Instead of trusting the binary 'is_scam', let's use a confidence threshold.
        # A score > 0.5 (50%) is a good starting point for a flag.
        if analysis['risk_score'] > 0.5:
            risk_score_percent = f"{analysis['risk_score']:.2%}"
            alert_message = (
                f"**🚨 CHATGUARD ALERT 🚨**\n\n"
                f"*This message has been flagged as a potential scam with a risk score of **{risk_score_percent}**.*\n\n"
                "**Action:** The bot will not process this request."
            )
            st.session_state.messages.append({"role": "assistant", "content": alert_message})
            with st.chat_message("assistant", avatar="🛡️"):
                 st.warning(alert_message, icon="⚠️")
        else:
            # If safe, get the normal bot response
            bot_reply = get_bot_response(prompt)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            with st.chat_message("assistant"):
                st.markdown(bot_reply)