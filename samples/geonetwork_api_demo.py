"""Demonstrate direct GeoNetwork API calls.

Edit SERVER, USERNAME, and PASSWORD below before running.
Uploading a thesaurus or overwriting metadata is opt-in via command-line args.
"""

import argparse
import os

from geOrchestra.meta_apis import GN_API, Meta_manipulation


SERVER = "https://your-georchestra.example.org"
USERNAME = "your-username"
PASSWORD = "your-password"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--thesaurus-file", help="RDF file to upload as a thesaurus.")
    parser.add_argument("--thesaurus-type", default="local")
    parser.add_argument("--thesaurus-directory", default="theme")
    parser.add_argument(
        "--overwrite-metadata",
        metavar="XML_FILE",
        help="Upload this metadata XML using UUID processing OVERWRITE.",
    )
    parser.add_argument(
        "--thesaurus-name",
        default="exemple",
        help="Local thesaurus name used when adding its keyword to metadata.",
    )
    args = parser.parse_args()

    api = GN_API(SERVER, USERNAME, PASSWORD)
    try:
        print("GeoNetwork:", api.get_gnversion())
        for thesaurus in api.list_thesaurus() or []:
            print("Thesaurus key:", thesaurus["key"])

        if args.thesaurus_file:
            filename = os.path.basename(args.thesaurus_file)
            with open(args.thesaurus_file, "rb") as rdf_file:
                result = api.create_thesaurus_dict(
                    {
                        "filename": filename,
                        "type": args.thesaurus_type,
                        "dname": args.thesaurus_directory,
                    },
                    rdf_file.read(),
                )
            print("Thesaurus upload:", result)

        if args.overwrite_metadata:
            with open(args.overwrite_metadata, encoding="utf-8") as metadata_file:
                metadata = metadata_file.read()
            metadata = Meta_manipulation.add_thesaurus(
                metadata,
                title="Category",
                server=SERVER,
                thesaurus_value="test1",
                local_thesaurus_name=args.thesaurus_name,
            )
            print(
                api.upload_metadata(
                    metadata=metadata,
                    uuidprocessing="OVERWRITE",
                    publish=True,
                )
            )
    finally:
        api.closesession()


if __name__ == "__main__":
    main()
