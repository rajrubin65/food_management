from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from datetime import datetime


db_url = 'sqlite:///database.db'

# Create the database engine
engine = create_engine(db_url)
Base = declarative_base()

# Create a session factory
Session = sessionmaker(autoflush=False,autocommit=False, bind=engine)

class FoodPrice(Base):
    __tablename__ = 'food_price'
    fp_id = Column("fp_id",Integer,primary_key=True,autoincrement=True)
    fp_provider = Column("fp_provider",String(50))
    fp_morng = Column("fp_morng",Integer)
    fp_noon = Column("fp_noon",Integer)
    fp_night = Column("fp_night",Integer)
    


# user table ORM
class Users(Base):
    __tablename__ = 'user'
    user_id = Column("user_id",Integer,primary_key=True,nullable=False)
    user_name = Column("user_name",String(50))
    phone_num = Column("phone_num",Integer)
    # food_provider = Column("food_provider",Integer,ForeignKey(FoodPrice.fp_id))


# Food details
class FoodDetails(Base):
    __tablename__ =  'food_details'
    fd_id = Column("fd_id",Integer,primary_key=True,nullable=False)
    datetime = Column("datetime",Integer)
    morning = Column("morning",Integer)
    noon = Column("noon",Integer)
    night = Column("night",Integer)
    amount = Column("amount",Integer)
    user_id = Column("user_id",Integer,ForeignKey(Users.user_id))




Base.metadata.create_all(engine)


# Login User

class UserOper:
    def __init__(self):
        self.db_session = Session()
    
    def check_user(self,user):
        user = self.db_session.query(Users).filter(Users.user_name == user).first()
        if user:
            return True
        return False
    
    def create_user(self,user_obj):
        if not self.check_user(user=user_obj['user_name']):
            new_user = Users(
                user_name = user_obj.get('user_name'),
                phone_num = user_obj.get('phone_num')
            )
            self.db_session.add(new_user)
            self.db_session.commit()
            return {"message":"user created sucessfully","status":True}
        return {'message':"user already existing !!","status":False}

    def get_all_users(self):
        users = self.db_session.query(Users).all()
        users_dict = [str(obj.user_id) + "-" + obj.user_name for obj in users]
        return users_dict


# Food details

class FoodDetailsOpr:
    def __init__(self):
        self.db_session = Session()
    
    def add_food_details(self,food_details):
        try:
            amount = 0
            if food_details['morning'] : amount += 40
            if food_details['noon'] : amount += 50
            if food_details['night'] : amount += 40
            new_food_obj = FoodDetails(
                datetime = food_details['datetime'],
                morning = food_details['morning'],
                noon = food_details['noon'],
                night = food_details['night'],
                user_id = food_details['user_id'],
                amount = amount
            )
            self.db_session.add(new_food_obj)
            self.db_session.commit()
            return {'message':'success'}
        except Exception as e:
            print('Error ===>',e)

    def update_food_details(self,food_details):
        try:
            self.db_session.query(FoodDetails).filter(
                FoodDetails.datetime==food_details['datetime'] and FoodDetails.user_id == food_details['user_id']
                ).update(
                {
                    FoodDetails.morning : food_details['morning'],
                    FoodDetails.noon : food_details['noon'],
                    FoodDetails.night : food_details['night']
                }
                )
            self.db_session.commit()
            return {'message':'success'}
        except Exception as e:
            print(e)
    
    def handle_ispresent(self,user_id,date):
        user_obj = self.db_session.query(FoodDetails).filter(
            FoodDetails.user_id == user_id,FoodDetails.datetime == date
        ).first()
        if user_obj:
            return True
        else:
            return False

    def get_all_food_details(self):
        data_set_obj  = self.db_session.query(FoodDetails).all()
        data_set = []
        for data in data_set_obj:
            data_set.append(
                {
                    "fd_id":data.fd_id,
                    'datetime': data.datetime,
                    'morning' : data.morning,
                    'noon': data.noon,
                    'night': data.night,
                    'amount': data.amount
                }
            )
        return data_set

    def delete_all_foods(self):
        self.db_session.query(FoodDetails).delete()
        self.db_session.commit()
        return {'message':'success'}

class FoodPriceOpr:
    def __init__(self):
        self.db_session = Session()
    
    def get_price_based_on():
        pass



# import pandas as pd

# df = pd.read_csv(r'C:\Users\rubin\Downloads\food_price.csv')
# food_opr = FoodDetailsOpr()
# for ind in range(df.shape[0]):
#     data = df.loc[ind].to_dict()
#     del data['fd_id']
#     data['morning'] = True
#     data['noon'] = True
#     data['night'] = True
#     data['user_id'] = 1
#     food_opr.add_food_details(food_details=data)