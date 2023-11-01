from pathlib import Path

from attrs import define, field

from .ivt import IVT_v6


@define
class FirmwareImage_v6:
    img_path: Path
    data: bytes = field(repr=lambda _: "")
    ivt: IVT_v6

    @classmethod
    def from_path(cls, img_path: Path, ivt_offset: int = 0x1000):
        if not isinstance(img_path, Path):
            img_path = Path(img_path)
        img_path = img_path.expanduser()
        data = open(img_path, "rb").read()
        ivt = IVT_v6.parse(data[ivt_offset : ivt_offset + IVT_v6.sizeof()])
        return cls(img_path, data, ivt)

    def __str__(self) -> str:
        return f"\nimg_path: {self.img_path}\nivt:\n{self.ivt}"
