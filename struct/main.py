import struct

# Define the format string for the struct

fmt = "ii64s"

# Pack the values into a binary string
packed_data = struct.pack(fmt, 1, 2, b"binary_data")
print("packed:", packed_data)

# Unpack the binary string back into values
unpacked_data = struct.unpack(fmt, packed_data)

# Extract the values and store them in variables
foo, bar, binary_string = unpacked_data

print(f"foo: {foo}, bar: {bar}, binary_string: {binary_string}")