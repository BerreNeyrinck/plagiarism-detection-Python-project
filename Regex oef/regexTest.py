import re

string1 = "apple, banana, avocado, cherry, apricot"
S1 = re.findall(r"\ba[a-z]*", string1)
print(S1)

string2 = "Er zijn 12 maanden in een jaar, 24 uur in een dag."
S2 = re.findall(r"\d[1-99]", string2)
print(S2)

string3 = "I am walking while singing and eating."
S3 = re.findall(r"\w[a-z]*ing", string3)
print(S3)

string4 = "Alice wonders everywhere under the sky"
S4 = re.findall(r"\b[aeiouAEIOU][a-z]*", string4)
print(S4)

string5 = "Mijn email is voorbeeld@voorbeeld.com en info@test.be."
S5 = re.findall(r"\b[a-z]*@[a-z]*.[a-z]*", string5)
print(S5)