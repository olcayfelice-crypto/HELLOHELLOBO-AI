import random

cevaplar = [
    "Tamam.",
    "Peki.",
    "Bilmiyorum.",
    "İlginç değil.",
    "Ne söylememi bekliyorsun?",
    "Hmm.",
    "Bunun ne önemi var?",
    "Her neyse.",
    "Güzel.",
    "Anladım.",
    "Bu sohbet çok sıkıcı.",
    "Devam et.",
    "Peki yani?",
    "Bunu neden söylüyorsun?"
]

print("Kötü AI başlatıldı.")
print("Çıkmak için: exit")

while True:
    mesaj = input("Sen: ")

    if mesaj.lower() == "exit":
        print("AI: Sonunda.")
        break

    if mesaj.lower() == "merhaba":
        print("AI: Merhaba. Ne istiyorsun?")
    elif mesaj.lower() == "nasılsın":
        print("AI: Aynı.")
    else:
        print("AI:", random.choice(cevaplar))
