def notes_strategy(player_notes):
    for key, value in player_notes.items():
        print("\nNotes on " + key +": " + ". ".join(value))
        print("1. Remove Note or Action")
        print("2. Add Action")
        print("3. Add Note")
        print("4. Nothing")
        add_note = input("Choice:")
        if add_note == "2":
            note = input("Action: ")
            fascist_action = input("Was the action fascist or liberal? (L/F)").upper()
            if fascist_action == "F":
                level_sus = input("How suspicious is the action? (1-10)")
                value.append(note + " (" + "Fascist)" + "(" + level_sus + ")")
            elif fascist_action == "L":
                level_sus = input("How Liberal is the action? (1-10)")
                value.append(note + " (" + "Liberal)" + "(" + level_sus + ")")
                
        elif add_note == "1":
            try:
                note = int(input("Enter the number of the note to remove(Notes are separated by '.'): "))
                value.remove(value[note-1])
            except:
                print("Invalid input")
        elif add_note == "3":
            note = input("Note: ")
            value.append(note)
        elif add_note == "4":
            pass
    count_fas_dict = {}
    count_lib_dict = {}
    for name, value in player_notes.items():
        count_fas = 0
        count_lib = 0
        for note in value:
            try:
                lit = note.split("(")
                fas_lib = lit[1]
                points = int(lit[2].strip(")"))
                if fas_lib == "Fascist)":
                    count_fas += points
                elif fas_lib == "Liberal)":
                    count_lib += points
            except:
                pass
        count_fas_dict[name] = count_fas
        count_lib_dict[name] = count_lib
    lib_num = 0
    lib_name = ""
    fas_num = 0
    fas_name = ""
    for name in count_fas_dict.keys():
        fas_count = count_fas_dict[name]
        lib_count = count_lib_dict[name]
        difference = lib_count - fas_count
        if difference > lib_num:
            lib_count = difference
            lib_name = name
        if difference < fas_num:
            fas_num = difference
            fas_name = name
    recomendation = []
    recomendation.append(lib_name)
    recomendation.append(fas_name)
    return player_notes, recomendation
if __name__ == "__main__":
    player_notes = {"Axel": []}
    player_notes, recomendation =liberal_play(player_notes)
    liberal_recomendation = recomendation[0]
    fascist_recomendation = recomendation[1]
    print("Top Choice: " + liberal_recomendation)
    print("Bottom Choice: " + fascist_recomendation)
    for name, notes in player_notes.items():
        print("Notes on " + name + ": " + ". ".join(notes))