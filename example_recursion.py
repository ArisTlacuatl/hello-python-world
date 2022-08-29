def countdown(i):
    print i
    #Base case:
    if i<= 1:
        return
    #Recursive case:
    else:
        countdown(i-1)

        