
def main(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def word_count(text):
    return len(text.split())

def character_count(text):
    dictionary = {}
    seen = set()
    ignore = [' ','\n']
    for char in text:
        char1 = char.lower()
        if char1 in ignore:
            continue
        if char1 not in seen:
            dictionary[char1]=1
            seen.add(char1)
        else:
            dictionary[char1]+=1
    return dictionary

def report(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))
    print('--- Begin report of books/frankenstein.txt ---')
    for key in sorted_dict:
        print(f'The \'{key}\' character was found {sorted_dict[key]} times')
    print('--- End report ---')
        
book = main('books/frankenstein.txt')
print(f'{word_count(book)} words found in the document\n')
report(character_count(book))