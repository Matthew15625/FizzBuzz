'''
keyNumbers = [3, 5]
keyWords = ["Fizz", "Buzz"]
OUTPUT "How far to count?"
INPUT howFar
WHILE howFar < 1
    OUTPUT "Not a valid number, please try again."
    INPUT howFar
ENDWHILE
FOR i <- 1 TO howFar
    output <- ""
    FOR j <- 1 To 2
        IF i MOD keyNumbers[j] = 0
            output <- output + keyWords[j]
        ENDIF
    ENDFOR
    IF output = ""
        output <- str(i)
    ENDIF
    OUTPUT output
ENDFOR
'''


keyNumbers = [3, 5]
keyWords = ["Fizz", "Buzz"]
howFar = ""
validInput = False
while not validInput:
    howFar = input("How far to count?")
    try:
        howFar = int(howFar)
        if howFar >= 1:
            validInput = True
            break
    except:
        pass
    print("Not a valid number, please try again.")

for i in range(1, howFar+1):
    output = ""
    for j in range(0, len(keyNumbers)):
        if i % keyNumbers[j] == 0:
            output += keyWords[j]
    if output == "":
        output = i

    print(output)