from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Connect to the database (or create it if it doesn't exist)
engine = create_engine('sqlite:///example2.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define a table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)

# Create the table
Base.metadata.create_all(engine)

# Insert some data
session = Session()
session.add_all([User(name='Alice', age=25), User(name='Bob', age=30)])
session.commit()

# Retrieve data
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

# Close the session
session.close()
