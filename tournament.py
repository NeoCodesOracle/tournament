#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect(database_name="tournament"):
    """Connect to tournament database and return connection and cursor"""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def deleteMatches():
    """Remove all the match records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db, cursor = connect()
    cursor.execute("DELETE FROM players")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db, cursor = connect()
    sql_query = "SELECT count(name) AS num FROM players"
    cursor.execute(sql_query)
    players = cursor.fetchone()[0]
    db.close()
    return players


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    player = "INSERT INTO players (name, matches, wins) VALUES (%s,%s,%s)"
    cursor.execute(player, (name,0,0))
    db.commit()
    db.close()


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

    db, cursor = connect()
    players = "SELECT id, name, wins, matches \
        FROM players \
        ORDER BY wins,matches DESC"
    cursor.execute(players)
    for row in cursor.fetchall():
        standings.append(row)
    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, cursor = connect()
    match_results = "INSERT INTO matches VALUES (%s,%s)"
    winner_update = "UPDATE players \
                     SET matches = matches+1, wins = wins+1 \
                     WHERE id = %s;"
    loser_update = "UPDATE players \
                    SET matches = matches+1 \
                    WHERE id = %s"
    cursor.execute(match_results, (winner, loser))
    cursor.execute(winner_update, (winner,))
    cursor.execute(loser_update, (loser,))
    db.commit()
    db.close()


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
    pairings = [] 
    total_players = countPlayers()

    db, cursor = connect()
    # Find registered players and sort by most wins descending
    query = "SELECT id, name \
        FROM players \
        ORDER BY wins,matches"
    cursor.execute(query)
    players = cursor.fetchall()
    # Next we pair adjacent players in standings
    if total_players % 2 == 0:
        pairings = [(players[i-1] + players[i])
                    for i in range(1, len(players), 2)]
    else:
        raise "Uneven number of players."

    return pairings
