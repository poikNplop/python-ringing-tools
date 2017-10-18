# -*- encoding: utf-8 -*-

from bellrow import Bellrow, Rowchange

class PlaceNotationParser:
    def __init__(self, swapbellchars="1234567890ETABCD", swapnochars="x-",
                 splitchars=".", palindromechars=",", casesensitive=False):
        self._cases = casesensitive
        self._chardata = [self._checkcases(swapbellchars),
                          self._checkcases(swapnochars),
                          self._checkcases(splitchars),
                          self._checkcases(palindromechars)]

    def _checkcases(self, text):
        if self._cases:
            return(text)
        else:
            return(text.lower())

    def parse(self, bells=6, pn=["16","-"], bob="14", single="1234"):
        bob, single = self._checkcases(bob), self._checkcases(single)
        if type(pn) == list:
            pnlist = pn
        else:
            pass # not implemented
        
        outlist = []
        for swap in pnlist:
            outlist += [Rowchange(self._checkcases(swap),
                                  chars= self._chardata[0],
                                  nochars= self._chardata[1])]
            
        outbob = [Rowchange(bob, chars= self._chardata[0],
                  nochars= self._chardata[1])]
        outsingle = [Rowchange(single, chars= self._chardata[0],
                               nochars= self._chardata[1])]

        return(outlist, outbob, outsingle)
