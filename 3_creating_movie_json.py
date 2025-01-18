import json

movie = {
    "title": "Hangover",
    "director": "Todd Phillips",
    "actors": ["Bradley Cooper", "Zach Galifianakis", "Ed Helms", "Heather Graham", "Sasha Barrese"],
    "release_year": 2019
}

with open("3_movie.json", "w", encoding="utf-8") as file:
    json.dump(movie, file, ensure_ascii=False, indent=4, sort_keys=True)
