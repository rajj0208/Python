#String is immputable
str1 = "Raj Jaiswal"
print(str1.upper(), str1.lower())

str2 = "  Raj Jaiswal   "
print(str2.strip())

str3 = "raj 8"
print(str3.rstrip("8"))

str4 = "Potato is not a Potato"
print(str4.replace("P", "T"))

str5 = "He is great guy and is doing well"
print(str5.index("is"))