import os
def hitler_strategy():
    os.system("clear")
    print("Welcome to Hitler's game!")
    print("As Hitler, you want to stay lowkey and be trusted by the liberal party at almost all costs, \neven throwing your partner under the bus.")
    print("If killed, the fascist party will lose.")
    input("If handed Chancellor, the fascist party will win.")
def fascist_strategy():
    os.system("clear")
    print("Welcome to Fascist's game!")
    print("As Fascist, play aggresively and frame other liberals. Lay as many fascist cards as possible.")
    print("Try to fill the fascist seats as fast as possible.")
    input("Lie.")
def liberal_strategy():
    os.system("clear")
    print("Welcome to Liberal's game!")
    print("As Liberal, never trust anyone. Think critically and always tell the truth.")
    print("Don't give the chancellor to Hitler or you lose.")
    input("Try to fill the liberal seats before the fascists fill all the fascist seats.")
def card_counting(number_fascist_cards, number_liberal_cards):
    print("\n\nCards: ")
    print(f"Chances for fascist being flipped: {number_fascist_cards / (number_fascist_cards + number_liberal_cards)*100}%")
    print(f"Chances for liberal being flipped: {number_liberal_cards / (number_fascist_cards + number_liberal_cards)*100}%")
    num_fas = int(input("How many fascist cards did the president flip? "))
    num_lib = 3-num_fas
    number_fascist_cards = number_fascist_cards - num_fas
    number_liberal_cards = number_liberal_cards - num_lib
    if number_fascist_cards <= 0:
        print("Someone has lied about the fascist cards.")
    if number_liberal_cards <= 0:
        print("Someone has lied about the liberal cards.")
    return number_fascist_cards, number_liberal_cards
def chancellor_move(fascist_num, liberal_num):
    fascist_yes =input("Did the chancellor lay a fascist card? (y/n) ")
    if fascist_yes == "y":
        fascist_num +=1
    else:
        liberal_num +=1
    return fascist_num, liberal_num
def board(fascist_num, liberal_num):
    board_fascist = (["F "] * fascist_num) + (["_ "] * (6 - fascist_num))
    board_liberal = (["L "] * liberal_num) + (["_ "] * (5 - liberal_num))
    print("".join(board_fascist))
    print("".join(board_liberal))
def prime_suspects_list(prime_suspects):
    print("Prime suspects: ")
    for suspect in prime_suspects:
        print(suspect)
    suspect_plus = input("Do you want to add a suspect or a frameable person? (y/n)")
    if suspect_plus == "y":
        suspect = input("What is the name of the suspect or frameable person? ")
        prime_suspects.append(suspect)
    suspect_remove = input("Do you want to remove a suspect or frameable person? (y/n)")
    if suspect_remove == "y":
        suspect = input("What is the name of the suspect or frameable person? ")
        prime_suspects.remove(suspect)
    return prime_suspects
if __name__ == "__main__":
    number_fascist_cards = 11
    number_liberal_cards = 6
    players =  int(input("How many players are there? "))
    if players % 2 == 0:
        num_fascists = players / 2
        num_liberals = players / 2
    elif players % 2 == 1:
        num_fascists = (players - 1) / 2
        num_liberals = (players + 1) / 2
    else:
        print("Invalid number of players")
        exit()
    role = input("What role are you? (Fascist, Liberal)")
    if role == "Fascist":
        type_fascist = input("Are you Hitler? (y/n) ")
        if type_fascist == "y":
            hitler = True
            fascist = True
            liberal = False
        else:
            hitler = False
            fascist = True
            liberal = False
    elif role == "Liberal":
        liberal = True
        fascist = False
        hitler = False
    else:
        print("Invalid role")
        exit()
    if hitler:
        hitler_strategy()
    elif fascist:
        fascist_strategy()
    elif liberal:
        liberal_strategy()
    fascist_num = 0
    liberal_num = 0
    prime_suspects = []
    while True:
        board(fascist_num, liberal_num)
        prime_suspects = prime_suspects_list(prime_suspects)
        yes_no = input("Have you shuffled the cards? (y/n) ")
        if yes_no == "y":
            number_fascist_cards = 11
            number_liberal_cards = 6  
        chancellor = input("Are you chancellor? (y/n) ")
        president = input("Are you president? (y/n) ") 
        if chancellor == "y" and hitler:
            if fascist_num >= 3:
                print("Fascist win!")
                break
            else:
                print("Play safe and gain trust if the president is cleared.")
                print("If the president is a suspect, lie.")
                print("If the president is a fellow fascist, either frame them to gain trust or help the fascists.")
        elif chancellor == "y" and liberal:
            print("Play truthful and don't let the fascists frame you.")
        elif chancellor == "y" and fascist:
            print("Lie a lot but still don't make it obvious.")
            print("Or try to gain trust and manipulate liberals.")
        elif president == "y" and hitler:
            print(f"Prime suspects: {prime_suspects}")
            print("Give the chancellor to a person unsuspecting.")
            print("If the chancellor is a suspect, frame them.")
            print("Or play safe and stay lowkey and gain trust.")
            print("Only lie in extreme cases.")
        elif president == "y" and liberal:
            print(f"Prime suspects: {prime_suspects}")
            print("Give the chancellor to only trustworthy persons.")
            print("Always tell the truth and support the liberal cause.")
        elif president == "y" and fascist:
            print(f"Prime suspects: {prime_suspects}")
            print("Give the chancellor to a liberal or hitler if it doesn't cause suspicion.")
            print("Frame a liberal if they are suspicious.")
            print("Or play unlucky and say three fascist cards.")
            print("Lie a lot and play aggresive but not too obvious.")
        elif chancellor == "n" and liberal and president == "n":
            print(f"Prime suspects: {prime_suspects}")
            print("Think critically and don't trust anyone who isn't absolutely trustworthy.")
            print("Vote no if the president or chancellor is a suspect.")
        number_fascist_cards, number_liberal_cards = card_counting(number_fascist_cards, number_liberal_cards)
        fascist_num, liberal_num = chancellor_move(fascist_num, liberal_num)  