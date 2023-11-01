import contextlib
from shutil import get_terminal_size


def banner(name: str, fill: str = "=", padding: int = 2) -> None:
    width = get_terminal_size().columns
    fill_len = len(fill)
    if fill_len < 1:
        raise ValueError(f"fill must be >= 1 character not {fill_len}.")
    if padding < 1:
        raise ValueError("Padding must be >= 1 spaces.")
    insert_len = len(name) + padding * 2
    pre_banner_len = width // 2 - insert_len // 2
    if pre_banner_len < 1:
        raise ValueError(
            f"Banner left-hand size width must be >= 1, not {pre_banner_len}."
        )
    post_banner_len = width - insert_len - pre_banner_len
    if post_banner_len < 1:
        raise ValueError(
            f"Banner right-hand size width must be >= 1, not {post_banner_len}."
        )
    pre_banner_num, pre_banner_rem = (
        pre_banner_len // fill_len,
        pre_banner_len % fill_len,
    )
    post_banner_num, post_banner_rem = (
        post_banner_len // fill_len,
        post_banner_len % fill_len,
    )
    print(
        fill * pre_banner_num
        + fill[:pre_banner_rem]
        + " " * padding
        + name
        + " " * padding
        + fill * post_banner_num
        + fill[:post_banner_rem]
    )


@contextlib.contextmanager
def banner_ctx(
    name: str,
    start_str: str = "START:",
    end_str: str = "END:",
    fill: str = "=",
    padding: int = 2,
) -> contextlib.AbstractContextManager:
    try:
        yield banner(start_str + " " + name, fill, padding)
    finally:
        banner(end_str + " " + name, fill, padding)
