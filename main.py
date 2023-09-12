from datetime import datetime
import streamlit as st
import pandas as pd
import subprocess
import os
from db_opperations import UserOper,FoodDetailsOpr
from logics import create_data_set,handle_db_clear
from apscheduler.schedulers.background import BackgroundScheduler

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
show_details = st.checkbox('Show Details')
submit = st.button('Submit')
get_amount = st.button('Get Current Amount')


if submit:
    # get user id
    date_str = str(datetime.now().date())
    user_id = selected_option.split('-')[0]
    if not food_oper.handle_ispresent(user_id=user_id,date=date_str):
        food_oper.add_food_details(
            food_details={
                'datetime': date_str,
                'morning':morng,
                'noon': noon,
                'night': night,
                "user_id": user_id 
            }
        )
        st.info('Submited Sucessfully...!!')
    else:
        st.info("Allready Submitted")


if show_details:
    data_set = food_oper.get_all_food_details()
    data_frame = st.dataframe(data=data_set)
    df = pd.DataFrame(data=data_set)
    total_sum = df['amount'].sum()
    df['Total Amount'] = total_sum
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
    "Press to Download",
    csv,
    "food_price.csv",
    "text/csv",
    key='download-csv'
    )
    

if get_amount:
    data_set = food_oper.get_all_food_details()
    df = pd.DataFrame(data=data_set)
    total_sum = df['amount'].sum()
    st.subheader(f'Total Amount: {total_sum}')


# To run the sceduler tasks
scheduler = BackgroundScheduler()
scheduler.add_job(create_data_set, 'interval', seconds=2400)
scheduler.add_job(handle_db_clear, 'interval', seconds=2400)
scheduler.start()