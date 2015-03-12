# -*- coding: utf-8 -*-
 
import unicodedata

class Utiles(object):
    """docstring for ClassName"""
    def __init__(self):
        self=self
        
    def supprime_accent(self, ligne):
        chaine = unicodedata.normalize('NFKD', ligne).encode('ASCII', 'ignore')
        return chaine


    def cleanString(self,s):
        if isinstance(s,str):
            b=s.encode("UTF-8")
            s = str(b,"UTF-8","replace")
            s=unicodedata.normalize('NFD',s)
        return s.encode('ascii','ignore')