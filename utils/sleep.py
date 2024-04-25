import random
import time


def sleep(min: int = 2, max: int = 5):
    """
    This function pauses the execution of the program
    for a random amount of time between 2 and 5 seconds.
    """
    sleep_time = random.uniform(min, max)
    time.sleep(sleep_time)
