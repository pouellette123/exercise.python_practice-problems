# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        if step==0:
            return [0]
        else:
            return [num for num in range(start,stop+1,step)]
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
        '''

    def get_even_list(self, start, stop, step):
        if step==0:
            return [0]
        else:
            return [num for num in range(start, stop+1, step) if num%2 == 0]
        ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are divisible by 2
        '''

    def get_odd_list(self, start, stop, step):
        if step == 0:
            return []
        else:
            return [num for num in range(start, stop+1, step) if num % 2 != 0]
    ''' TODO - Implement solution
        Given 3 integers,
            `start`, `stop`, and `step`
        return a list of all integers
            between `start`,
            incrementing by `step`,
            up to and including `stop`
            and are not divisible by 2
        '''
