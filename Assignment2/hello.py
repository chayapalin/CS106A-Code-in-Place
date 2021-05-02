"""
File: hello.py
------------------
Prompts user for their name and then says hello!
"""


def main():
    user_name = input("What is your name? ")
    print("Hello " + user_name + "!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
