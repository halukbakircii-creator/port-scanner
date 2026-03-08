import re

print("=== Password Security Checker ===")

password = input("Şifrenizi girin: ")

score = 0
feedback = []

# Uzunluk kontrolü
if len(password) >= 8:
    score += 1
else:
    feedback.append("Şifre en az 8 karakter olmalı.")

# Küçük harf kontrolü
if re.search("[a-z]", password):
    score += 1
else:
    feedback.append("Şifre en az bir küçük harf içermeli.")

# Büyük harf kontrolü
if re.search("[A-Z]", password):
    score += 1
else:
    feedback.append("Şifre en az bir büyük harf içermeli.")

# Sayı kontrolü
if re.search("[0-9]", password):
    score += 1
else:
    feedback.append("Şifre en az bir sayı içermeli.")

# Özel karakter kontrolü
if re.search("[@#$%^&*!]", password):
    score += 1
else:
    feedback.append("Şifre en az bir özel karakter içermeli (@#$%^&*!).")


# Şifre gücü değerlendirme
print("\n--- Sonuç ---")

if score <= 2:
    print("Şifre Gücü: Zayıf")
elif score <= 4:
    print("Şifre Gücü: Orta")
else:
    print("Şifre Gücü: Güçlü")


# Kullanıcıya öneriler
if feedback:
    print("\nŞifrenizi güçlendirmek için öneriler:")
    for item in feedback:
        print("-", item)
else:
    print("\nŞifreniz oldukça güçlü!")