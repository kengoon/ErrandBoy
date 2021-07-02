import time


def call_me_back(*args):
    """accepts and prints as when argument as possible"""
    print('Hello and welcome to Python\'s world oof programming')
    print('Welcome to the programming world, where we eat python (not the snake!!!) as food')
    print(args[1], args)


def the_timer(timer, callback=None):
    """the_timer(timer, callback) - argument timer contains the seconds you want the program to run and callback is the
    function you wish to callback."""
    if not callable(callback):
        raise NotImplementedError("'callback' is not a function")
    start_time = 0
    while True:
        callback('hi', 'hello')
        if start_time == timer:
            break
        time.sleep(1)  # argument taken is equal to the number of seconds the execution can be delayed
        start_time += 1


if __name__ == '__main__':
    the_timer(10, call_me_back)

