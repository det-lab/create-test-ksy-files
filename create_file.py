from construct import *
from construct.lib import *

format = Struct(
    "signature" / Const(b"BMP"),
    "width" / Int8ub,
    "height" / Int8ub,
    "pixels" / Array(this.width * this.height, Byte),
)

binary_content= format.build(dict(width=3,height=2,pixels=[7,8,9,11,12,13]))

# Open a file in binary write mode ('wb' mode)
with open('binary_file.bin', 'wb') as f:
    # Write binary content to the file
    f.write(binary_content)

print("Binary content has been written to binary_file.bin")
