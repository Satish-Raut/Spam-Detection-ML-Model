
import streamlit as st
import pickle 

count_vec = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("model.pkl", 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter The Message")


if st.button("Predict"):
    # 1. Vectorize

    vec_input = count_vec.transform([input_sms])
    # 2. Predict

    result = model.predict(vec_input)[0]
    # 3. Diplay

    if(result == 1):
        st.header("Spam")
    elif(result == 0):
        st.header("Not Spam")

if(input_sms == ""):
    st.header("Predicted Message type")