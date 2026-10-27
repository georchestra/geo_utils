## [GeoNetwork: `GN_API`](https://github.com/georchestra/geo-utils/blob/main/geOrchestra/meta_apis/gn_api.py#L18)

Create the client directly to configure GeoNetwork-specific options:

```python
from geOrchestra.meta_apis import GN_API

server = "https://demo.georchestra.org"
username = "testadmin"
password = "testadmin"

gn = GN_API(
    server,
    username,
    password,
    verifytls=True,
    prefix_gn_url="/geonetwork",
    xsrf_via_get=False,
)
```

TLS certificate verification is enabled by default. `xsrf_via_get=True` uses `/srv/api/me`; the default uses the legacy `/srv/fre/info?type=me` endpoint to establish the XSRF cookie.

### Examples

The following examples come from the `__main__` blocks and comments in the sources.

#### Add a thesaurus keyword to a metadata file and upload it

```python
from geOrchestra.meta_apis import GN_API, Meta_manipulation

gn = GN_API("https://demo.georchestra.org", "testadmin", "testadmin", verifytls=False)

with open("sample_meta.xml") as f:
    metadata = f.read()

metadata = Meta_manipulation.add_thesaurus(
    metadata,
    title="Category",
    server="https://demo.georchestra.org",
    thesaurus_value="test1",
    local_thesaurus_name="exemple",
)

gn.upload_metadata(metadata=metadata, uuidprocessing="OVERWRITE", publish=True)

for thesaurus in gn.list_thesaurus():
    print("Key name:", thesaurus["key"])

gn.closesession()
```

#### List active filesystem harvests

```python
all_harvests = geOr_api.gn.get_harvests()
filesystem = [h for h in all_harvests if h["@type"] == "filesystem"]
active = [h for h in filesystem if h["options"]["status"] == "active"]
```

#### Back up a record and keep its sharing settings

```python
uuid = "4b5f8e1b-de37-47cd-9203-37a59f318b09"

zip_bytes = geOr_api.gn.get_metadata_mef_zip(uuid, with_related=True)
if zip_bytes:
    with open(f"{uuid}.zip", "wb") as f:
        f.write(zip_bytes)

# groupOwner and isPublishedToAll, to resubmit with an OVERWRITE upload
privileges = geOr_api.gn.get_record_privileges(uuid)
```

#### Batch edit records from a search selection

Create and feed a selection first, check its content, then apply the change:

```python
results = geOr_api.gn.search_keyword("Mayotte")
uuids = [hit["_source"]["uuid"] for hit in results["hits"]["hits"]]

geOr_api.gn.feed_search_bucket("geoutilsbucket", uuids)
print(geOr_api.gn.get_search_bucket("geoutilsbucket"))

geOr_api.gn.batch_edit_search_and_replace(
    "geoutilsbucket", search="old text", replace="new text", regex_flags="i"
)

geOr_api.gn.purge_search_bucket("geoutilsbucket")
```


### [Catalog and metadata](https://github.com/georchestra/geo-utils/blob/main/geOrchestra/meta_apis/gn_api.py#L40)

| Method | Purpose | Result notes |
| --- | --- | --- |
| `get_gnversion()` | Read GeoNetwork site details and node ID | Parsed JSON object |
| `get_all_catalog(steps=100, portal=None)` | Collect catalog record UUIDs using CSW paging | List of UUIDs, or `None` if no records/request failure |
| `get_metadataxml(uuid)` | Read a record XML document | XML text on HTTP 200; otherwise `None` |
| `get_metadata_mef_zip(uuid, with_related=True, timeout=120)` | Download a MEF ZIP export | ZIP bytes on HTTP 200; otherwise `None` |
| `upload_metadata(metadata, groupid="100", uuidprocessing="GENERATEUUID", publish=False)` | Upload a metadata file-like object; `uuidprocessing` supports the GeoNetwork values `NOTHING`, `OVERWRITE`, and `GENERATEUUID` | Parsed JSON on success; `False` for handled failures |
| `get_record_privileges(uuid)` | Read owner group and public visibility | Dictionary on success; otherwise `None` |



### [Thesaurus](https://github.com/georchestra/geo-utils/blob/main/geOrchestra/meta_apis/gn_api.py#L244)

| Method | Purpose |
| --- | --- |
| `list_thesaurus(thesaurus_key=None)` | List thesauri, or return one matching thesaurus by key; returns `None` if the request fails or the key is not found |
| `get_thesaurus(thesaurus_key)` | Retrieve one thesaurus as RDF/XML text; returns `None` if the request fails |
| `searchin_thesaurus_dict(keyword="", thesaurus_key=False)` | Search vocabulary terms across all thesauri or restrict the search to one or more keys; returns parsed JSON on HTTP 200, otherwise `None` |
| `add_thesaurus_keyword(thesaurus_ref, ref_type, namespace, label, definition, keyword_uri=None, language="fre")` | Add a localized keyword to an existing thesaurus; generates a UUID-based concept URI if omitted and returns `(True, response_text)` on HTTP 200/201 |
| `create_thesaurus_dict(info_thesaurus_json, rdf_content)` | Upload an RDF thesaurus. `info_thesaurus_json` requires `filename`, `type`, and `dname`; returns `(True, response_text)` on HTTP 200/201 or `(False, response_text)` otherwise. |
| `create_thesaurus(thesaurus_info)` | Create thesaurus metadata from a JSON payload using GeoNetwork's PUT endpoint; returns `(True, response_text)` on HTTP 200/201 or `(False, response_text)` otherwise. |
| `delete_thesaurus(thesaurus_key)` | Delete a thesaurus by key; returns `(True, response_text)` on HTTP 200/204 or `(False, response_text)` otherwise. |

Example upload:

```python
info = {"filename": "example.rdf", "type": "local", "dname": "theme"}
with open("example.rdf", "rb") as rdf_file:
    result = gn.create_thesaurus_dict(info, rdf_file.read())

if result[0]:
    print(result[1])
else:
    print("Thesaurus upload failed:", result[1])
```

Create a thesaurus entry using its metadata:

```python
thesaurus_info = {
    "title": "",
    "description": "",
    "filename": "test",
    "defaultNamespace": "https://registry.geonetwork-opensource.org/theme/test",
    "dname": "theme",
    "type": "local",
    "multilingualTitles": {"fr": "test"},
    "multilingualDescriptions": {"fr": "test"},
}
result = gn.create_thesaurus(thesaurus_info)
print(result)
```

Add a French keyword to an existing local thesaurus. If `keyword_uri` is omitted, the method creates a unique URI under the namespace:

```python
result = gn.add_thesaurus_keyword(
    thesaurus_ref="local.theme.test",
    ref_type="theme",
    namespace="https://registry.geonetwork-opensource.org/theme/test",
    label="test123",
    definition="test123",
    language="fre",
)
print(result)
```

### [Harvests](https://github.com/georchestra/geo-utils/blob/main/geOrchestra/meta_apis/gn_api.py#L369)

| Method | Purpose | Result notes |
| --- | --- | --- |
| `get_harvests()` | List harvest configurations | Parsed JSON on success; `"Error"` otherwise |
| `make_harvest_local(uuid)` | Assign a harvest to the local GeoNetwork node | `"Okay"` or `False`; request timeout is up to one hour |
| `delete_harvest(id)` | Remove a harvest configuration | Parsed JSON response |


### [Search selections and batch editing](https://github.com/georchestra/geo-utils/blob/main/geOrchestra/meta_apis/gn_api.py#L440)

| Method | Purpose |
| --- | --- |
| `search_keyword(keywords)` | Search records using the configured GeoNetwork query |
| `get_search_buckets()` | List saved search selections |
| `get_search_bucket(name)` | Read a selection by name |
| `feed_search_bucket(name, uuid)` | Add one or more record UUIDs to a selection |
| `purge_search_bucket(name, uuid=None)` | Remove selected UUIDs, or delete/clear the selection when UUIDs are omitted |
| `batch_edit_search_and_replace(bucket_name, search, replace, regex_flags="", use_regex="false", update_date_stamp="false")` | Search and replace metadata values for records in a selection |
| `batch_edit_xpath(bucket_name, xpath, value, update_timestamps=False, action="replace", condition="")` | Apply an XPath-based batch edit to records in a selection |

Batch edit methods operate on records in a search bucket. Review the bucket contents before applying changes. Response JSON is returned without a common error wrapper.

Call `closesession()` when finished with a standalone `GN_API` client to close its requests session.