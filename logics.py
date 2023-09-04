from datetime import datetime, timedelta
import calendar
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


def food_data_creater():
    pass



