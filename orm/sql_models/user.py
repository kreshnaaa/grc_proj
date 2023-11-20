from sqlalchemy import Column, String, Integer, ForeignKey, func, Date, JSON, String, Boolean, Table, DateTime
# from sqlalchemy.dialects.mysql import DATETIME
# from orm.sql.models.RunHistory import RunHistory
from orm.sql_models.base import Base
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base(metadata=Base)

class User(Base):

    __tablename__ = 'User'
    __table_args__ = {'schema': 'grcshema'}

    User_Id = Column(Integer, primary_key=True)
    User_name = Column(String(100), nullable=False)
    Phone_Number = Column(String(15), nullable=False)
    Email_Id = Column(String(50), unique=True, nullable=False)
    create_date = Column(DateTime, default=func.now())
    update_date = Column(DateTime, default=func.now(), onupdate=func.now())


    # Define the table with the schema
# user_table = Table('User', Base, 
#     Column('User_Id', Integer, primary_key=True),
#     Column('User_name', String(100), nullable=False),
#     Column('Phone_Number', String(15), nullable=False),
#     Column('Email_Id', String(120), unique=True, nullable=False),
#     Column('Create_Date', Date, nullable=False),
#     Column('Update_Date', Date, nullable=False),
#     schema='grcschema'
# )