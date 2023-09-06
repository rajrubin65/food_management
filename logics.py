from datetime import datetime, timedelta
import calendar
import schedule
import pandas as pd
from datetime import datetime,timedelta
from db_opperations import FoodDetailsOpr,UserOper


def get_food_dataset(no_of_days, user_id,today):
    # today = datetime.now().date()
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
        df.to_csv('data_set.csv')
        food_detail_opr.delete_all_foods()
