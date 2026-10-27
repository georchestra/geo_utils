"""Add a GeoNetwork thesaurus keyword to an ISO 19115-3 metadata file.

Edit SERVER, USERNAME, and PASSWORD below before running.
"""

import argparse

from geOrchestra.meta_apis import GN_API, Metadata, ThesaurusKeyword


SERVER = "https://your-georchestra.example.org"
USERNAME = "your-username"
PASSWORD = "your-password"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("metadata_file")
    parser.add_argument("--output", default="sample_meta3.xml")
    parser.add_argument("--thesaurus-key", default="local.theme.geographie-ofb")
    parser.add_argument("--keyword", default="Mayotte")
    args = parser.parse_args()

    api = GN_API(SERVER, USERNAME, PASSWORD)
    try:
        thesaurus = api.list_thesaurus(args.thesaurus_key)
        results = api.searchin_thesaurus_dict(
            keyword=args.keyword,
            thesaurus_key=args.thesaurus_key,
        )
        if not thesaurus or not results:
            raise SystemExit("The thesaurus or keyword could not be found.")

        metadata = Metadata()
        metadata.load_from_file(args.metadata_file)
        keyword = results[0]
        helper = ThesaurusKeyword()
        helper.load_from_json_get_thesaurus_dict(thesaurus)
        helper.load_from_json_search_thesaurus_dict(keyword)
        metadata.add_thesaurus_to_metadata(helper)
        metadata.save_into_file(args.output)
        print("Updated metadata written to:", args.output)
    finally:
        api.closesession()


if __name__ == "__main__":
    main()
