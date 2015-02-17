#make a calculator


#Read an input (read an entire string e.g., 3+5)
def ReadInput():
    InputString = raw_input ('Enter computation e.g., 3+5')
    #Available only in this function
    return InputString

#Check for valid input
def CheckValidity(string):
    if string[0] not in '0123456789':
        return False
    if '+' not in string and
       '-' not in string and
       '*' not in string and
       '/' not in string and
       '^' not in string:
        return False
    #Lots of checking needed
    return True

def Execute (InputString):
    answer = eval (InputString)
    return answer
    
def main():
    #Read an input (read an entire string e.g., 3+5)
    InputString = ReadInput()
    #Check for valid input
    valid = CheckValidity(InputString)
    if valid:
        #Do the operation
        answer = Execute(InputString)
        #Print the result in some manner
    else:
        print 'Error'
    
