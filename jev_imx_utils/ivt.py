import dataclasses
import sys

from construct import (
    ByteSwapped,
    Const,
    Int8ul,
    Int16ub,
    Int32ul,
    Hex,
)
from construct_typed import DataclassMixin, DataclassStruct, TEnum, csfield

from .construct_typed_additions import EnumBase

_le_native: bool = sys.byteorder == "little"

# class BigEndianAdapter(Adapter):
#     def _decode(self, obj, context, path):
#         if not _le_native:
#             return obj

#         return self._decode()

#     def _encode(self, obj, context, path):
#         return list(map(int, obj.split(".")))


def BigEndianByteSwapped(subcon):
    if not _le_native:
        return subcon
    return ByteSwapped(subcon)


class IVT_v6_Header_Version(EnumBase):
    v64 = 0x40
    v65 = 0x41


@dataclasses.dataclass
class _IVT_v6_Header(DataclassMixin):
    # probe: None = csfield(Probe(lookahead=4))
    tag: int = csfield(Const(0xD1, Hex(Int8ul)))
    length: int = csfield(Const(32, Int16ub))
    version: IVT_v6_Header_Version = csfield(TEnum(Hex(Int8ul), IVT_v6_Header_Version))


foo = DataclassStruct(_IVT_v6_Header)

# inspect(foo)


# IVT_Header = BigEndianByteSwapped(DataclassStruct(_IVT_Header))
IVT_v6_Header = DataclassStruct(_IVT_v6_Header)


@dataclasses.dataclass
class _IVT_v6(DataclassMixin):
    header: IVT_v6_Header = csfield(IVT_v6_Header)
    entry: int = csfield(Hex(Int32ul))
    reserved: Int32ul = csfield(Const(0, Hex(Int32ul)))
    dcd: int = csfield(Hex(Int32ul))
    boot_data: int = csfield(Hex(Int32ul))
    ivt_self: int = csfield(Hex(Int32ul))
    cfs: int = csfield(Hex(Int32ul))
    reserved2: int = csfield(Const(0, Int32ul))


IVT_v6 = DataclassStruct(_IVT_v6)
