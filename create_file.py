from construct import *
from construct.lib import *

format = Struct(
    "signature" / Const(b"BMP"),
    "width" / Int8ub,
    "height" / Int8ub,
    "pixels" / Array(this.width * this.height, Byte),
)

print(format.build(dict(width=3,height=2,pixels=[7,8,9,11,12,13])))