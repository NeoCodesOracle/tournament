Swiss Tournament Generator

This application is an assignment for the course Intro to Relational Databases, part of Udacity's Full Stack Nanodegree Program. It is an application that helps manage Swiss style tournaments. The objective was to write a program using Python in conjuction with PSQL that would pass all tests found in the file tournament_test.py.

Installation

Prerequisites:
Prerequisite  Documentation   Download
Git   docs  download
Virtual Box   docs  download
Vagrant   docs  download

Installation Steps:

    Open terminal:
      Windows: Open Git Bash, which installed at the time you installed Git. This will open a Unix-style terminal.
      Other systems: Use any terminal program of your choosing
      Change from your root directory to the directory of your choice
        Example: cd Desktop/my_directory
    Clone VM Configuration
        From Git: Enter the following command
         git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack
         this will create a new directory titled fullstack that will hold all of the configuration files needed to run this application.
    Move to the vagrant folder by entering: cd fullstack/vagrant/
    Using Git, clone this project:
        Run: git clone https://github.com/gravic07/tournament.git tournament
        This will create a directory inside the vagrant directory titled tournament.
    Run Vagrant by entering: vagrant up

File Contents
tournament.py This is the main Python file used to conduct the Swiss Style Tournament.
tournament.sql This is the database used to store tournament records.
tournament_test.py This is a python file created by Udacity and modified to perform essential tests on the tournament application.


Usage

Once the installation steps are complete, you are ready to connect to the Vagrant box. To connect:

    Log into Vagrant VM by entering: vagrant ssh
    Move to tournament directory by entering: cd /vagrant/tournament/

    Create the tournament database by entering: psql -f tournament.sql

        Note: You can run psql -f tournament.sql at anytime to completely delete the database and start over.

    If you would like to test the database against Udacity's criteria, enter: python tournament_test.py

        Note: To clear the database after running tournament_test.py, you can either call the deletePlayers() and deleteMatches() functions or refer to step 3.

    Launch Python command line by entering python
    Import tournament by entering: import tournament
    Execute a desired function. (see below)


Functions

    Note: Make sure you import tournament.py before attempting to call any of these functions by entering import tournament and pressing enter.

    Note: All functions need to be proceeded by tournament. e.g. tournament.playerStandings()

    Note: The tournament argument is a three character code that is assigned to players in the same tournament.

registerPlayer(tournament, name)
Registers a player by the name provided. The tournament argument is optional and if a tournament is passed, the player will be registered to that tournament. A player ID will be automatically generated.

countPlayers(tournament)
Counts the number of players in the registry. The tournament argument is optional and if a tournament is passed, only the players registered for that tournament will be counted.

deletePlayers(playerID) Deletes players from the registry. The playerID argument is optional and if a player ID if passed, only that player will be deleted.

reportMatch(tournament, player, opponent, result)
Reports a match between two players.
tournament: tournament code
player: id number of the player
opponent: id number of the opponent result: result of match (must be 'win', 'lose', 'tie')

    Note: reportMatch() also reports a second match with the opponent as the player and the player as the opponent.

deleteMatches(tournament)
Deletes all match record. If a three character tournament code is passed, only the matches for the tournament will be deleted.

playerStandings()
Returns the win record of all registered players.
More specifically, returns a list of tuples each consisting of a player's id, name, # of wins, and # of matches. The players are returned in Ascending order based on # of wins.
Example:

[ (103, 'Rich Guy', 3L, 3L),
  (111, 'Cool Guy', 2L, 3L),
  (104, 'Poor Guy', 2L, 3L),
  (108, 'Big Guy', 2L, 3L),
  (101, 'New Guy', 1L, 3L),
  (110, 'Bad Guy', 1L, 3L),
  (105, 'Tall Guy', 1L, 3L),
  (107, 'Small Guy', 1L, 3L),
  (109, 'Good Guy', 1L, 3L),
  (106, 'Short Guy', 0L, 3L),
  (102, 'Old Guy', 0L, 3L) ]

swissPairings(tournament)
Returns a new round of matches based on the Swiss Tournament pairing guidelines.
More specifically, returns a list of tuples each consisting of player id, player name, opponent id, and opponent name. The tournament argument is optional and if a tournament is passed, only the players registered for that tournament will be considered in the pairing.
Example:

[ (106, 'Short Guy', 0, 'BYE'),
  (103, 'Rich Guy', 108, 'Big Guy'),
  (104, 'Poor Guy', 111, 'Cool Guy'),
  (109, 'Good Guy', 105, 'Tall Guy'),
  (101, 'New Guy', 110, 'Bad Guy'),
  (107, 'Small Guy', 102, 'Old Guy') ]

    Note: The above example returned a BYE round since an odd number of players where registered for the tournament.

    Note: If swissPairings() can not be completed due to tournament guideline constraints, the pairing will be aborted.


Credits

Created by NeoCodesOracle
License

Licensed under the MIT License (MIT)

Copyright (c) [2015] [NeoCodesOracle]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS ORIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
