'''
keyNumbers = {3:"Fizz", 5:"Buzz"}
For i <- 1 To 15
    output <- ""
    For num in keyNumbers.keys
        if i MOD num = 0 THEN
            output <- output + keyNumbers[num]
    if output = "" THEN
        output = str(i)
    #python version of if statement above# output = output if output else str(i)
    print(output)
'''


keyNumbers = {3:"Fizz", 5:"Buzz"}
for i in range(1, 16):
    output = ""
    for num in list(keyNumbers.keys()):
        if i % num == 0:
            output += keyNumbers[num]
    output = output if output else str(i)

    print(output)