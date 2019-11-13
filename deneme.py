vize = int(input("Vize Notu :"))
final = int(input("Final Notu :"))
ortalama = (vize * 0.4) + (final * 0.6)  # vizenin %40 final %60 olarak al?nd?
if (ortalama >= 85):
    print("Harf notunuz : AA0")
elif (ortalama >= 70 and ortalama < 85):
    print("Harf notunuz : BA")
elif (ortalama >= 60 and ortalama < 70):
    print("Harf notunuz : BB")
elif (ortalama >= 45 and ortalama < 60):
    print("Harf notunuz : CB")
elif (ortalama >= 0 and ortalama < 45):
    print("Harf notunuz : FF")

demet = ("Python", "Java", "Ruby", "JavaScript")
    print(demet)
