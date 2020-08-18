from dotenv import load_dotenv
from connection_helper import get_client
from operations.vertices import insert_vertices

load_dotenv()

gremlin_insert_vertices = [
    "g.addV('person').property('id', 'thomas').property('firstName', 'Thomas').property('age', 44).property('pk', 'pk')",
    "g.addV('person').property('id', 'mary').property('firstName', 'Mary').property('lastName', 'Andersen').property("
    "'age', 39).property('pk', 'pk')",
    "g.addV('person').property('id', 'ben').property('firstName', 'Ben').property('lastName', 'Miller').property('pk', 'pk')",
    "g.addV('person').property('id', 'robin').property('firstName', 'Robin').property('lastName', "
    "'Wakefield').property('pk', 'pk') "
]


insert_vertices(get_client(), gremlin_insert_vertices)

