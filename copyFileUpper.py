def fileOnTheWall():
    file = input("Enter name of file. ")
    openIt = open(file,"r")
    contents = openIt
    
    for i in range(len(contents)):
        x = contents[i]
        print(x.upper())
        
fileOnTheWall()
