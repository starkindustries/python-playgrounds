import hashlib
import string
import os
# import whirlpool

# constants
MD5 = "md5"
SHA1 = "sha1"
SHA256 = "sha256"
SHA3_256 = "sha3_256"
BLAKE2B = "blake2b"
# WHIRLPOOL = "whirlpool"

def hash_this_string(s, hashtype):
    if hashtype == MD5:
        return hashlib.md5(s.encode()).hexdigest()
    if hashtype == SHA1:
        return hashlib.sha1(s.encode()).hexdigest()
    if hashtype == SHA256:
        return hashlib.sha256(s.encode()).hexdigest()
    if hashtype == SHA3_256:
        return hashlib.sha3_256(s.encode()).hexdigest()
    if hashtype == BLAKE2B:
        return hashlib.blake2b(s.encode()).hexdigest()
    # if hashtype == WHIRLPOOL:
    #     return whirlpool.new(s.encode()).hexdigest()
    


def solve(inputfile, outputfile, hashtype, delete_firstline=False):
    if os.path.isfile(outputfile) and os.path.getsize(outputfile) > 0:
        print(f"WARNING: File [{outputfile}] exists and is not empty.. ")
        return

    # Open the file and read the hashes into a list
    with open(inputfile, 'r') as f:
        hash_strings = f.read().splitlines()

    if delete_firstline:
        print(f"Deleting first line of file: {hash_strings.pop(0)}")

    current_string = ""
    for hash in hash_strings:
        # first check if the current_string (or an empty empty string) matches the hash
        if hash == hash_this_string(current_string, hashtype):
            continue

        found_match = False
        for character in string.printable:
            temp_string = current_string + character
            if hash == hash_this_string(temp_string, hashtype):
                current_string += character
                found_match = True
                break
        if not found_match:
            print(f"ERROR: match not found for hash: {hash}")
            break

    print(current_string)
    if current_string:
        with open(outputfile, 'w') as f:
            f.write(current_string)


def solve_all():
    solve("puzzle.txt", "output.txt", MD5)
    solve("output.txt", "output2.txt", SHA1, True)

    hashtypes = [SHA256, SHA3_256, BLAKE2B]
    for type in hashtypes:
        solve("output2.txt", "output3.txt", type, True)

    print("solve completed")


# Profile program
profiling_output = 'profiling_output'

if os.path.isfile(profiling_output) and os.path.getsize(profiling_output) > 0:
    print(f"WARNING: File [{profiling_output}] exists and is not empty.. ")
else:
    import cProfile
    cProfile.run('solve_all()', profiling_output)

import pstats
p = pstats.Stats(profiling_output)
p.sort_stats('cumulative').print_stats()  # print top 10 functions ordered by cumulative time