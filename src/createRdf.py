from rdflib import Graph, plugin
from rdflib.serializer import Serializer

g = Graph()

path = "../data/dump.json"
opath = path + ".rdf"

try:
    g.parse(path, format='json-ld')
except:
    pass

print(g.serialize(destination=opath))
