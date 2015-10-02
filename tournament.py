#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database. Returns a database connection."""

    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    sql_query = "SELECT count(name) AS num FROM players"
    c.execute(sql_query)
    players = c.fetchone()[0]
    DB.close()
    return players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    # Register new player and return his/her id
    player = "INSERT INTO players (name, matches, wins) VALUES (%s,%s,%s) RETURNING id"
    # All newly registered players must appear in score card
    #standings = "INSERT INTO scorecard (player_id, player_name, wins, matches) \
    #             VALUES (%s,%s,%s,%s)"
    c.execute(player, (name,0,0))
    playerid = c.fetchone()[0]
    #c.execute(standings, (playerid, name, 0, 0))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    standings = []  # list for storing player standings

    DB = connect()
    c = DB.cursor()
    players = "SELECT id, name, wins, matches \
        FROM players \
        ORDER BY wins,matches DESC"
    c.execute(players)
    for row in c.fetchall():
        standings.append(row)
    DB.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    match_results = "INSERT INTO matches VALUES (%s,%s)"
    winner_update = "UPDATE players \
                     SET matches = matches+1, wins = wins+1 \
                     WHERE id = %s;"
    loser_update = "UPDATE players \
                    SET matches = matches+1 \
                    WHERE id = %s"
    c.execute(match_results, (winner, loser))
    c.execute(winner_update, (winner,))
    c.execute(loser_update, (loser,))
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    pairings = []  # list that will store pairings

    DB = connect()
    c = DB.cursor()
    # Find registered players and sort by most wins descending
    standings = "SELECT id, name \
        FROM players \
        ORDER BY wins,matches"
    c.execute(standings)
    players = c.fetchall()
    # Next we pair adjacent players in standings
    pairings = [(players[i-1] + players[i])
                for i in range(1, len(players), 2)]
    return pairings
