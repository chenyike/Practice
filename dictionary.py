#program for computing the frequency of words in a given text

freq = {}

def freqCount(line):
    #get the global dictinary
    global freq
    words = line.split()
    for word in words:
        #convert word to lower case
        word=word.lower()
        # if the word has never seen before, put this new word in the dictionary and set the frequency to 1
        freq[word] = freq.get(word,0) + 1

        
def most_frequent():
    global freq
    words = freq.keys()
    frequencies=freq.values()
    max_freq=max(frequencies)
    #At what index did the max freq occur
    disired_index=frequencies.index(max_freq)
    return (words[disired_index],max_freq)


def main():
    line = raw_input('enter text and use quit to quit\n')
    while line != 'quit':
        freqCount(line)
        line = raw_input()
    for word in freq:
        print word + ' occurs ' + str(freq[word]) + ' times'


    print 'most_frequent word is',most_frequent()

main()
