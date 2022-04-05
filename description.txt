Football Stats DSL
Programming Languages Final
Aaron Miller

A mini programming language to keep track of stats during a football game
and to output player stats at the end of the game

Each player has these statistics:
name
position
yards
rush attempts
pass attempts
pass completions
touchdowns
interceptions
fumbles

GRAMMAR

active [player number] [player name] [position]
Creates a player in the dictionary with other stats set to 0

output
exports the data to a .json file
title includes the time of file creation

load [file name]
takes in a .json file of players and places them in the dictionary
clears any existing players from the dictionary

incomplete [player number] OR
incomplete [player number] [player number]
can take in one or two arguments depending on if one or two players should be credited with an incomplete pass
both players incremented one incomplete pass
order of player numbers does not matter

complete [player number] [player number] [number of yards]
order of player numbers does not matter
both players incremented one attempt, one completion, and number of years gained

rush [player number] [number of yards]
player incremented one rush attempt and number of yards

fumble [player number]
player incremented one fumble

interception [player number]
player incremented one interception

touchdown [player number] OR
touchdown [player number] [player number]
takes one or two players depending on number of players credited with touchdown
player(s) incremented one touchdown

stats [player number]
all stat categories listed for the given player
