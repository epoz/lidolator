# LIDOlator

A utility package in Python to convert [LIDO](https://lido-schema.org/) metadata from XML to other formats.

You can test this library by [opening the test notebook on Google Colab](https://colab.research.google.com/github/epoz/lidolator/blob/main/test_samples.ipynb) where you can load some real-world sample data.

Example:

```python
import lidolator
import urllib.request

r = urllib.request.urlopen("https://www.lido-schema.org/documents/examples/LIDO-v1.1-Example_FMobj00154983-LaPrimavera.xml")
lidodoc = lidolator.from_string(r.read())

print(lidodoc.keys())
# dict_keys(['recordInfoLink', 'image', 'description', 'classification', 'title', 'legalBody', 'relatedNote', 'actor', 'displayDate', 'earliestDate', 'latestDate', 'recordID'])
```

Also see: [LIDO Primer](https://lido-schema.org/documents/primer/latest/lido-primer.html)

Note that this simple library at the moment combines the data from the rich LIDO representation into a simpler key-value format to be used in indexing. Each key in the returned dict references a list of values, which are still XML ELementTree nodes.

At this point it is up to the consuming code to transform the nodes into other formats, depending on the application needs.

## Background information

The lidolator library is currently a "placeholder" for gathering information on the current state-of-the-art in projects that wish to convert LIDO XML files into RDF.
The author of the package (@epoz) has contacted the CIDOC LIDO Working groups, and others to try and collect information on implementations with the aim of creating a shared resource that is usable in a wider context, hopefully saving time in future efforts.

To date we have found:

- [conversions by the Yale LUX team](https://github.com/ycba-cia/reconciliation/blob/ycba_master/scripts/builder_ycba.py) to [https://linked.art/](https://linked.art/) (thanks to Eric James et al)

- [LIDO converter in the Hydra Scraper](https://github.com/digicademy/hydra-scraper/blob/main/helpers/convert.py) from Jonatan Steller

- Digicult OAI-PMH LIDO to JSONLD (links not available)

- [Ein Knowledge Graph für wissenschaftliche Sammlungen : Generierung von Linked Open Data für heterogene museale Sammlungen auf der Basis des ASCH-Modells](https://opus4.kobv.de/opus4-th-wildau/frontdoor/index/index/docId/1203)

- [Legacy Marburg Java Code](https://github.com/epoz/lido2crm_legacy)

- [Mappings](https://cidoc-crm.org/Resources/mappings-between-lido-v1.0-and-cidoc-crm-v6.0-in-x3ml-ver.1) in [x3ml](https://github.com/isl/x3ml)
