-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE player (
	player_id serial PRIMARY KEY,
	player_name text
);

CREATE TABLE match (
	player_1 integer REFERENCES player(player_id),
	player_2 integer REFERENCES player(player_id),
	winner integer REFERENCES player(player_id)
);

CREATE VIEW wins AS
	SELECT player_id, count(winner) AS num_wins
	FROM player LEFT JOIN match ON (player_id=winner)
	GROUP BY player_id;

CREATE VIEW m1 AS
	SELECT player_id, count(player_1) AS num_matches_1
	FROM player LEFT JOIN match ON (player_id=player_1)
	GROUP BY player_id;

CREATE VIEW m2 AS
	SELECT player_id, count(player_2) AS num_matches_2
	FROM player LEFT JOIN match ON (player_id=player_2)
	GROUP BY player_id;

CREATE VIEW standings AS
	SELECT player_id, player_name, num_wins, num_matches_1 + num_matches_2 AS num_matches
	FROM player LEFT JOIN m1 using (player_id)
				LEFT JOIN m2 using (player_id)
				LEFT JOIN wins using (player_id)
	ORDER BY num_wins DESC;