
def count_lines(list_of_lines):
    '''Count number of lines in a list of lines. '''
    return len(list_of_lines)
    
def count_words(list_of_words):
    '''count words in a list of lines'''
    word_count = 0
    for line in list_of_lines:
        list_of_words = lines.split()
        word_count += len(list_of_words)
    return word_count
        
##def count_characters(list_of_lines):
##    for 

def main():
    # ask for a file name
    filename = raw_input('Give me a file name please. \n')
    # count characters
    # count words
    # count lines
    f= open(filename)
    lines = f.readlines()
    print lines
    print count_lines(lines)

    f.seek(0)
    content = f.read()

        
if __name__ == '__main__':
    main()
