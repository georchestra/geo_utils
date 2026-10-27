# geo-utils

This repository contains many tips/scripts/librairies in order to simplify administration/automation of geOrchestra plateform.

If you have any ideas to develop/which you could create a new issue here : https://github.com/georchestra/geo-utils/issues

## Python module

There is also a python module in order to script actions in geOrchestra plateform

To install the published package:
```
python -m pip install geOrchestra
```

To install directly from the repository:
```
python -m pip install git+https://github.com/georchestra/geo-utils/
```

to try it:
```
In [1]: from geOrchestra import geOrchestra
In [2]: username = "testadmin"
In [3]: password = "testadmin"
In [4]: url = "https://demo.georchestra.org/"
In [5]: geo_api = geOrchestra(url, username, password)
In [6]: geo_api.console.getroles()
Out[6]: '[{"uniqueIdentifier":[......]
In [7]: geo_api.gn.search_keyword("velo")
Out[7]: ......
```
## Dependencies 

geoserverCloud librairy https://github.com/camptocamp/python-geoservercloud

can be installed with `pip install geoservercloud`

## Documentation

The Python library documentation is built with MkDocs and Material, following the geOrchestra documentation template structure.

Install the documentation dependencies and preview the site locally:

```bash
python -m pip install -r mkdocs_requirements.txt
mkdocs serve
```

Then open http://127.0.0.1:8000/. The English documentation sources are in [`docs/`](docs/index.en.md).

## Extra useful lib

https://github.com/jdev-org/georchestra-ldap-py

https://github.com/pi-geosolutions/vrt2rdf

## Publishing

Publishing runs when a version tag starting with `v` is pushed to GitHub. The tag version must match the version in `pyproject.toml`.

Configure PyPI Trusted Publishing for this GitHub repository and the `.github/workflows/publish-pypi.yml` workflow. This uses GitHub's OIDC identity and does not require a PyPI token in GitHub secrets.
