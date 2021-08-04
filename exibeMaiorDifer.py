# having fun
def exibeMaiorDifer(x):
    diferList = []
    numList = []
    
    for elem in x:
        if x.index(elem) < len(x)-1:
            difer = abs(elem - x[x.index(elem)+1])
            diferList.append(difer)
            numList.append([x[x.index(elem)],x[x.index(elem)+1]])
    
    var = diferList[0]
    for elem in diferList:
        if elem > var:
            var = elem
    
    print("Maior diferença: " + str(var) + " (que é a diferença entre " + str(numList[diferList.index(var)][0]) + " e " + str(numList[diferList.index(var)][1]) + ")")

x = [1.3, 4.2, 2.5, 3.0, -1.1]
y = [11.0, 3.0, 13.0, 18.0]

exibeMaiorDifer(x)
exibeMaiorDifer(y)
