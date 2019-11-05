CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    artist_name TEXT NOT NULL,
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    album_title TEXT NOT NULL,
    artist_id INTEGER NOT NULL REFERENCES artist(id),
);

CREATE TABLE track (
    id INTEGER PRIMARY KEY,
    album_id INTEGER NOT NULL REFERENCES album(id),
    track_number INTEGER NOT NULL,
    track_title TEXT NOT NULL,
    track_length INTEGER NOT NULL
);