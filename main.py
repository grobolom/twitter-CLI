import sys
import readchar

def main():
    print('fetch data from the api')
    print('loop')
    print('   shove data + action into reducer to get a visual representation')
    print('   push it into a renderer to get an 80x40 printout of it')
    print('   wait for commands from the user')

    key = 0
    while key != 27:
        key = ord(readchar.readchar())
        print(key)

if __name__ == "__main__":
    main()
