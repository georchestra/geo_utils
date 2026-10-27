"""Example: migrate thesauri from one geOrchestra platform to another."""

from geOrchestra import geOrchestra

# Source platform
username = "testadmin"
password = "testadmin"
source = geOrchestra("https://demo.georchestra.org", username, password)

# Destination platform
demo_username = "testadmin"
demo_password = "testadmin"
destination = geOrchestra(
    "https://georchestra-127-0-0-1.nip.io",
    demo_username,
    demo_password,
    verifytls=False,
)

# Copy each thesaurus from the source to the destination.
thesaurus_attributes = source.gn.list_thesaurus()
print(len(thesaurus_attributes))

for thesaurus in thesaurus_attributes:
    thesaurus_data = source.gn.get_thesaurus(thesaurus["key"])
    destination.gn.create_thesaurus_dict(thesaurus, thesaurus_data)