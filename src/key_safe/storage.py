import base64
from typing import TextIO

import pyperclip
import tomlkit

from key_safe import encryption


def create_safe_file(file: TextIO) -> None:
    safe = tomlkit.document()
    safe["Key Safe"] = {}
    tomlkit.dump(safe, file)


def store_token(file: TextIO, name: str, token: bytes) -> None:
    safe = tomlkit.load(file)
    safe["Key Safe"][name] = base64.b64encode(token).decode()
    file.seek(0)
    tomlkit.dump(safe, file)


def retrieve_token(file: TextIO, name: str, password: str) -> None:
    safe = tomlkit.load(file)
    token = base64.b64decode(safe["Key Safe"][name].encode())
    pyperclip.copy(encryption.decrypt(token, password))
