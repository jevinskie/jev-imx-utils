from pathlib import Path

from attrs import define, field

from .ivt import IVT


@define
class FirmwareImage:
    img_path: Path
    data: bytes = field(repr=lambda _: "")
    ivt: IVT

    @classmethod
    def from_path(cls, img_path: Path, ivt_offset: int = 0x1000):
        data = open(img_path, "rb").read()
        ivt = IVT.parse(data[ivt_offset : ivt_offset + IVT.sizeof()])
        return cls(img_path, data, ivt)
