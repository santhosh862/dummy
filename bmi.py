import streamlit as st
import google.generativeai as genai
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

# configure the api key

key_variable = os.getenv('GOGGLE_API_KEY')
genai.configure(api_key=key_variable)
# SET UP ONE PAGE

st.title('Health Assistant for Fitness')
st.header('This page will help you to get information for fitness using BMI value')
st.subheader('STREAMILT IS WORKING')

st.sidebar.subheader('Height')
height = st.sidebar.text_input('Enter the height in meters:')

st.sidebar.subheader('Weight')
weight = st.sidebar.text_input('Enter the weight in kgs:')

try:
    height = pd.to_numeric(height)
    weight = pd.to_numeric(weight)
    if height >0 and weight >0:
        bmi = weight/(height*2)
        st.sidebar.success(f'Bmi value is: {round(bmi,2)}')
    else:
        st.sidebar.write('Please enter the positive value')
except:
    st.sibebar('Please enter the positive values')       
            
input = st.text_input('Ask your question here')  

submit = st.button('Click here') 
model = genai.GenerativeModel('gemini-1.5-flash')                    
def generate_result(bmi,input):
    if input is not None:
        
        prompt = f''' You are a health assistant now so you need to results based on the fitness 
        or other health question. You can suggest some diet to the followed and also sone fitness
        exercises to the user. '''
        
        result = model.generate_content(input+prompt)
        return result.text
if submit:
    with st.spinner('Result is loading...'):
        response = generate_result(bmi,input)
        
    st.markdown(':green[Result]')
    st.write(response)            
