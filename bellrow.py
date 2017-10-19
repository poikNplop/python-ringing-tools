# -*- coding: utf-8 -*-

class Bellrow(tuple):
    def __init__(self, inobj, chars='1234567890ETABCDFGHIJKLMNOPQRSUVWXYZ'):
        self._inobj = inobj
        self._letters = chars
        self = tuple(inobj)

    def __str__(self):
        istr = ''
        inobj = self._inobj
        letters = self._letters
        for x in range(0, len( inobj ) ):
            c_obj = inobj[x]
            if cobj < len(letters):
                c_obj = letters[cobj]
            else:
                c_obj = '#'
            istr += str(c_obj)
        return(istr)

class Rowchange:
    def __init__(self, pn, chars='1234567890ETABCDF', nochars="x-"):
        self._pn = pn
        self._chars = [chars, nochars]

    def swap(self, inrow):
        row = str(inrow)
        rowl = len(row)
        outrow = ""
        chars = self._chars

        for char in chars[1]:
            if char in self._pn:
                if rowl % 2:
                    raise IndexError("Odd number of bells can't swap all bells")

        swapping = False
        for n in range(0, rowl):
            bell = chars[0][n]
            if bell in self._pn:
                if swapping:
                    raise IndexError("Odd number of bells between two non-swapping bells")
                outrow += bell
            else:
                if swapping:
                    outrow += chars[0][n] + chars[0][n-1]
                else:
                    swapping = True

        if swapping:
            raise IndexError("Odd number of bells after non-swapping bell")

        return(Bellrow(outrow))
