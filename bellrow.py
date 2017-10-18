# -*- coding: utf-8 -*-

class Bellrow(tuple):
    def __init__(self, inobj):
        self._inobj = inobj
        self._letters = '0ETABCDFGHIJKLMNOPQRSUVWXYZ!"£$%^&*()-=_+[]{};:~,.<>'
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
