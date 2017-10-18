# -*- coding: utf-8 -*-

class Bellrow(tuple):
    def __init__(self, inobj, chars='0ETABCDFGHIJKLMNOPQRSUVWXYZ!"£$%^&*()-=_+[]{};:~,.<>'):
        self._inobj = inobj
        self._letters = chars
        self = tuple(inobj)

    def __str__(self):
        istr = ''
        inobj = self._inobj
        letters = self._letters
        for x in range(0, len( inobj ) ):
            c_obj = inobj[x]
            try:
                cobj = int(c_obj)
                success = True
            except ValueError:
                success = False
            if success and cobj > 9:
                if cobj < len(letters) + 10:
                    c_obj = letters[cobj-10]
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

        if self._pn:
            if rowl % 2:
                raise IndexError("Odd number of bells can't swap all bells")

        pass # not implemented
