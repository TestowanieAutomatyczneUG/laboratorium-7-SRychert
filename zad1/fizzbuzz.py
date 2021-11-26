import unittest

class FizzBuzz:
    def play(self, number):
        '''
        >>> f = FizzBuzz()
        >>> f.play(5)
        '"Buzz"'

        >>> f.play(3)
        '"Fizz"'

        >>> f.play(15)
        '"FizzBuzz"'

        >>> f.play(17)
        '"17"'

        >>> f.play(0)
        '"FizzBuzz"'

        >>> f.play('3')
        Traceback (most recent call last):
        ...
        Exception: number must be int
        
        >>> f.play(-3)
        '"Fizz"'

        >>> f.play(-5)
        '"Buzz"'

        >>> f.play(-15)
        '"FizzBuzz"'

        >>> f.play(-17)
        '"-17"'

        >>> f.play(999)
        '"Fizz"'

        >>> f.play(15050)
        '"Buzz"'

        >>> f.play(3750)
        '"FizzBuzz"'

        '''

        if type(number) != int: raise Exception("number must be int")
        if (number % 15 == 0):
            return '"FizzBuzz"'
        elif number % 3 == 0:
            return '"Fizz"'
        elif number % 5 == 0:
            return '"Buzz"'
        else:
            return('"'+str(number)+'"')


if __name__ == "__main__":
  import doctest
  doctest.testmod()
