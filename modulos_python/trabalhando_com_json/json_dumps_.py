import json
# from pprint import pprint
from typing import TypedDict

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

string_json = '''
{
    "title": "O senhor dos anéis: A sociedade do Anel",
    "original_title": "The lord of the rings: The fellowship of the ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas"],
    "budget": null
}
'''

filme: Movie = json.loads(string_json)
# pprint(filme, width=40)
# pprint(filme['title'])
# print(filme['characters'][0])
# print(filme['year'] + 10)

json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)