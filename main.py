toprow = ")!@#$%^&*("

with open('message') as mdata:
	message = mdata.read()

decoded = ""
for word in message.split(':::'):
	if word == '':
		continue
	decodedword = ''
	for letter in word.split(':'):
		number = ''
		for part in letter:
			number += str(toprow.index(part))
		decodedword += chr(64+int(number))
	decoded += decodedword + " "

print(decoded)

a = input('To encode > ').upper()
encoded = ''
for x in a.split():
	for letter in x:
		num = str(ord(letter)-64)
		for part in num:
			encoded += toprow[int(part)]
		encoded += ":"
	encoded += ":::"

encoded = ":::" + encoded.replace('::::',':::')
with open('encoded', 'w+') as file:
	file.write(encoded)