# -*- coding: utf-8 -*-

"""This file contains definitions for named rows"""

from bellrow import Bellrow

def Rounds(n_bells):
    return( Bellrow( range(1, n_bells+1) ) )

def Backrounds(n_bells):
    return( Bellrow( range(n_bells, 0, -1) ) )

def Queens(n_bells):
    if n_bells % 2 != 0:
        return( Bellrow( range(2,n_bells+1,2) + range(1,n_bells+1,2) ) )
    return( Bellrow( range(1,n_bells+1,2) + range(2,n_bells+1,2) ) )

def Kings(n_bells):
    if n_bells % 2 != 0:
        return( Bellrow( range(n_bells-1,0,-2) + range(1,n_bells+1,2) ) )
    return( Bellrow( range(n_bells-1,0,-2) + range(2,n_bells+1,2) ) )

def Tittums(n_bells):
    ranges, result = [range(1, int(n_bells/2) +1),
                      range(int(n_bells/2) +1, n_bells+1)], []
    if n_bells % 2 != 0:
        ranges.reverse()
    for x in range(0, int(round(n_bells/2.0, 0))):
        result.append( ranges[0][x] )
        try:
            result.append( ranges[1][x] )
        except IndexError:
            nothing = 'nothing' # Odd number of bells
    return( Bellrow(result) )
