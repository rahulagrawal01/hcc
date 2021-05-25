import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('priyanshuhcc1.pkl','rb'))   
dataset= pd.read_csv('Wholesale customers data.csv')
X = dataset.iloc[:,2:8].values
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
def predict_note_authentication(chanel,region,fresh1,milk1,grocery1,frozen1,detergents1,delicassen1,fresh2,milk2,grocery2,frozen2,detergents2,delicassen2,fresh3,milk3,grocery3,frozen3,detergents3,delicassen3,fresh4,milk4,grocery4,frozen4,detergents4,delicassen4,fresh5,milk5,grocery5,frozen5,detergents5,delicassen5):
  predict= model.fit_predict(sc.transform([[fresh1,milk1,grocery1,frozen1,detergents1,delicassen1],[fresh2,milk2,grocery2,frozen2,detergents2,delicassen2],[fresh3,milk3,grocery3,frozen3,detergents3,delicassen3],[fresh4,milk4,grocery4,frozen4,detergents4,delicassen4],[fresh5,milk5,grocery5,frozen5,detergents5,delicassen5]]))
  #for i in predict:
   # if predict==[0]:
   #   result0="Customer is careless"

    #if predict==[1]:
    #  result1="Customer is standard"
   # if predict==[2]:
     # result2="Customer is Target"
    #if predict==[3]:
    #  result3="Customer is careful"

    #if predict==[4]:
     # result4="Custmor is sensible"
   #result=result0+result1+result2+result3+result4
  
  return predict
def main():

    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Customer Segmenation on wholesale data ")
    
    chanel = st.selectbox(
    "Chanel",
    ("1", "2")
    )
    region = st.selectbox(
    "Region",
    ("1", "2","3")
    )
    fresh1 = st.number_input('Insert Fresh1 ',3,100000)
    milk1 = st.number_input("Insert milk1 ",55,100000)
    grocery1 = st.number_input("Insert grocery1",3,100000)
    frozen1 = st.number_input("Insert frozen1 ",25,100000)
    detergents1 = st.number_input("Insert detergents1",3,100000)
    delicassen1 = st.number_input("Insert delicaseen1",3,100000)

    fresh2 = st.number_input('Insert Fresh2 ',3,100000)
    milk2 = st.number_input("Insert milk2 ",55,100000)
    grocery2 = st.number_input("Insert grocery2 ",3,100000)
    frozen2 = st.number_input("Insert frozen2 ",25,100000)
    detergents2 = st.number_input("Insert detergents2",3,100000)
    delicassen2 = st.number_input("Insert delicaseen2",3,100000)

    fresh3 = st.number_input('Insert Fresh3 ',3,100000)
    milk3 = st.number_input("Insert milk 3",55,100000)
    grocery3 = st.number_input("Insert grocery3 ",3,100000)
    frozen3 = st.number_input("Insert frozen3 ",25,100000)
    detergents3 = st.number_input("Insert detergents3",3,100000)
    delicassen3 = st.number_input("Insert delicaseen3",3,100000)

    fresh4 = st.number_input('Insert Fresh4 ',3,100000)
    milk4 = st.number_input("Insert milk4 ",55,100000)
    grocery4 = st.number_input("Insert grocery4",3,100000)
    frozen4 = st.number_input("Insert frozen4 ",25,100000)
    detergents4 = st.number_input("Insert detergents4",3,100000)
    delicassen4 = st.number_input("Insert delicaseen4",3,100000)

    fresh5 = st.number_input('Insert Fresh5 ',3,100000)
    milk5 = st.number_input("Insert milk 5",55,100000)
    grocery5 = st.number_input("Insert grocery5",3,100000)
    frozen5 = st.number_input("Insert frozen5 ",25,100000)
    detergents5 = st.number_input("Insert detergents5",3,100000)
    delicassen5 = st.number_input("Insert delicaseen5",3,100000)

    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(chanel,region,fresh1,milk1,grocery1,frozen1,detergents1,delicassen1,fresh2,milk2,grocery2,frozen2,detergents2,delicassen2,fresh3,milk3,grocery3,frozen3,detergents3,delicassen3,fresh4,milk4,grocery4,frozen4,detergents4,delicassen4,fresh5,milk5,grocery5,frozen5,detergents5,delicassen5)
      st.success('Model has predicted {}'.format(result))
      
    if st.button("About"):
      st.subheader("Developed by Priyanshu Jain")
      st.subheader("C-Section PIET")
    html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Machine learning Experiment No. 8</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
if __name__=='__main__':
  main()
