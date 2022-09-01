import string

vocals = "aeiou"

def getPart(word : string) -> string:
	word = word.lower()
	part = ""
	waitonvocal = ""
	vokalgroups = 0
	lastwasvocal = False
	for i in word[::-1]:
		if i in vocals:
			if vocalgroups < 2:

			lastwasvocal = True
		else:


words = ["Baum", "Traum", "singen", "klingen"]
for i in words:
	part = i.