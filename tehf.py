print("Қаржы шығындарын есептеу")
def add_rec(data,n,amt):
    data[n]=amt
    print(f"'{n}' сәтті қосылды! ({amt} ₸)")
def del_rec(data,n):
    if n in data:
        del data[n]
        print(f"'{n}' өшірілді!")
    else:
        print(f"'{n}' табылмады!")
def search_rec(data,n):
    if n in data:
        print(f"{n}: {data[n]} ₸ табылды!")
    else:
        print(f"{n} тізімде жоқ!")
def rec_sum(vals):
    if not vals:
        return 0
    return vals[0]+rec_sum(vals[1:])
try:
    n=input("Шығын атауы: ")
    amt=float(input("Сомасы (₸): "))
    exp=float(input("Күтілетін табыс (₸): "))
    diff=exp-amt
    if diff>=0:
        print(f"{n} тиімді! Пайда: {diff} ₸")
    else:
        print(f"{n} шығын! Залал: {abs(diff)} ₸")
except ValueError:
    print("Қате: дұрыс сан енгізіңіз!")
print("\nАйлық шығындар тізімі")
cats=["Тамақ","Жол ақысы","Коммуналка","Тамақ","Киім"]
print("Бастапқы тізім:",cats)
uniq=list(set(cats))
print("Қайталанбайтын:",uniq)
try:
    budget=float(input("Жалпы бюджет (₸): "))
    tpl=tuple(["Жалпы бюджет",budget])
    print("Кортеж (өзгермейтін):",tpl)
except ValueError:
    print("Қате: сан енгізіңіз!")
print("\nМәтіннен іздеу")
lower_cats=["тамақ","жол ақысы","коммуналка","киім"]
search=input("Қай санатты іздейсіз: ").lower()
if any(search in a for a in lower_cats):
    print(f"'{search}' санаты табылды!")
else:
    print(f"'{search}' тізімде жоқ!")
print("\nШығындар базасы")
db={"Тамақ":60000,"Жол ақысы":15000,"Коммуналка":20000}
for k,v in db.items():
    print(f"{k}: {v} ₸")
while True:
    print("\nҚосымша мәзір:")
    print("1–Шығын қосу")
    print("2–Барлығын көру")
    print("3–Іздеу")
    print("4–Өшіру")
    print("5–Барлық соманы қосу")
    print("6–Файлға жазу")
    print("7–Файлдан оқу")
    print("8–Шығу")
    ch=input("Таңдау: ")
    try:
        if ch=="1":
            n=input("Санат атауы: ")
            amt=float(input("Сомасы: "))
            add_rec(db,n,amt)
        elif ch=="2":
            print("\nБарлық шығындар:")
            for k,v in db.items():
                print(f"{k}: {v} ₸")
        elif ch=="3":
            n=input("Ізделетін санат: ")
            search_rec(db,n)
        elif ch=="4":
            n=input("Өшірілетін санат: ")
            del_rec(db,n)
        elif ch=="5":
            total=rec_sum(list(db.values()))
            print(f"Барлық шығындардың қосындысы: {total} ₸")
        elif ch=="6":
            with open("shygyn.csv","w",encoding="utf-8") as f:
                for k,v in db.items():
                    f.write(f"{k},{v}\n")
            print("Мәліметтер файлға сақталды")
        elif ch=="7":
            try:
                with open("shygyn.csv","r",encoding="utf-8") as f:
                    print("\nФайл мазмұны:")
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("Файл табылмады!")
        elif ch=="8":
            print("Бағдарлама аяқталды.")
            break
        else:
            print("Қате таңдау! 1–8 аралығында нөмір енгізіңіз.")
    except ValueError:
        print("Қате: сан енгізіңіз!")
    except ZeroDivisionError:
        print("Қате: нөлге бөлуге болмайды!")
    except Exception as e:
        print("Күтпеген қате:",e)
