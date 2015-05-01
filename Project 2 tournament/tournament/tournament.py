#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM match;")
    db.commit()
    cur.close()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    cur = db.cursor()
    cur.execute("DELETE FROM player;")
    db.commit()
    cur.close()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT count(*) FROM player;")
    count = cur.fetchone() [0]
    cur.close()
    db.close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.
    (This is handled by your SQL database schema, not in this Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    cur = db.cursor()
    clean_name = bleach.clean(name)        # scrub the input
    SQL = "INSERT INTO player (player_name) VALUES (%s);"
    data = (clean_name, )
    cur.execute(SQL, data)                 # use this recommended form of data passing for SQL
    db.commit()
    cur.close()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT * FROM standings;")
    standings = [(row[0], str(row[1]), row[2], row[3],) for row in cur.fetchall()]
    cur.close()
    db.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    cur = db.cursor()
    SQL = "INSERT INTO match (player_1, player_2, winner) VALUES (%s, %s, %s);"
    data = (winner, loser, winner, )
    cur.execute(SQL, data)
    db.commit()
    cur.close()
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
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT * FROM standings;")
    players = cur.fetchall()
    cur.close()
    db.close()

    num_players = len(players)
    match = []
    player1=num_players-1
    while player1 > 0:                  # handles only even number of players in this code
        match.append((players[player1][0], players[player1][1], players[player1-1][0], players[player1-1][1]))
        player1 -= 2
        
    return match

