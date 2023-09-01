from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

db_url = 'sqlite:///database.db'

# Create the database engine
engine = create_engine(db_url)
Base = declarative_base()

# Create a session factory
Session = sessionmaker(autoflush=False,autocommit=False, bind=engine)

# user table ORM
class Users(Base):
    __tablename__ = 'user'
    user_id = Column("user_id",Integer,primary_key=True,nullable=False)
    user_name = Column("user_name",String(50))
    phone_num = Column("phone_num",Integer)


# Food details
class FoodDetails(Base):
    __tablename__ =  'food_details'
    fd_id = Column("fd_id",Integer,primary_key=True,nullable=False)
    datetime = Column("datetime",Integer)
    morning = Column("morning",Integer)
    noon = Column("noon",Integer)
    night = Column("night",Integer)


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
        users_dict = [obj.user_name for obj in users]
        return users_dict


# Food details

class FoodDetails:
    def __init__(self):
        self.db_session = Session()
    
    def add_food_details():
        return{'message':'success'}