#!/usr/bin/env python
# coding: utf-8

# In[1]:



import numpy as np
import streamlit as st
import pickle


# In[2]:


#loading the saved model
load_model=pickle.load(open('C:/Users/hi/Desktop/my_flask_app/KNN_classifier.pkl','rb'))


# In[4]:


#creating function for predection
def AQI_predict(input_data):
#     input_data=(45,0,9,2,118221,50,3.046,10000,10000,10000,10000,5,4,2012,15)
    #changing input data into numpy array
    np_array=np.asarray(input_data)
    #reshape array as we are predecting for one instance
    input_reshaped=np_array.reshape(1,-1)
    predict=load_model.predict(input_reshaped)
    return predict


# In[ ]:


def main():
    #giving title 
    st.title("AQI PREDECTION WEB APP")
    PM_SubIndex=st.text_input("PM2.5_SubIndex")
    PM_SubIndex1=st.text_input("PM10_SubIndex")
    SO_SubIndex=st.text_input("SO2_SubIndex")
    NOx_SubIndex=st.text_input("NOx_SubIndex")
    NH_SubIndex=st.text_input("NH3_SubIndex")
    CO_SubIndex=st.text_input("CO_SubIndex")
    O_SubIndex=st.text_input("O3_SubIndex")
    AQI=" "
    if st.button("AQI predection result"):
        AQI=AQI_predict([PM_SubIndex,PM_SubIndex1,SO_SubIndex,NOx_SubIndex,NH_SubIndex,CO_SubIndex,O_SubIndex])
    
    
    st.success(AQI)
    
    


# In[ ]:


if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:





# In[ ]:




