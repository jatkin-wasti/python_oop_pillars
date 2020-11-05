import mod_1  # When mod_1 is imported it runs the code and outputs the print line with the name
# mod_1 instead of __main__ as it is run from an imported file so the __name__ is the same as the file name
print("This is mod_2 reporting in, name --> " + __name__)
