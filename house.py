import streamlit as st 
import pandas as pd 
import joblib

st.title("House price prediction website")
model=joblib.load("house_model.joblib")
df=pd.read_csv("pune.csv")
st.subheader("Enter the details of the house:")
col1,col2=st.columns(2)

with col1:
    area=st.selectbox("Select area:",df['area'].unique().tolist())
    square_feet = st.number_input("Size of the House (in sqft):",min_value=100, max_value=10000, value=1500)
    num_bedrooms = st.number_input("Number of Bedrooms:",min_value=1, max_value=10, value=3)
    
with col2:
    num_bathrooms = st.number_input("Number of Bathrooms:",min_value=1, max_value=10, value=2)
    year_built= st.number_input("Age of the House (in years):",min_value=0, max_value=100, value=10)
    has_garage = st.selectbox("Does the house have a garage?", ["Yes", "No"])
    has_garage = 1 if has_garage == "Yes" else 0

input_data=pd.DataFrame({
    'area':[area],
    'square_feet':[square_feet],
    'num_bedrooms':[num_bedrooms],
    'num_bathrooms':[num_bathrooms],
    'year_built':[year_built],
    'has_garage':[has_garage]
})
col1, col2, col3 = st.columns([4,4,2])  # middle column is wider
with col2:
    if st.button("Predict Price"):
        prediction=model.predict(input_data)
        st.success(f"The predicted price is: ₹{prediction[0]:,.2f}")   
    

