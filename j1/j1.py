import string

vocals = "aeiou"

def getPart(word : string) -> string:
	word = word.lower()
	part = ""
	vokalgroups = 0
	lastwasvocal = False
	for i in word[::-1]:
		if i in vocals:
			


words = ["Baum", "Traum", "singen", "klingen"]
for i in words:
	part = i.	