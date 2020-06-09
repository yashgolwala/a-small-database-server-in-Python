import socket
import sys

HOST, PORT = "localhost", 9999
data = "".join(sys.argv[1:])

def menu():
    print("\nPython DB Menu\n")
    print("1. Find customer")        
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit")
    select = input("\nSelect: ")
    return select

def inputNumber(text):
  while True:
    try:
       userInput = str(int(input(text)))
    except ValueError:
       print("Not a number! Try again.")
       continue
    else:
       return userInput 
       break 

def run():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        
        sock.connect((HOST, PORT))
        choice = menu()
        if(choice=="1"):
            name = input("Enter Name ").capitalize().strip(" ")
            sock.sendall(bytes(data+choice+"|"+name, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()
                
                
        elif(choice=="2"):
            name = input("Enter Name ").capitalize().strip(" ")
            age = inputNumber("Enter age ")
            address = input("Enter address ").title()
            phone = input("Enter phone ")
            sock.sendall(bytes(data+choice+"|"+name+"|"+age+"|"+address+"|"+phone+"\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()

        elif(choice=="3"):
            name = input("Enter Name ").capitalize().strip(" ")
            sock.sendall(bytes(data+choice+"|"+name, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()

        elif(choice=="4"):
            name = input("Enter Name ").capitalize().strip(" ")
            age= inputNumber("Enter age ")
            sock.sendall(bytes(data+choice+"|"+name+"|"+age, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()
            
        elif(choice=="5"):
            name = input("Enter Name ").capitalize().strip(" ")
            address = input("Enter address ").title()
            sock.sendall(bytes(data+choice+"|"+name+"|"+address, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()
            
        elif(choice=="6"):
            name = input("Enter Name ").capitalize().strip(" ")
            phone = input("Enter Phone ")
            sock.sendall(bytes(data+choice+"|"+name+"|"+phone, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()
            
        elif(choice=="7"):
            sock.sendall(bytes(data+choice, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            run()

        elif(choice=="8"):
            sock.sendall(bytes(data+choice, "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))
            sock.close()

        else:
            print("Not a valid selection \nSelect again!")
            run()

run()