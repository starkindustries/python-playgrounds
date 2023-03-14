import argparse

# Define the parser
parser = argparse.ArgumentParser(description='Example command-line argument parser')
parser.add_argument('-f', '--fooo', type=str, help='A string argument')
parser.add_argument('-b', '--barr', type=int, help='An integer argument')
parser.add_argument('-z', '--bazz', type=argparse.FileType('r'), help='A file path argument')

# Parse the arguments
args = parser.parse_args()

# Access the values of the parsed arguments
foo_value = args.fooo
bar_value = args.barr

# Note that to get the file path, we need to access the 'name' attribute of the file object
baz_value = args.bazz.name 

# Do something with the parsed arguments
print('foo:', foo_value)
print('bar:', bar_value)
print('baz:', baz_value)

print(args)