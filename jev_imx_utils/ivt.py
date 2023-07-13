import dataclasses
import sys
import typing as t

from construct import (
    Adapter,
    Array,
    Byte,
    BytesInteger,
    ByteSwapped,
    Const,
    Int8ul,
    Int16ub,
    Int32ul,
    Probe,
    this,
)
from construct_typed import DataclassMixin, DataclassStruct, EnumBase, TEnum, csfield
from rich import inspect, print

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


class IVT_Header_Version(EnumBase):
    v64 = 0x40
    v65 = 0x41


@dataclasses.dataclass
class _IVT_Header(DataclassMixin):
    # probe: None = csfield(Probe(lookahead=4))
    tag: int = csfield(Const(0xD1, Int32ul))
    length: int = csfield(Const(32, Int16ub))
    version: IVT_Header_Version = csfield(TEnum(Int8ul, IVT_Header_Version))


foo = DataclassStruct(_IVT_Header)

# inspect(foo)


IVT_Header = BigEndianByteSwapped(DataclassStruct(_IVT_Header))
# IVT_Header = DataclassStruct(_IVT_Header)


@dataclasses.dataclass
class _IVT(DataclassMixin):
    header: IVT_Header = csfield(IVT_Header)
    entry: int = csfield(Int32ul)
    reserved: Int32ul = csfield(Const(0, Int32ul))
    dcd: int = csfield(Int32ul)
    boot_data: int = csfield(Int32ul)
    ivt_self: int = csfield(Int32ul)
    cfs: int = csfield(Int32ul)
    reserved2: int = csfield(Const(0, Int32ul))


IVT = DataclassStruct(_IVT)
