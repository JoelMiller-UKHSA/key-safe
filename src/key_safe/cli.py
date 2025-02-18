import argparse
import getpass
import os
from key_safe import constants, encryption, storage


def store(args: argparse.Namespace) -> None:
    token = getpass.getpass("Enter secret to store: ")
    password = getpass.getpass("Enter encryption password: ")

    if not os.path.exists(constants.SAFE_FILE):
        with open(constants.SAFE_FILE, "w") as f:
            storage.create_safe_file(f)
        os.chmod(constants.SAFE_FILE, 0o600)

    with open(constants.SAFE_FILE, "r+") as f:
        storage.store_token(f, args.name, encryption.encrypt(token, password))
    del token
    del password


def retrieve(args: argparse.Namespace) -> None:
    password = getpass.getpass(f"Enter encryption password for {args.name}: ")

    with open(constants.SAFE_FILE, "r") as f:
        storage.retrieve_token(f, args.name, password)
    del password
    print(f"{args.name} was copied to the clipboard")
