'''
keyNumbers = {3:"Fizz", 5:"Buzz"}
For i <- 1 To 15
    output = ""
    For num in keyNumbers.keys
        if i MOD num == 0 THEN
            output <- output + keyNumbers[num]
    #python only# output = output if output else str(i)
    print(output)
'''