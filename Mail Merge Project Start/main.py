PLACEHOLDER = "[name]"

# Read from the text file containing the names to be included in the new text file
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
    print(names)

# Read the starting text file that is used to build the tailored letters
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    # read the names from the file
    letter_contents = letter_file.read()

    # loop through the text file with the names
    for name in names:
        # take the name from the text file
        stripped_name = name.strip()

        """
        Wherever "[name] is found in the text file, replace that with the stripped name, 
        obtained from the name text file"
        """
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)

        # create a new file with the newly created text with a new name
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
