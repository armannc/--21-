print("Қаржы шығындарын есептеу")
atauy = input("Шығынның атауы: ")
somasy = float(input("Сомасы (теңге): "))
korshetkish = float(input("Күтілетін табыс (теңге): "))
nat = korshetkish - somasy

if nat >= 0:
    print(f"{atauy} тиімді! Пайда: {nat} ₸")
else:
    print(f"{atauy} шығын! Залал: {abs(nat)} ₸")

print("\nАйлық шығындар тізімі")
s_sanaty = ["Тамақ", "Жол ақысы", "Коммуналка", "Тамақ", "Киім"]
print("Бастапқы тізім:", s_sanaty)
b_emsiz = list(set(s_sanaty))
print("Қайталанбайтын:", b_emsiz)
bjudjet = float(input("Жалпы бюджет енгіз (теңге): "))
ozgerm = tuple(["Жалпы бюджет", bjudjet])
print("Кортеж (өзгермейтін):", ozgerm)

print("\nМәтіннен іздеу")
ataular = ["тамақ", "жол ақысы", "коммуналка", "киім"]
izdeu = input("Қай санатты іздейсіз: ").lower()
if any(izdeu in a for a in ataular):
    print(f"'{izdeu}' санаты табылды!")
else:
    print(f"'{izdeu}' тізімде жоқ!")

print("\nШығындар базасы")
shygyn_dict = {
    "Тамақ": 60000,
    "Жол ақысы": 15000,
    "Коммуналка": 20000
}

for at, som in shygyn_dict.items():
    print(f"{at}: {som} ₸")

while True:
    print("\n1 – Шығын қосу\n2 – Барлығын көру\n3 – Шығу")
    tandau = input("Таңдау: ")
    if tandau == "1":
        at = input("Санат атауы: ")
        som = float(input("Сомасы: "))
        shygyn_dict[at] = som
    elif tandau == "2":
        for k, v in shygyn_dict.items():
            print(f"{k}: {v} ₸")
    elif tandau == "3":
        print("Бағдарлама аяқталды.")
        break
    else:
        print("Қате таңдау!")
