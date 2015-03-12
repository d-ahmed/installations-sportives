import unicodedata

def cleanString(s):
	if isinstance(s,str):
		b=s.encode("utf-8")
		s = str(b,"utf-8","replace")
		s=unicodedata.normalize('NFD',s)
	return s.encode('ascii','ignore')