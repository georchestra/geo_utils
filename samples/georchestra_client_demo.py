"""Demonstrate the combined GeoNetwork, Console, and GeoServer client.

Edit SERVER, USERNAME, and PASSWORD below before running.
Remote harvest assignment and batch editing require explicit flags.
"""

import argparse
import json

from geOrchestra import geOrchestra


SERVER = "https://your-georchestra.example.org"
USERNAME = "your-username"
PASSWORD = "your-password"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--uuid", help="Record UUID to inspect or edit.")
    parser.add_argument(
        "--assign-harvests",
        action="store_true",
        help="Assign active filesystem harvests to the local node.",
    )
    parser.add_argument(
        "--batch-edit",
        action="store_true",
        help="Replace 'Awesome' with 'Awesome test ici' in the selected record.",
    )
    args = parser.parse_args()

    api = geOrchestra(SERVER, USERNAME, PASSWORD)
    try:
        if args.uuid:
            print(api.gn.get_metadataxml(args.uuid))

        harvests = api.gn.get_harvests()
        active_harvests = [
            harvest
            for harvest in (harvests if isinstance(harvests, list) else [])
            if harvest.get("@type") == "filesystem"
            and harvest.get("options", {}).get("status") == "active"
        ]
        print("Active filesystem harvests:", len(active_harvests))
        if args.assign_harvests:
            for harvest in active_harvests:
                harvest_uuid = harvest["site"]["uuid"]
                print(harvest_uuid, api.gn.make_harvest_local(harvest_uuid))

        if args.batch_edit:
            if not args.uuid:
                parser.error("--batch-edit requires --uuid")
            bucket = "sample-edit-bucket"
            api.gn.feed_search_bucket(bucket, args.uuid)
            print("Selection:", api.gn.get_search_bucket(bucket))
            result = api.gn.batch_edit_search_and_replace(
                bucket_name=bucket,
                search="Awesome",
                replace="Awesome test ici",
            )
            if isinstance(result, dict):
                print(json.dumps(result, indent=2))
            else:
                print(result)
            api.gn.purge_search_bucket(bucket)
    finally:
        api.gn.closesession()


if __name__ == "__main__":
    main()
