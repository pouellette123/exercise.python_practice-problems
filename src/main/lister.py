# Created by Leon Hunter at 12:10 PM 12/08/2020
class Lister(object):
    def get_integer_list(self, start, stop, step):
        if step==0:
            return [0]
        else:
            return [num for num in range(start,stop+1,step)]

    def get_even_list(self, start, stop, step):
        if step==0:
            return [0]
        else:
            return [num for num in range(start, stop+1, step) if num%2 == 0]

    def get_odd_list(self, start, stop, step):
        if step == 0:
            return []
        else:
            return [num for num in range(start, stop+1, step) if num % 2 != 0]