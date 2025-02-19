def character_count(file_contents):
    character_dict = {}
    new_string = []
  
    for character in file_contents:
        if character.isalpha():
            new_string.append(character.lower())

    for character in new_string:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    for value in character_dict:
        print(f"The '{value}' character was found {character_dict[value]} times")
    
    


def main():
    with open('books/frankenstein.txt', encoding='utf-8') as f:
        file_contents = f.read()
        # Split the file contents into a list of words
        file_string = file_contents.split()
        # Count the number of words in the file
        count_words = len(file_string)

        #print(f'{count_words}') 
        character_count(file_contents)         

main()