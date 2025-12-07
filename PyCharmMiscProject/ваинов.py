import numpy as np
import matplotlib.pyplot as plt
import sqlite3
print("Қаржы шығындарын есептеу")

def create_table():
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            amount REAL
        )
    """)
    conn.commit()
    conn.close()
    print("Кесте дайын (expenses).")

create_table()
def db_insert(name, amount):
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO expenses(name, amount) VALUES(?,?)", (name, amount))
    conn.commit()
    conn.close()
    print("Мәлімет базаға сақталды!")

def total_sum():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    total = cur.fetchone()[0]
    conn.close()
    return total if total else 0

def total_sum():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM expenses")
    total = cur.fetchone()[0]
    conn.close()
    return total if total else 0

def db_show():
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM expenses")
    rows=cur.fetchall()
    conn.close()

    print("\n--- SQLite мәліметтері ---")
    if not rows:
        print("Базада ештеңе жоқ.")
    else:
        for r in rows:
            print(f"ID: {r[0]} | Санат: {r[1]} | Сома: {r[2]} ₸")
    print()

class Expense:
    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    def info(self):
        return f"Санат: {self.name} | Сома: {self.amount} ₸"

class BigExpense(Expense):
    def __init__(self,name,amount,limit):
        super().__init__(name,amount)
        self.limit=limit
    def is_big(self):
        return self.amount>=self.limit
    def info(self):
        base=super().info()
        tip="ҮЛКЕН ШЫҒЫН!" if self.is_big() else "Қалыпты шығын"
        return base+f" | Лимит: {self.limit} ₸ | {tip}"

def add_rec(n, amt):
    import sqlite3
    conn=sqlite3.connect("expenses.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO expenses(name, amount) VALUES(?,?)", (n, amt))
    conn.commit()
    conn.close()
    print(f"'{n}' шығыны базаға жазылды ({amt} ₸)")

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

db={"Тамақ":60000,"Жол ақысы":15000,"Коммуналка":20000}

cats=["Тамақ","Жол ақысы","Коммуналка","Тамақ","Киім"]
print("Бастапқы тізім:",cats)
uniq=list(set(cats))
print("Қайталанбайтын:",uniq)

try:
    budget=float(input("Жалпы бюджет (₸): "))
    tpl=("Жалпы бюджет",budget)
    print("Кортеж (өзгермейтін):",tpl)
except ValueError:
    print("Қате: сан енгізіңіз!")

lower_cats=["тамақ","жол ақысы","коммуналка","киім"]
search=input("Қай санатты іздейсіз: ").lower()
if any(search in a for a in lower_cats):
    print(f"'{search}' санаты табылды!")
else:
    print(f"'{search}' тізімде жоқ!")

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
    print("9–Статистика (NumPy)")
    print("10–График шығару (Matplotlib)")
    print("11–OOP (класс & мұрагерлік)")
    print("12–SQLite дерекқоры")
    ch=input("Таңдау: ")

    try:
        if ch == "1":
            n=input("Санат атауы: ")
            amt = float(input("Сомасы: "))
            db_insert(n, amt)

        elif ch == "2":
            db_show()

        elif ch == "3":
            n = input("Ізделетін санат: ")
            search_sql(n)

        elif ch == "4":
            _id = int(input("Өшірілетін ID: "))
            delete_sql(_id)

        elif ch == "5":
            print("Барлық шығын:", total_sum(), "₸")

        elif ch=="6":
            with open("shygyn.csv","w",encoding="utf-8") as f:
                for k,v in db.items():
                    f.write(f"{k},{v}\n")
            print("Мәліметтер файлға сақталды")

        elif ch=="7":
            try:
                with open("shygyn.csv","r",encoding="utf-8") as f:
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("Файл табылмады!")

        elif ch=="8":
            print("Бағдарлама аяқталды.")
            break

        elif ch=="9":
            vals=np.array(list(db.values()))
            print("Барлық сома:",np.sum(vals))
            print("Орташа шығын:",np.mean(vals))
            print("Максимум:",np.max(vals))
            print("Минимум:",np.min(vals))

        elif ch=="10":
            categories=list(db.keys())
            values=list(db.values())
            plt.figure(figsize=(8,5))
            plt.bar(categories,values)
            plt.title("Айлық шығындар графигі")
            plt.xlabel("Санаттар")
            plt.ylabel("Сома (₸)")
            plt.grid(True,alpha=0.3)
            plt.show()

        elif ch=="11":
            print("\nOOP көрсету:")
            name=input("Санат атауы: ")
            amount=float(input("Сомасы: "))
            big=input("Үлкен шығын ба? (иә/жоқ): ").lower()
            if big=="иә":
                limit=float(input("Лимит: "))
                obj=BigExpense(name,amount,limit)
            else:
                obj=Expense(name,amount)
            print("\nОбъект туралы ақпарат:")
            print(obj.info())
        elif ch == "12":
            print("\nSQLite дерекқоры:")
            print("1 – Кесте құру")
            print("2 – Мәліметті базаға қосу")
            print("3 – Базадан оқу")

            s = input("Таңдау: ")

            if s == "1":
                create_table()
            elif s == "2":
                name = input("Санат атауы: ")
                amount = float(input("Сома: "))
                db_insert(name, amount)
            elif s == "3":
                db_show()
            else:
                print("Қате таңдау!")

        else:
            print("Қате таңдау! 1–11 аралығында нөмір енгізіңіз.")

    except ValueError:
        print("Қате: сан енгізіңіз!")
    except Exception as e:
        print("Күтпеген қате:",e)
