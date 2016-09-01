# -*- coding: utf-8 -*-

import named_rows as nrows

class PBSTree:
    def __init__(self,plain,bob,single,indiv=[]):
        ' Note: Does not fully work; only works on six; use abcdef for 123456. '
        self._pbs = (plain,bob,single,indiv)

    def plain(self,row):
        plain, indiv = self._pbs[0], self._pbs[3]
        orow = []
        a,b,c,d,e,f = row[0], row[1], row[2], row[3], row[4], row[5]
        for cr in [plain] + indiv:
            for x in list(cr):
                orow += [eval(x)]
        return([nrows.Bellrow(orow)])

    def bob(self,row):
        bob, indiv = self._pbs[1], self._pbs[3]
        orow = []
        a,b,c,d,e,f = row[0], row[1], row[2], row[3], row[4], row[5]
        for cr in [bob] + indiv:
            for x in list(cr):
                orow += [eval(x)]
        return([nrows.Bellrow(orow)])

    def single(self,row):
        single, indiv = self._pbs[2], self._pbs[3]
        orow = []
        a,b,c,d,e,f = row[0], row[1], row[2], row[3], row[4], row[5]
        for cr in [single] + indiv:
            for x in list(cr):
                orow += [eval(x)]
        return([nrows.Bellrow(orow)])

    def tree(self, max_length=20, itrees=None, trueonly=True):
        nlen = max_length -1
        otrees = []
        if not itrees:
            itrees = [[[[nrows.Rounds(6)]],[],0]]
        if nlen < 1:
            return(itrees)
        for tree in itrees:
            if str(tree[0][0][-1]) == str(nrows.Rounds(6)) and tree[2]:
                if self._true(tree[0][0][1:]) or not trueonly:
                    print('New Path Complete:')
                    print('Length:\t\t'+str(tree[2]))
                    print('Pattern:\t'+(''.join(tree[1])))
                    print('True:\t\t'+str(self._true(tree[0][0][1:])))
            else:
                otrees.append([[tree[0][0]+self.plain(tree[0][0][-1])],
                              tree[1]+['P'],tree[2]+1])
                otrees.append([[tree[0][0]+self.bob(tree[0][0][-1])],
                              tree[1]+['B'],tree[2]+1])
                otrees.append([[tree[0][0]+self.single(tree[0][0][-1])],
                              tree[1]+['S'],tree[2]+1])
        self.tree(nlen, otrees)

    def _true(self,rows):
        eql, tl = [], []
        for i in rows:
            eql.append(str(i))
        for line in eql:
            if line in tl:
                return(False)
            tl += [line]
        return(True)
