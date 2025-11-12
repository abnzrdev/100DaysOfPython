# Written by Abenezer

# Step 1: Get all names from the file
with open('Input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()

# Step 2: Get the letter template
with open('Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter_template = letter_file.read()

# Step 3: Make a letter for each name
for name in names:
    clean_name = name.strip()  # Remove spaces and newlines
    # Replace [name] with the real name
    personalized_letter = letter_template.replace('[name]', clean_name)
    # Add the author at the end
    personalized_letter += '\n\nWritten by Abenezer'
    # Save the new letter
    with open(f'Output/ReadyToSend/letter_for_{clean_name}.txt', 'w') as output_file:
        output_file.write(personalized_letter)

print('All letters are ready!')
