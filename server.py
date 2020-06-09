import socketserver
from collections import OrderedDict
import re

customerRecord = []
custDict = {}

def loadDataFile():
    with open("data.txt","r") as file:
        for line in file.readlines():
            if(line[0]!="|"):
                line1 = line.strip("\n")
                line2 = line1.split("|")
                re.sub(" ","  ",line2[0])
                customerRecord.append(tuple(line2))  
                d1 = {line2[0].strip(" ").capitalize():line2[1:]}
                custDict.update(d1)
        file.close()
    with open("data.txt","w+") as raw:
        for k,v in custDict.items():
            length = len(v)
            count=0
            string = ""
            while count<length:
                string += "|" + v[count] 
                count+=1
            raw.write(f"{k}{string}"+"\n")
        raw.close()
    return custDict

def choice(message):
    selection = message[0]
    if(selection=="1"):
        temp = message.split("|")
        if temp[1] in custDict:
            fetch = custDict[temp[1]]
            return str(tuple(fetch))
        else:
            return "Customer not found"

    elif selection=="2":
        temp = message.strip("\n")
        temp1 = temp.split("|")
        if temp1[1] in custDict:
            return "Customer already exists"
        else:
            with open("data.txt","a+") as file:
                temp1[4]= temp1[4]+"\n"
                file.write(f"{temp1[1]}|{temp1[2]}|{temp1[3]}|{temp1[4]}")
                file.close()
            loadDataFile()
            return "Data Added and file updated"
    
    elif selection=="3":
        tempMessage = message.split("|")
        if(custDict.pop(tempMessage[1])):
            with open("data.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                    temp = line.split("|")
                    if(temp[0]==tempMessage[1]):
                        lines.remove(line)
                        file.close()
                with open("data.txt","w+") as newFile:
                    for line in lines:
                        newFile.write(line)
                    newFile.close()
                    loadDataFile()
            return "Data Deleted"
        else:
            return "Customer not found"
    
    elif selection=="4":
        tempMessage = message.split("|")
        name = tempMessage[1]
        age = tempMessage[2]
        if name in custDict:
            with open("data.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                    temp = line.split("|")
                    if(temp[0]==name):
                        temp[1]=age
                        lines.remove(line)
                        lines.insert(0,(f"{temp[0]}|{temp[1]}|{temp[2]}|{temp[3]}"))
                        file.close()
                with open("data.txt","w+") as newFile:
                    for line in lines:
                        newFile.write(line)
                    newFile.close()
                    loadDataFile()
            return "Customer's age updated"
        else:
            return "Customer not found"
    
    elif selection=="5":
        tempMessage = message.split("|")
        name = tempMessage[1]
        addres = tempMessage[2]
        if name in custDict:
            with open("data.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                    temp = line.split("|")
                    if(temp[0]==name):
                        temp[2]=addres
                        lines.remove(line)
                        lines.insert(0,(f"{temp[0]}|{temp[1]}|{temp[2]}|{temp[3]}"))
                        file.close()
                with open("data.txt","w+") as newFile:
                    for line in lines:
                        newFile.write(line)
                    newFile.close()
                    loadDataFile()
            return "Customer's address updated"
        else:
            return "Customer not found"
    
    elif selection=="6":
        tempMessage = message.split("|")
        name = tempMessage[1]
        phone = tempMessage[2]
        if name in custDict:
            with open("data.txt","r") as file:
                lines = file.readlines()
                for line in lines:
                    temp = line.split("|")
                    if(temp[0]==name):
                        temp[3]=phone
                        lines.remove(line)
                        lines.insert(0,(f"{temp[0].capitalize()}|{temp[1]}|{temp[2]}|{temp[3]}"+"\n"))
                        file.close()
                with open("data.txt","w+") as newFile:
                    for line in lines:
                        newFile.write(line)
                    newFile.close()
                    loadDataFile()
            return "Customer's phone updated"
        else:
            return "Customer not found"

    elif selection =="7":
        rep = '\n'
        report = OrderedDict(sorted(custDict.items()))
        for k,v in report.items():
            rep += f"({k}|{v[0]}|{v[1]}|{v[2]})" + "\n"
        return rep
    
    elif(selection=="8"):
        return "Good Bye"
        
class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        message = self.data.decode("utf-8")
        reply = choice(message)
        self.request.sendall(bytes(reply, "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    #For storing data into the tuples and dictonary and will do this before even starting server for the client.
    loadDataFile()

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()