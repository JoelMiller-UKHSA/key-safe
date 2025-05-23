from io import StringIO
from textwrap import dedent

import pyperclip

from key_safe import storage


def test_create_safe_file() -> None:
    mock_file = StringIO()
    storage.create_safe_file(mock_file)
    assert mock_file.getvalue() == '["Key Safe"]\n'


def test_store_token() -> None:
    mock_file = StringIO('["Key Safe"]\n')
    test_token = b"token"
    test_name = "test"
    storage.store_token(mock_file, test_name, test_token)
    assert (
        mock_file.getvalue()
        == dedent(
            """
        ["Key Safe"]
        test = "dG9rZW4="
        """
        ).removeprefix("\n")
    )


def test_retrieve_token(monkeypatch) -> None:
    monkeypatch.setattr("key_safe.encryption.decrypt", lambda x, _: f"{x.decode()}_decrypted")
    mock_file = StringIO(
        dedent(
            """
        ["Key Safe"]
        test = "dG9rZW4="
        """
        )
    )
    storage.retrieve_token(mock_file, "test", "mock_password")

    assert pyperclip.paste() == "token_decrypted"


def test_list_token_names() -> None:
    mock_file = StringIO(
        dedent(
            """
        ["Key Safe"]
        test1 = "dG9rZW4="
        test2 = "dG9rZW4="
        """
        )
    )
    names = storage.list_token_names(mock_file)

    assert names == ["test1", "test2"]
