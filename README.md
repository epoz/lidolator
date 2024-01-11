# LIDOlator

A utility package in Python to convert [LIDO](https://lido-schema.org/) metadata from XML to other formats.

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

Note that this simple library at the moment combines the data froim the rich LIDO representation into a simpler key-value format to be used in indexing. Each key in the returned dict references a list of values, which are still XML ELementTree nodes.

At this point it is up to the consuming code to transform the nodes into other formats, depending on the application needs.
