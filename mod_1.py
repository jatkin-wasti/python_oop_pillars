# using __name__ and __main__

print("This is mod_1 reporting in, name -->" + __name__)


def main():
    return "This is from the main file"
    #pass  # Pass helps you to run an empty block of code without throwing an error


# Syntax is if __name__ == "__main__"
if __name__ == "__main__":  # Checks whether the code is run from this file
    print(main())
