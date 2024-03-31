import os


def writeData():
    data = '\nCreate me in here.'
    with open('dalt.txt', 'a') as f:
        f.write(data)
        f.close()



def openFile():
    with open('dalt.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()





if __name__ == "__main__":
    writeData()
    openFile()
    
