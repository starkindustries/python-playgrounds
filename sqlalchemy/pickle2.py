from sqlalchemy import create_engine, Column, Integer, PickleType
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pickle

# create an engine to connect to a SQLite database
engine = create_engine('sqlite:///example.db', echo=True)

# create a declarative base object
Base = declarative_base()

# create a model class that uses the declarative base
class Example(Base):
    __tablename__ = 'example'

    id = Column(Integer, primary_key=True)
    data = Column(PickleType)

# create the table in the database
Base.metadata.create_all(engine)

# create a session factory to interact with the database
Session = sessionmaker(bind=engine)

# create a session
session = Session()

# create some data to insert
my_data = {'name': 'John Doe', 'age': 42}

# serialize the data using pickle
# serialized_data = pickle.dumps(my_data)

# create a new instance of the model class
# example = Example(data=serialized_data)
example = Example(data=my_data)

# add the instance to the session
session.add(example)

# commit the changes to the database
session.commit()

# query the database for the instance we just inserted
example = session.query(Example).filter_by(id=1).first()

# deserialize the data using pickle
deserialized_data = example.data # pickle.loads(example.data)

# print the data
print("my_data:", my_data)
print("example.data:", example.data)
print("deserialized_data:", deserialized_data)
print(deserialized_data['name'])
