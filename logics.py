from datetime import datetime, timedelta
import calendar
import pandas as pd
from datetime import datetime,timedelta
from db_opperations import FoodDetailsOpr,UserOper
from email_senter import send_email


def get_food_dataset(no_of_days, user_id):
    today = datetime.now().date()
    weekends = ['Sunday','Saturday']
    data_list = [
        {
            "datetime": str(today + timedelta(days=i)),
            "morning": True,
            "noon": True,
            "night": True,
            "user_id": user_id,
        }
        for i in range(no_of_days)
        if calendar.day_name[(today + timedelta(days=i)).weekday()] not in weekends
    ]
    return data_list


food_detail_opr = FoodDetailsOpr()



def handle_db_clear():
    """
    To handle the schedule based database clear and 
    send the amount details to mail
    """
    current_date = datetime.now()
    if current_date.date().day == 1:
        data_set = food_detail_opr.get_all_food_details()
        df = pd.DataFrame(data=data_set)
        df.to_csv('data.csv')
        send_email()
        food_detail_opr.delete_all_foods()



def create_data_set():
    print('hyyy')
    data_set = get_food_dataset(no_of_days=1,user_id=1)
    date_str = str(datetime.now().date())
    if len(data_set)!= 0 and not food_detail_opr.handle_ispresent(date=date_str,
        user_id=1):
        FoodDetailsOpr().add_food_details(food_details=data_set[0])


