"""
I have a class called Time, and I need to implement a Frequency class. How can I implement dividing ints or floats by an instance of Time to get an instance of Frequency ?
https://stackoverflow.com/questions/44970692/dividing-a-number-by-instances-of-my-class-in-python
"""


class Time(object):
    """
    This is an example of the solution. However, python 2.7 doesn't support these 2 functions.
    """
    def __init__(self, period):
        self.period = period

    def __truediv__(self, other):
        return self.period / other

    def __rtruediv__(self, other):
        return other / self.period


if __name__ == "__main__":
    time = Time(10)
    print(time / 10)
    print(100 / time)