names = ['Aang', 'Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']

with open("./Input/Names/invited_names.txt", 'r') as file:
    all_names = file.readlines()
    print(all_names)                # returns the names as a list

with open("./Input/Letters/starting_letter.txt") as file:
    start_letter = file.read()
    for each_name in names:                                                             # for every name in the list
        new_letter = start_letter.replace("[name]", f"{each_name}")        # replace [name] with each name
        # empty _letter = open(f"./Output/ReadyToSend/letter_to_{each_name}", "x")      # create empty letter per name

        # Find the letter and append text to empty letters
        with open(f"./Output/ReadyToSend/letter_to_{each_name}", mode='a') as new_file:
            new_file.write(f"{new_letter}")

