#program to convert Celsius to Fahrenheit
Choice = raw_input('do you use C or F ? ')  #Choice is scoped to the entire program
    
# Conditional Statement
# if choice is C then C -> F
# if choice is F then F -> C
# if choice is something else print Error

if Choice in ('C','c'):
    c = input ('what is the temperature in Celsius ? \n') 
    f = 9.0 * c / 5.0  + 32
    print 'the temperature in Fahrenheit is ', f

elif Choice in ('F','f'):
    f = input ('what is the temperature in Fahrenheit ? \n') 
    c = 5.0 / 9 *( f - 32 )
    print 'the temperature in Celcius is ', c

else:
    print 'Error'


# Ask repeatedly
CountChoice=raw_input('Do you want to continue?')
while CountChoice !='n':
    Choice = raw_input('do you use C or F ? ') 
    if Choice in ('C','c'):
        c = input ('what is the temperature in Celsius ? \n') 
        f = 9.0 * c / 5.0  + 32
        print 'the temperature in Fahrenheit is ', f

    elif Choice in ('F','f'):
        f = input ('what is the temperature in Fahrenheit ? \n') 
        c = 5.0 / 9 *( f - 32 )
        print 'the temperature in Celcius is ', c

    else:
        print 'Error'
    
