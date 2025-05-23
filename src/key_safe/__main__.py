import argparse

from key_safe.cli import store, retrieve, list_keys


def main() -> None:
    parser = argparse.ArgumentParser(prog="key-safe")

    subparser = parser.add_subparsers(dest="command")

    store_parser = subparser.add_parser(name="store", help="Store a new secret.")
    store_parser.add_argument("name", help="Name of the secret to store.")

    retrieve_parser = subparser.add_parser(
        name="retrieve", help="Retreive a stored secret."
    )
    retrieve_parser.add_argument("name", help="Name of the secret to retrieve.")

    list_parser = subparser.add_parser(name="list", help="List the names of currently stored secrets.")

    args = parser.parse_args()
    match args.command:
        case "store":
            store(args)
        case "retrieve":
            retrieve(args)
        case "list":
            list_keys(args)
        case _:
            raise NotImplementedError


if __name__ == "__main__":
    main()
