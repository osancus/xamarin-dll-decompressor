import lz4.block
import sys
import struct


input_filepath = 'INPUT-FILE-PATH-HERE'
output_filepath = 'OUTPUT-FILE-PATH-HERE'
header = b'XALZ'
    
with open(input_filepath, "rb") as xalz_file:
    data = xalz_file.read()

    if data[:4] != header:
        sys.exit("XALZ header not found, try with the right file!")

    header_uncompressed_length = struct.unpack('<I', data[8:12])[0]
    payload = data[12:]
    
    decompressed = lz4.block.decompress(payload, uncompressed_size=header_uncompressed_length)
            
    with open(output_filepath, "wb") as output_file:
        output_file.write(decompressed)
        output_file.close()
    print("Decompressed file written successfully")
