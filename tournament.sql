-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Automate tedious commands at the prompt

-- Disconnect active users 
SELECT pg_terminate_backend(pg_stat_activity.pid)
FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'tournament'
AND pid <> pg_backend_pid();

-- Disconnect ourselves by connecting to another database
\c vagrant
-- Remove any previously created database with same name
DROP DATABASE IF EXISTS tournament;
-- New database with 0 entries
CREATE DATABASE tournament;
-- Connect to it
\c tournament

-- Keep track of all newly registered players
CREATE TABLE players(
	name text,
	wins integer,
	matches integer,
	id serial primary key	);

-- Let's keep track of played matches
CREATE TABLE matches(
	winners INT REFERENCES players(id),
	losers INT REFERENCES players(id),
	match_id serial primary key,
	CHECK (winners <> losers) );	

	