from constPS import * #-
import threading

def goodbye():
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
       ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
       "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `")
  print("\n                GOODBYE! HOPE TO SEE YOU AGAIN\n")
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
      ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
      "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")

def welcome():
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
       ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
       "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `")
  print("\n                WELCOME TO THE LIST MANAGER!\n" +
        "                   WE ARE CONFIGURING YOUR CHAT\n")
  print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.\n" +
      ":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\n" +
      "'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      `\n\n")
  return menu()

def menu():
  return input("CHOOSE THE OPTION THAT BEST FITS YOUR NEEDS:\n1 - PRINT THE ENTIRE LIST.\n2 - SEARCH FOR A VALUE IN THE LIST.\n3 - ADD A VALUE TO THE LIST.\n" +
              "4 - APPEND ANOTHER LIST TO THE LIST. \n5 - REMOVE A VALUE FROM THE LIST. \n6 - SORT THE LIST \n0 - EXIT THE LIST MANAGER\n")

class RecHandler

def run():
    welcome()
    x = menu()

    while(x != 0):
        x = menu()
    goodbye()

if __name__ == '__main__':
    run()    