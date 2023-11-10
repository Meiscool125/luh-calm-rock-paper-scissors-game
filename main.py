from functions import forcePlayerRespondPvP,forcePlayerAnswerChoice,checkResult
shouldBePvP = forcePlayerRespondPvP()
if shouldBePvP.casefold() == ' Y'.casefold() or shouldBePvP.casefold() == 'Y'.casefold():
    #PvP = True
    choices = ["rock", "paper", "scissors"]
    player1Response = forcePlayerAnswerChoice(choices)
    player2Response = forcePlayerAnswerChoice(choices)
    finalResult = checkResult(player1Response,player2Response, None)

elif shouldBePvP.casefold() == 'N'.casefold() or shouldBePvP.casefold() == 'N'.casefold():
    #PvP = False
    import random
    choices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(choices)
    player1Response = forcePlayerAnswerChoice(choices)
    finalResult = checkResult(player1Response, None, computerChoice)
else:
    print("exit code 0: Can not recognize input. Please restart program and try again.")

