# Runnable samples

The examples below are also available as scripts in the [samples directory](https://github.com/georchestra/geo_utils/tree/main/samples). Run them from the repository root or after installing the package. They require a reachable geOrchestra instance and an account permitted to use the requested services.

Each script defines editable `SERVER`, `USERNAME`, and `PASSWORD` constants near the top. Replace the placeholder values with your instance URL and account before running; the metadata-string helper only needs `SERVER`.

## Library examples

- [Console API](https://github.com/georchestra/geo_utils/blob/main/samples/console_api_demo.py): reads the configured user by default. `--apply` creates and deletes temporary test resources. `--update-user-description` changes the configured user's description.

```bash
python samples/console_api_demo.py
python samples/console_api_demo.py --apply
```

- [Combined client](https://github.com/georchestra/geo_utils/blob/main/samples/georchestra_client_demo.py): lists active filesystem harvests and optionally reads a record with `--uuid UUID`. `--assign-harvests` changes harvest assignments. `--batch-edit` edits the selected record and must be used with `--uuid`.

```bash
python samples/georchestra_client_demo.py --uuid UUID
python samples/georchestra_client_demo.py --uuid UUID --batch-edit
```

- [GeoNetwork API](https://github.com/georchestra/geo_utils/blob/main/samples/geonetwork_api_demo.py): reads site and thesaurus information by default. `--thesaurus-file FILE` uploads a thesaurus; `--overwrite-metadata FILE` overwrites and publishes a record.

```bash
python samples/geonetwork_api_demo.py
python samples/geonetwork_api_demo.py --thesaurus-file vocabulary.rdf
```

- [Metadata thesaurus helper](https://github.com/georchestra/geo_utils/blob/main/samples/metadata_thesaurus_demo.py): adds a selected GeoNetwork keyword to an input metadata file and writes to `sample_meta3.xml` by default. Use `--output FILE` to choose another destination.

```bash
python samples/metadata_thesaurus_demo.py metadata.xml --output updated.xml
```

- [Metadata string helper](https://github.com/georchestra/geo_utils/blob/main/samples/meta_manipulation_demo.py): adds a legacy ISO 19139 thesaurus element and writes to `<input>.new` by default.

```bash
python samples/meta_manipulation_demo.py metadata.xml
```

- [Duplicate resource identifiers](https://github.com/georchestra/geo_utils/blob/main/samples/detection_duplicate_id_ressource.py): existing sample for detecting duplicate resource identifiers.

Remote changes are deliberately opt-in. Review the sample and target instance before using mutation flags, especially `--update-user-description`, `--assign-harvests`, `--batch-edit`, `--thesaurus-file`, and `--overwrite-metadata`.

## Other command-line tools

These files are standalone utilities, not library demos; their `main()` entry points remain in place:

- [LDAP LDIF creator](https://github.com/georchestra/geo_utils/blob/main/ldap/creatorldif.py), with usage notes in the [LDAP README](https://github.com/georchestra/geo_utils/blob/main/ldap/README.md).
- [Proxy link generator](https://github.com/georchestra/geo_utils/blob/main/proxy/proxy_links.py), with usage notes in the [proxy README](https://github.com/georchestra/geo_utils/blob/main/proxy/README.md).
