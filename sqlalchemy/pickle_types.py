import pickle

# create some sample data to serialize
mydata = {'foo': 42, 'bar': [1, 2, 3], 'baz': {'qux': 'hello', 'quux': 'world'}}

# serialize the data using pickle
pickled_data = pickle.dumps(mydata)

# deserialize the data using pickle
unpickled_data = pickle.loads(pickled_data)

# print the original and deserialized data for comparison
print(f"Original data: {mydata}")
print(f"pickled data: {pickled_data}")
print(f"Unpickled data: {unpickled_data}")
print(f"{unpickled_data['baz']['qux']} {unpickled_data['baz']['quux']}")