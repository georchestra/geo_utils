"""Add a legacy ISO 19139 thesaurus element to a metadata XML file.

Edit SERVER below before running. The original file is left unchanged; the
result is written to the path passed with --output or to <input>.new.
"""

import argparse

from geOrchestra.meta_apis import Meta_manipulation

SERVER = "https://your-georchestra.example.org"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata_file")
    parser.add_argument("--output")
    parser.add_argument("--title", default="DonnéeType")
    parser.add_argument("--keyword", default="Test")
    parser.add_argument("--thesaurus-name", default="type_test")
    args = parser.parse_args()

    with open(args.metadata_file, encoding="utf-8") as metadata_file:
        metadata = metadata_file.read()
    updated = Meta_manipulation.add_thesaurus(
        metadata=metadata,
        title=args.title,
        server=SERVER,
        thesaurus_value=args.keyword,
        local_thesaurus_name=args.thesaurus_name,
    )
    output = args.output or f"{args.metadata_file}.new"
    with open(output, "w", encoding="utf-8") as output_file:
        output_file.write(updated)
    print("Updated metadata written to:", output)


if __name__ == "__main__":
    main()
