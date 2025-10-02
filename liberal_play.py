def liberal_play(player_notes):
    for key, value in player_notes.items():
        print("Notes on " + key +": " + ". ".join(value))
        add_note = input("Do you want to remove, add a note or do nothing? (R, A, N) ")
        if add_note == "A":
            note = input("Note: ")
            value.append(note)
        elif add_note == "R":
            try:
                note = int(input("Enter the number of the note to remove(Notes are separated by '.'): "))
                value.remove(value[note-1])
            except:
                print("Invalid input")
        elif add_note == "N":
            pass
    return player_notes
if __name__ == "__main__":
    liberal_play()