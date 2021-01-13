'''
keyNumbers = [3, 5]
keyWords = ["Fizz", "Buzz"]
FOR i <- 1 TO 15
    output <- ""
    FOR j <- 1 To 2
        IF i MOD keyNumbers[j] = 0 THEN
            output <- output + keyWords[j]
    IF output = "" THEN
        output = str(i)
    print(output)
'''


keyNumbers = [3, 5]
keyWords = ["Fizz", "Buzz"]
for i in range(1, 16):
    output = ""
    for j in range(0, len(keyNumbers)):
        if i % keyNumbers[j] == 0:
            output += keyWords[num]
    if output == "":
        output = i

    print(output)