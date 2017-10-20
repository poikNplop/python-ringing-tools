# -*- encoding: utf-8 -*-

from bellrow import Bellrow, Rowchange
from place_notation_parser import PlaceNotationParser

class BaseMethod:
    def __init__(self, bells, pn, bob, single, pnparser=PlaceNotationParser):
        self._parser = pnparser()
        self.changes = self._parser.parse(bells, pn, bob, single)

    def update(self, bells, pn, bob, single):
        self.changes = self._parser.parse(bells, pn, bob, single)

    def getchanges(self, ending=0):
        # ending 0: all [default]
        #        1: plain
        #        2: bob
        #        3: single
        
        if ending < 1 or ending > 3: # all
            return(self.changes)
        
        output = self.changes[0]
        
        if ending == 2:
            output[-1] = self.changes[1]
        elif ending == 3:
            output[-1] = self.changes[2]

        return(output)
