# Created by Leon Hunter at 12:10 PM 12/08/2020
class Filterer(object):
    def remove_characters(self, string_to_remove_from, characters_to_remove):

        remove_list = [character for character in characters_to_remove]
        rstring = ""
        for char in string_to_remove_from:
            if char not in remove_list:
                rstring += char

        return rstring

    def remove_vowels(self, string_to_remove_from):
        vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        rstring = ""
        for char in string_to_remove_from:
            if char not in vowel_list:
                rstring += char

        return rstring

    def remove_consonants(self, string_to_remove_from):
        constants_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', \
                      'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', \
                      'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', \
                      'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
                      ]
        rstring = ""
        for char in string_to_remove_from:
            if char not in constants_list:
                rstring += char

        return rstring
