import sqlite3
import numpy as np
import matplotlib.pyplot as plt

print("Қаржы шығындарын есептеу")

class Record:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def info(self):
        return f"{self.name}: {self.amount} ₸"

class BigRecord(Record):
    def __init__(self, name, amount, limit):
        super().__init__(name, amount)
        self.limit = limit

    def info(self):
        return f"{self.name}: {self.amount} ₸ (лимит {self.limit} ₸)"

class Budget:
    def __init__(self):
        self.records = []

    def add(self, record):
        self.records.append(record)
        print(f"'{record.name}' сәтті қосылды! ({record.amount} ₸)")

    def delete(self, name):
        for r in self.records:
            if r.name == name:
                self.records.remove(r)
                print(f"'{name}' өшірілді!")
                return
        print(f"'{name}' табылмады!")

    def search(self, name):
        for r in self.records:
            if r.name == name:
                print(f"{r.info()} табылды!")
                return
        print(f"{name} тізімде жоқ!")

    def total(self):
        return sum(r.amount for r in self.records)

    def list_all(self):
        for r in self.records:
            print(r.info())

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for r in self.records:
                f.write(f"{r.name},{r.amount}\n")
        print("Мәліметтер файлға сақталды")

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.records = []
                for line in f:
                    name, amount = line.strip().split(",")
                    self.records.append(Record(name, float(amount)))
            print("Файлдан оқу сәтті аяқталды")
        except FileNotFoundError:
            print("Файл табылмады!")

budget = Budget()
budget.add(Record("Тамақ", 60000))
budget.add(Record("Жол ақысы", 15000))
budget.add(Record("Коммуналка", 20000))

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
    print("11–OOP көрсету")
    ch = input("Таңдау: ")
    try:
        if ch == "1":
            name = input("Санат атауы: ")
            amt = float(input("Сомасы: "))
            lim = input("Лимит (болмаса Enter басыңыз): ")
            if lim:
                budget.add(BigRecord(name, amt, float(lim)))
            else:
                budget.add(Record(name, amt))
        elif ch == "2":
            budget.list_all()
        elif ch == "3":
            name = input("Ізделетін санат: ")
            budget.search(name)
        elif ch == "4":
            name = input("Өшірілетін санат: ")
            budget.delete(name)
        elif ch == "5":
            total = budget.total()
            print(f"Барлық шығындардың қосындысы: {total} ₸")
        elif ch == "6":
            budget.save_to_file("shygyn.csv")
        elif ch == "7":
            budget.load_from_file("shygyn.csv")
        elif ch == "8":
            print("Бағдарлама аяқталды.")
            break
        elif ch == "9":
            vals = np.array([r.amount for r in budget.records])
            print("\nNumPy статистикасы:")
            print("Барлық сома:", np.sum(vals))
            print("Орташа шығын:", np.mean(vals))
            print("Максимум:", np.max(vals))
            print("Минимум:", np.min(vals))
        elif ch == "10":
            categories = [r.name for r in budget.records]
            values = [r.amount for r in budget.records]
            plt.figure(figsize=(8,5))
            plt.bar(categories, values)
            plt.title("Айлық шығындар графигі")
            plt.xlabel("Санаттар")
            plt.ylabel("Сома (₸)")
            plt.grid(True, alpha=0.3)
            plt.show()
        elif ch == "11":
            r1 = Record("Тамақ", 60000)
            r2 = BigRecord("Киім", 90000, 100000)
            print("\nOOP нәтижелері:")
            print(r1.info())
            print(r2.info())
        else:
            print("Қате таңдау!")
    except ValueError:
        print("Қате: сан енгізіңіз!")
    except Exception as e:
        print("Күтпеген қате:", e)
