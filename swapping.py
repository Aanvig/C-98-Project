

def swapData():
    essay = input("File 1 name: ")
    decoy = input("File 2 name: ")


    with open(essay, "r") as a:
        data_a = a.read()
    
    with open(decoy, "r") as b:
        data_b = b.read()

    with open(essay,"w") as a:
        a.write(data_b)

    with open(decoy,"w") as b:
        b.write(data_a)

    print(data_a)
    print(data_b)
    


swapData()