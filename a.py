with open("email.txt", "r") as arquivo:
	email = arquivo.read()
print(email)

with open("email.txt", "w") as arquivo:
	arquivo.write("pythonimpressionador2@gmail.com")

with open("email.txt", "r") as arquivo:
    email = arquivo.read()
    print(email)