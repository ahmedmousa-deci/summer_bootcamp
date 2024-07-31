from termcolor import colored, cprint
import re
import getpass
import os
from session import session
import keyboard as k


cprint("░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░████████╗██████╗░██╗██████╗░██╗░░░░░███████╗  ███╗░░░███╗", color="yellow")
cprint("░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗╚══██╔══╝██╔══██╗██║██╔══██╗██║░░░░░██╔════╝  ████╗░████║", color="yellow")
cprint("░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║░░░██║░░░██████╔╝██║██████╔╝██║░░░░░█████╗░░  ██╔████╔██║", color="yellow")
cprint("░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║░░░██║░░░██╔══██╗██║██╔═══╝░██║░░░░░██╔══╝░░  ██║╚██╔╝██║", color="yellow")
cprint("░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝░░░██║░░░██║░░██║██║██║░░░░░███████╗███████╗  ██║░╚═╝░██║", color="yellow")
cprint("░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═╝░░░░░╚══════╝╚══════╝  ╚═╝░░░░░╚═╝", color="yellow")


print("Sign up")

while True:
    name = colored(input("Enter you name: ").strip(), "green")
    if name == "":
        print("empty input")
    else:
        break

while True:
    email = input("enter email: ").strip()
    if email == "":
        print("Empty input")
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("not vaild")
    else:
        break


while True:
    password = getpass.getpass("Enter your password: ").strip()
    if password == "":
        print("empty")
    elif len(password) < 8:
        print("to short")
    else:
        break


print(f"ok {name}, you have signed up")


# edit account

os.system("cls")


cprint("██╗░░██╗░█████╗░███╗░░░███╗███████╗", "cyan")
cprint("██║░░██║██╔══██╗████╗░████║██╔════╝", "cyan")
cprint("███████║██║░░██║██╔████╔██║█████╗░░", "cyan")
cprint("██╔══██║██║░░██║██║╚██╔╝██║██╔══╝░░", "cyan")
cprint("██║░░██║╚█████╔╝██║░╚═╝░██║███████╗", "cyan")
cprint("╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝", "cyan")


print("1.Edit Account")
print("2.Start session")
cprint("Enter q to exit", "red")
print("Enter 1, 2 or " + colored("Q", "red") + " to " + colored("exit", "red") + ".")
while True:
    if k.is_pressed("q"):
        break
    if k.is_pressed("1"):
        break
    if k.is_pressed("2"):
        session()
