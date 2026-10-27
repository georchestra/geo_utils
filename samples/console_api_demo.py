"""Demonstrate Console reads and optional user/organization changes.

Edit SERVER, USERNAME, and PASSWORD below before running.
Pass --apply to create/delete temporary test resources, or
--update-user-description to change the configured user's description.
"""

import argparse
import json
import uuid

from geOrchestra.console import Console_api


SERVER = "https://your-georchestra.example.org"
USERNAME = "your-username"
PASSWORD = "your-password"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Create and delete temporary test user and organization resources.",
    )
    parser.add_argument(
        "--update-user-description",
        action="store_true",
        help="Update the configured user's description.",
    )
    args = parser.parse_args()

    console = Console_api(SERVER, USERNAME, PASSWORD)

    user_text = console.getusers(uid=USERNAME)
    if not user_text:
        raise SystemExit(f"Could not retrieve user {USERNAME!r}.")
    user = json.loads(user_text)
    print("User:", user.get("uid"), "Organization:", user.get("org"))

    if args.update_user_description:
        user["orgObj"] = json.loads(console.getorgs(uid=user["org"]))
        user["description"] = "Description changed by the geOrchestra sample"
        print(console.updateuserdetails(uid=user["uid"], json=json.dumps(user)))

    if args.apply:
        suffix = uuid.uuid4().hex[:8]
        test_user = f"sample{suffix}"
        test_org = f"SAMPLE{suffix.upper()}"
        print(
            console.createnewuser(
                org=user["org"],
                sn="Sample",
                givenname="User",
                mail=f"{test_user}@example.org",
                description="Temporary user created by the geOrchestra sample",
            )
        )
        print(console.deluser(id=test_user))
        print(console.createneworgs(name=test_org, shortName=test_org.lower(), orgType="Other"))
        print(console.delorgs(id=test_org.lower()))

    if not args.apply and not args.update_user_description:
        print("Read-only run. Pass a mutation flag to change Console data.")


if __name__ == "__main__":
    main()
