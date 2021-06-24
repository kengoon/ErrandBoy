import time


def hello():
    print('Hello and welcome to Python\'s world oof programming')


def timer():
    while True:
        hello()
        time.sleep(2)  # argument taken is equal to the number of seconds the execution can be delayed


if __name__ == '__main__':
    timer()

