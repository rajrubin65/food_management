from datetime import datetime
import streamlit as st
from db_opperations import UserOper,FoodDetailsOpr

user_oper = UserOper()
food_oper = FoodDetailsOpr()

# screen design
st.title("Food Management")
st.subheader(str(datetime.now().date()))
all_users = user_oper.get_all_users()
selected_option = st.selectbox('Select an option', all_users)
morng = st.checkbox('Morning',value=True)
noon = st.checkbox('Noon',value=True)
night = st.checkbox('Night',value=True)
submit = st.button('Submit')

if submit:
    # get user id
    user_id = 1
    food_oper.update_food_details(
        food_details={
            'datetime': str(datetime.now().date()),
            'morning':morng,
            'noon': noon,
            'night': night
        }
    )
    st.info('Submited Sucessfully...!!')

