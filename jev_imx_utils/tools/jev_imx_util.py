#!/usr/bin/env python3

import argparse
from pathlib import Path

from jev_imx_utils.firmware_image import FirmwareImage


def real_main(args):
    print(f"hi parsing {args.firmware_image_path}")
    fw_img = FirmwareImage.from_path(args.firmware_image_path, args.ivt_offset)
    print(f"fw_img: {fw_img}")


def main():
    parser = argparse.ArgumentParser(description="jev-imx-util")
    parser.add_argument(
        "-f",
        "--firmware-image",
        required=True,
        dest="firmware_image_path",
        type=Path,
        help="Raw firmware binary to parse.",
    )
    parser.add_argument(
        "-v",
        "--ivt-offset",
        default=0x1000,
        type=lambda o: int(o, 0),
        help="IVT offset (defaults to 4 KB [0x1000])",
    )
    args = parser.parse_args()
    real_main(args)


if __name__ == "__main__":
    main()
