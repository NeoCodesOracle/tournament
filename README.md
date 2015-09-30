Swiss Tournament Application
============================
This application is an assignment for the course Intro to Relational Databases, part of Udacity's Full Stack Nanodegree Program. It is an application that helps manage Swiss style tournaments. The objective was to write a program using Python in conjuction with PSQL that would pass all tests found in the file tournament_test.py.

Installation
------------

#### Requirements
1. Git
2. Virtual Box
3. Vagrant

#### Setup

1. Open terminal:
   * Windows: 
        Open Git Bash, which installed at the time you installed Git. This will open a Unix-style terminal.
   * Other systems: 
        Use any terminal program of your choosing
2. Change from your root directory to the directory of your choice.   
  Example: `cd Desktop/my_directory`
3. Clone VM Configuration
    From Git, enter the following command:
    `git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack`, 
    this will create a new directory named fullstack, a clone of Udacity's repository for this assignment which holds all of the configuration files needed to run this application.

4. Move to the vagrant folder by entering: cd fullstack/vagrant/

5. Clone Project: From Git, clone this project by entering the following command:
    `git clone https://github.com/NeoCodesOracle/tournament.git'
    This will create a directory inside the vagrant directory named tournament.

6. Run Vagrant 
    At the prompt type: vagrant up

Usage
-----

After completing all installation steps you are ready to connect to Vagrant box. Connect by following these steps:

1. At the pormpt enter the follwoing command: vagrant ssh
2. Move to tournament directory by entering: cd /vagrant/tournament/
3. Log in to psql by typing this command at the prompt: psql
4. Next you need to initialize the database. Type \i tournament.sql , which will import the commands fournd in our file that contains the database schema for this application. Simply run this command anytime you want to 'reset' the tournament.
5. Exit psql by typing the command \q

Running Udacity's Test File
---------------------------

After executing the last command above, enter the following command: python tournament_test.py. This command will test against the file provided by Udacity to ensure all criteria is met.

File Contents
-------------
1. **tournament.py**
    Main python file that runs the Swiss tournament
2. **tournament.sql**
    File that stores database schemas for tournament
3. **tournament_test.py**
    Udacity's Python test file

Function Descriptions
---------------------

Function        | Description
----------------|----------------------------------------------------------
Connect()       | Meant to connect to the database. Already set up for you.
deleteMatches() | Remove all the matches records from the database.
deletePlayers() | Remove all the player records from the database.
countPlayers()  | Returns the number of players currently registered
registerPlayer(name)| Adds a player to the tournament database.
playerStandings() | Returns a list of the players and their win records, sorted by wins. 
reportMatch(winner, loser)   | This is to simply populate the matches table and record the winner and loser as (winner,loser) in the insert statement.
swissPairings() | Returns a list of pairs of players for the next round of a match. Here all we are doing is the pairing of alternate players from the player standings table, zipping them up and appending them to a list with values: (id1, name1, id2, name2)


Credits

Created by NeoCodesOracle
License

Licensed under the MIT License (MIT)

Copyright (c) [2015] [NeoCodesOracle]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS ORIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.