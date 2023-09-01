from datetime import datetime
import streamlit as st
from db_opperations import UserOper,FoodDetails

user_oper = UserOper()
food_oper = FoodDetails()

# screen design
st.title("Food Management")
st.subheader(str(datetime.now().date()))
all_users = user_oper.get_all_users()
selected_option = st.selectbox('Select an option', all_users)
morng = st.checkbox('Morning')
noon = st.checkbox('Noon')
night = st.checkbox('Night')
submit = st.button('Submit')

if submit:
    st.info('Submited Sucessfully...!!')

