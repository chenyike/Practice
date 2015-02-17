#define function that counts number of vowels in a string
def vowelCount(string):
    counter=0
    for ch in string:
        if ch in ('a','e','i','o','u','A','E','I','O','U'):
            counter+=1
    return counter
