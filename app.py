import streamlit as st
import pickle
import time

# Load model and vectorizer
count_vec = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

# ----- Custom CSS -----
st.markdown("""
    <style>
    .main-title {
        font-size: 40px;
        font-weight: 800;
        color: #4CAF50;
        text-align: center;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(-20px);}
        to {opacity: 1; transform: translateY(0);}
    }
    .result-card {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-top: 20px;
        font-size: 26px;
        font-weight: bold;
        animation: pop 0.6s ease-out;
    }
    @keyframes pop {
        0% {transform: scale(0.7); opacity: 0;}
        100% {transform: scale(1); opacity: 1;}
    }
    .spam {
        background-color: #ff5252;
        color: white;
    }
    .not-spam {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>📧 Email / SMS Spam Classifier 🧑‍💻</div>", unsafe_allow_html=True)
st.write("### Detect whether a message is *Spam* or *Not Spam*")

# Input box
input_sms = st.text_area("✍️ Enter your message below:", height=120)

# Prediction button
if st.button("🔍 Predict"):
    with st.spinner("Analyzing message... Please wait ⏳"):
        time.sleep(1.2)  # Animation effect

        vec_input = count_vec.transform([input_sms])
        result = model.predict(vec_input)[0]

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter a message to classify.")
    else:
        if result == 1:
            st.markdown("<div class='result-card spam'>🚫 Spam</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='result-card not-spam'>✅ Not Spam</div>", unsafe_allow_html=True)

else:
    st.info("👆 Enter a message and click **Predict** to see the result.")
