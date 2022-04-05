#Aaron Miller
#Programming Languages Final Project
#May 19, 2021

import datetime
import json

#dictionary of players, each player is a nested dictionary
players = {}

def eval(text):
    #splits input into array by spaces
    text = text.split(' ')

    #creates player
    if text[0] == "active":
        if checkArgs(text, 4):
            players[text[1]] = {'name': text[2],
                                'position': text[3],
                                'yards': 0,
                                'rushAttempts': 0,
                                'passAttempts': 0,
                                'passCompletions': 0,
                                'touchdowns': 0,
                                'interceptions': 0,
                                'fumbles': 0}
        else:
            print("USAGE: active [player number] [player name] [position]")

    #two functions that do not take a player number, checked before player number is checked

    #output creates a .json file with all the created players and their stats
    elif text[0] == "output":
        if (checkArgs(text, 1)):
            #date is included in file name to differentiate
            current = datetime.datetime.now()
            format = "%Y-%d-%m_%H:%M:%S"
            formatTime = current.strftime(format)

            file = open("game_" + formatTime + ".json", "x")
            file.write(json.dumps(players, indent = 4))
            file.close()
        else:
            print("USAGE: output")

    #takes in a .json file and places the players in the dictionary
    elif text[0] == "load":
        if checkArgs(text, 2):
            try:
                file = open(text[1])
                #clears the dictionary before inserting the new players
                players.clear()
                players.update(json.load(file))
            except:
                print("Unable to open file: ", text[1])
        else:
            print("USAGE: load [file name]")


    else:
        try:
            #if the player number exists, evaluate the rest
            #if no player number is given, exception is thrown
            if checkPlayer(text[1]):
                evalPlay(text)
        except:
            print("Must also include a player number for commands")

def checkArgs(text, number):
    return len(text) == number

#checks to see if a player number exists in the dictionary
def checkPlayer(number):
    found = False
    for player in players:
        #if player is found, evaluate the rest of the input
        if player == number:
            return True
    if not found:
        print("No player matching number ", number)
        return False;

#if the input was not active, output, or load, text is evaluated here
def evalPlay(text):
    if text[0] == "incomplete":
        if checkArgs(text, 2) or checkArgs(text, 3):
            #if a second player is listed (example: a dropped pass)
            #it is taken as a second argument
            if len(text) == 3:
                #second player still needs to be checked if it exists
                if checkPlayer(text[len(text) - 1]):
                    players[text[1]]['passAttempts'] += 1
                    players[text[len(text) - 1]]['passAttempts'] += 1
            else:
                players[text[1]]['passAttempts'] += 1
        else:
            print("USAGE: incomplete [player number]")
            print("OR: incomplete [player number] [player number] ")

    elif text[0] == "complete":
        if checkArgs(text, 4):
            players[text[1]]['passAttempts'] += 1
            players[text[1]]['passCompletions'] += 1

            players[text[2]]['passAttempts'] += 1
            players[text[2]]['passCompletions'] += 1

            players[text[1]]['yards'] += int(text[3])
            players[text[2]]['yards'] += int(text[3])
        else:
            print("USAGE: complete [player number] [player number] [number of yards]")

    elif text[0] == "rush":
        if checkArgs(text, 3):
            players[text[1]]['yards'] += int(text[2])
            players[text[1]]['rushAttempts'] += 1
        else:
            print("USAGE: rush [player number] [number of yards]")

    elif text[0] == "fumble":
        if checkArgs(text, 2):
            players[text[1]]['fumbles'] += 1
        else:
            print("USAGE: fumble [player number]")

    elif text[0] == "interception":
        if checkArgs(text, 2):
            players[text[1]]['interceptions'] += 1
        else:
            print("USAGE: interception [player number]")

    elif text[0] == "touchdown":
        #if a second player is listed (example: the person that caught the touchdown),
        #credit them with a touchdown too
        if checkArgs(text, 2) or checkArgs(text, 3):
            if len(text) == 3:
                #second player still needs to be checked in dictionary
                if checkPlayer(text[len(text) - 1]):
                    players[text[1]]['touchdowns'] += 1
                    players[text[len(text) - 1]]['touchdowns'] += 1
            else:
                players[text[1]]['touchdowns'] += 1
        else:
            print("USAGE: touchdown [player number]")
            print("OR: touchdown [player number] [player number]")

    elif text[0] == "stats":
        if checkArgs(text, 2):
            print("\nNumber: ", text[1])
            print("Name: ", players[text[1]]['name'])
            print("Position: ", players[text[1]]['position'])
            print("Yards: ", players[text[1]]['yards'])
            print("Rush Attempts: ", players[text[1]]['rushAttempts'])
            print("Pass Attempts: ", players[text[1]]['passAttempts'])
            print("Pass Completions: ", players[text[1]]['passCompletions'])
            print("Touchdowns: ", players[text[1]]['touchdowns'])
            print("Interceptions: ", players[text[1]]['interceptions'])
            print("Fumbles: ", players[text[1]]['fumbles'], "\n")
        else:
            print("USAGE: stats [player number]")

    #input did not match any of the recognized commands
    else:
        print("Unrecognized input")

def repl(prompt='football> '):
    while True:
        try:
            text = input(prompt)
        except EOFError:
            break

        #if no input is given, give new prompt
        if len(text) == 0:
            continue

        #leave repl
        if text in ('quit'):
            break

        try:
            eval(text)
        except:
            print("Unknown error")

if __name__ == '__main__':
    repl()
