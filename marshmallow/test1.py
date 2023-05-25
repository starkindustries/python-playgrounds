from marshmallow import Schema, fields

class Foo(Schema):
    bar = fields.List(fields.Dict(keys=fields.String(), values=fields.String()))

# Example usage
foo_schema = Foo()
data = {
    "bar": [
        {
            "key1": "value1",
            "key2": "value2",
        },
        {
            "key3": "value3",
            "key4": "value4",
        },
    ]
}

serialized_data = foo_schema.dump(data)
print(serialized_data)
