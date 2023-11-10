def ruleset(user1Input, user2Input):
    if user1Input == user2Input:
        "Tie"
    elif user1Input == "rock" and user2Input == "scissors":
        return 'first'
    elif user1Input == "scissors" and user2Input == "paper":
        return 'first'
    elif user1Input == "paper" and user2Input == 'rock':
        return 'first'
    else:
        return 'second'

def forcePlayerRespondPvP():
    shouldBePvP = input("Will this game be Player versus Player? Y/N: ").casefold()
    answers = ['Y'.casefold(), ' Y'.casefold(), 'N'.casefold(), ' N'.casefold()]
    while shouldBePvP not in answers:
        print(f'Put in "{shouldBePvP}", needs to be one of the following(case-insensitive): {answers}')
        shouldBePvP = input("Will this game be Player versus Player? Y/N: ").casefold()
    return shouldBePvP

def forcePlayerAnswerChoice(choices):
    playerInput = input("rock, paper, or scissors?: ")
    while playerInput not in choices:
        print(f'Put in "{playerInput}", needs to be one of the following: {choices}')
        playerInput = input("rock, paper, or scissors?: ")
    return playerInput

def checkResult(player1,player2,computer):
    if computer == None: #mode is PvP
        if ruleset(player1, player2) == 'first':
            return 'player1'
        else:
            return 'player2'
    else: #if mode is PvC
        if ruleset(player1,computer):
            return 'player1'
        else:
            return 'computer'