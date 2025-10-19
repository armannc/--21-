Бағдарлама атауы
print("Qarzhy shyǵyndaryn esepteý")

Мәліметтерді енгізу
atauy = input("Shyǵyn ataýy: ")
somasy = float(input("Somasy (teńge): "))
korshetkish = float(input("Kútiletin tabys (teńge): "))

Пайдаланушыдан шығынның атауын, сомасын және күтілетін табысты сұрап нәтижесін шығару
nat = korshetkish - somasy
if nat >= 0:
    print(f"{atauy} tiimdi! Paıda: {nat} ₸")
else:
    print(f"{atauy} shyǵyn! Zalal: {abs(nat)} ₸")

Табыс пен шығын айырмасын есептейді
Егер айырма оң болса — пайда, теріс болса — залал деп көрсетеді
 Айлық шығындар тізімі
s_sanaty = ["Tamaq", "Jol aqysy", "Kommunalka", "Tamaq", "Kiim"]
print("Bastapqy tizim:", s_sanaty)
b_emsiz = list(set(s_sanaty))
print("Qaıtalanbaıtyn:", b_emsiz)

Шығындар тізімін жасайды
 Бюджет пен кортеж
bjudjet = float(input("Jalpy bjudjetti engiz (teńge): "))
ozgerm = tuple(["Jalpy bjudjet", bjudjet])
print("Kortej (ózgermeıtin):", ozgerm)

Пайдаланушы жалпы бюджетті енгізеді
Ол мәлімет өзгермейтін tuple түрінде сақталады
Мәтіндік іздеу
ataular = ["tamaq", "jol aqysy", "kommunalka", "kiim"]
izdeu = input("Qaı sanatty izdeısiz: ").lower()
if any(izdeu in a for a in ataular):
    print(f"'{izdeu}' sanat tabyldy!")
else:
    print(f"'{izdeu}' tizimde joq!")

Пайдаланушы іздегісі келген санатты енгізеді
Егер ол тізімде болса — табылғаны туралы хабарлама шығады
Шығындар базасы (сөздік)
shygyn_dict = {
    "Tamaq": 60000,
    "Jol aqysy": 15000,
    "Kommunalka": 20000
}

for at, som in shygyn_dict.items():
    print(f"{at}: {som} ₸")

Барлық категориялар мен олардың сомаларын dict түрінде сақтап, экранға шығарады
Бағдарлама мәзірі (while циклі)
while True:
    print("\n1 – Shyǵyn qosy\n2 – Barlyǵyn kóru\n3 – Shyǵý")
    tandau = input("Tańdaý: ")

Мәзір арқылы үш іс-әрекет орындалады:
1 – жаңа шығын қосу
2 – барлық тізімді көру
3 – бағдарламадан шығу

Таңдау әрекеттері
if tandau == "1":
    at = input("Sanat ataýy: ")
    som = float(input("Somasy: "))
    shygyn_dict[at] = som


Жаңа категория мен соманы сөздікке қосады

elif tandau == "2":
    for k, v in shygyn_dict.items():
        print(f"{k}: {v} ₸")

Барлық сақталған мәліметті көрсетеді

elif tandau == "3":
    print("Baǵdarlama aıaqtaldy.")
    break

Бағдарламаны тоқтатады

else:
    print("Qate tańdaý!")

Қате таңдау енгізілсе, ескерту береді
