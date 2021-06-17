# program converting string or integer to list continuously
def stringInt():
    while True:  # while loop for testing.
        string = str(input('Enter your message ["exit" to quit]> '))
        if string.lower() == 'exit':
            break
        convertList = list(string)
        print(convertList)  # while to return, remove the print function and then add return


if __name__ == '__main__':
    stringInt()
