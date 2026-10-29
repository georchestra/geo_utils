"""Parse the same temporal extent with and without namespace declarations.

Metadata fills missing declarations from its namespace registry, adding only
used prefixes. Existing declarations are preserved. Each input needs one root.

Run from the repository root: python -m samples.metadata_namespaces_demo
"""

from geOrchestra.meta_apis import Metadata


# The registry supplies the missing gex and gml namespace URIs.
XML_WITHOUT_NAMESPACES = """<gex:temporalElement>
<gex:EX_TemporalExtent>
<gex:extent>
<gml:TimeInstant gml:id="d10661111111111111111111111111">
<gml:name>Date de d\u00e9but</gml:name>
<gml:timePosition/>
</gml:TimeInstant>
</gex:extent>
</gex:EX_TemporalExtent>
</gex:temporalElement>
"""

# These declarations are already present and take precedence over the registry.
XML_WITH_NAMESPACES = """<gex:temporalElement xmlns:gex="http://standards.iso.org/iso/19115/-3/gex/1.0" xmlns:gml="http://www.opengis.net/gml/3.2">
    <gex:EX_TemporalExtent>
        <gex:extent>
            <gml:TimeInstant gml:id="d10661111111111111111111111111">
                <gml:name>Date de d\u00e9but</gml:name>
                <gml:timePosition/>
            </gml:TimeInstant>
        </gex:extent>
    </gex:EX_TemporalExtent>
</gex:temporalElement>
"""


def main():
    for label, xml in (
        ("Missing declarations resolved:", XML_WITHOUT_NAMESPACES),
        ("Existing declarations preserved:", XML_WITH_NAMESPACES),
    ):
        print(label)
        print(Metadata(xml).to_string())


if __name__ == "__main__":
    main()