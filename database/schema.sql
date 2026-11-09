--O schema.sql fica responsável por criar as tabelas.


CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    usuario TEXT,
    senha TEXT
);


