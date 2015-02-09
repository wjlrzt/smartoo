from rdflib import Namespace
from rdflib.namespace import FOAF, RDFS, DC, XSD, RDF

"""
Module for RDF namespaces.
"""

RESOURCE = Namespace('http://dbpedia.org/resource/')
ONTOLOGY = Namespace('http://dbpedia.org/ontology/')
# own namespaces
SMARTOO = Namespace('http://fi.muni.cz/smartoo/')

NAMESPACES_DICT = {
    'dbpedia': RESOURCE,
    'dbpedia-owl': ONTOLOGY,
    'smartoo': SMARTOO,
    'foaf': FOAF,
    'rdf': RDF,
    'rdfs': RDFS,
    'dc': DC,
    'xsd': XSD
}
