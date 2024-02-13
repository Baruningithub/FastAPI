from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


connection_string = "sqlite:///"+os.path.join(BASE_DIR,'site.db')
base=declarative_base()
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)


class user(base):
    __tablename__='users'
    id = Column(Integer,primary_key=True)
    name = Column(String(35),nullable=False)
    email = Column(String(59),unique=True)
    date_created = Column(DateTime(),default=datetime.now)    
    def __repr__(self):
        return f"<id: {self.id} Name: {self.name} email:{self.email} date_created: {self.date_created}>"
    
base.metadata.create_all(engine)

