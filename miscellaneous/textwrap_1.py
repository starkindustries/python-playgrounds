import binascii
import textwrap

def hexdump(data):
    hexdata = binascii.hexlify(data)
    myhexstring = hexdata.decode('utf-8')
    pairs = textwrap.wrap(myhexstring, 2)
    hexstr = ' '.join(pairs)

    printable = ''.join([chr(b) if 32 <= b < 127 else '.' for b in data])
    address = "00005000"
    print(f'{address}: {hexstr}  {printable}')


def hexdump2(data):
    offset = 0
    while data:
        chunk, data = data[:16], data[16:]
        hexdata = binascii.hexlify(chunk)
        hexdecoded = hexdata.decode('utf-8')
        pairs = textwrap.wrap(hexdecoded, 4)
        hexstr = ' '.join(pairs).ljust(39)

        printable = ''.join([chr(b) if 32 <= b < 127 else '.' for b in chunk])
        print('{:08x}: {}  {}'.format(offset, hexstr, printable))
        offset += 16

# Example usage
data = b'foobar0123456789owaiejfpow238998u9 wefaw 09 wea9wj3 328j 3fjowie fa0w9 wfj aw9p3fj aw93 fj'
hexdump(data)
print()
hexdump2(data)