-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Avoid retyping sql commarnds by inserting them here
-- Create database "tournament" and connect to that database before creating tables
\c vagrant
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

-- Keep track of all newly registered players
create table players(
	name text,
	wins integer,
	matches integer,
	id serial primary key	);

-- Let's keep track of played matches
create table matches(
	winners INT REFERENCES players(id),
	losers INT REFERENCES players(id),
	match_id serial primary key,
	CHECK (winners <> losers) );	

	