import string

vocals = "aeiou"

# generate a list containing parts which are consonants or strings
def splitvocskons(word : string) -> string:
	parts = []
	part = ""
	for i in word:
		if part == "": # needed so no indexerror
			part = i
		else:
			# check what type it is
			# then what the last letter was
			# and either start new or append
			if i in vocals:
				if part[-1] in vocals:
					part += i
				else:
					parts.append(part)
					part = i 
			else:
				if part[-1] in vocals:
					parts.append(part)
					part = i
				else:
					part += i
	parts.append(part) # append last part

	return parts

# words = ["Baum", "Traum", "singen", "klingen"]
# for i in words:
# 	part = i.
for i in words:
	print(splitvocskons("Baum"))