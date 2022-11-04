def fileOnTheWall():
    file = input("Enter name of file. ")
    writeIt = 'UPPER' + file
    newOne = open(writeIt,"w")
    contents = writeIt
    
    for i in range(len(contents)):
        x = contents[i]
        newOne.write(x.upper())
        print(newOne)
        
fileOnTheWall()
