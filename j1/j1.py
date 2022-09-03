import string

vocals = "aeiouüäö"

# generate a list containing parts which are consonants or vocals
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

# generate the part of the word which will be the rime part
# this part will be checked againt the other rime parts
def getrimepart(parts): # take in list of word
	rime = []
	vocalparts = 0

	# add parts until 2 vocal parts have been added
	# start from the end
	for i in parts[::-1]:
		if vocalparts > 1:
			break
		if i[0] in vocals:
			vocalparts += 1
			rime.append(i)
		else:
			rime.append(i)

	# turn order, so it is right again
	rime = rime[::-1]
	# remove leading consonant part if present
	if rime[0][0] not in vocals:
		rime.remove(rime[0])
	# make it to string
	rime = "".join(rime)
	return rime

# check rule 2 and 3
def checkrime(rimepart, fullword):
	# check if group is large enough
	if (len(rimepart) + len(fullword) // 2) < len(fullword): # half of word is ok
		return False

	# check if it is the whole word
	if rimepart == fullword:
		return False

	return True

# read words from file
def getwords(filename):
	# read data and split at newline
	with open(filename) as file:
		data = file.read()
		lines = data.split("\n")
		# remove empty strings
		while "" in lines:
			lines.remove("")
		return lines

# main program
for i in range(3): # reimerei(i).txt
	#remove duplicates from words
	print(f"----reimerei{i}.txt----")
	wordsbase = list(dict.fromkeys(getwords(f"reimerei{i}.txt")))
	words = []

	# generate rime parts and list structure
	for word in wordsbase:
		rime = getrimepart(splitvocskons(word.lower()))
		if checkrime(rime, word.lower()):
			words.append([word, rime, []])

	# check rime parts against each other
	for i in range(len(words)):
		j = i + 1
		while(j < len(words)):
			if words[i][1] == words[j][1]:
				words[i][2].append(words[j][0])
			j += 1

	for i in words:
		for j in i[2]:
			print(i[0],":",j)