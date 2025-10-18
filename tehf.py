print("Qarzhy shyǵyndaryn esepteý")
atauy=input("Shyǵyn ataýy: ")
somasy=float(input("Somasy (teńge): "))
korshetkish=float(input("Kútiletin tabys (teńge): "))
nat=korshetkish-somasy
if nat>=0:
    print(f"{atauy} tiimdi! Paıda: {nat} ₸")
else:
    print(f"{atauy} shyǵyn! Zalal: {abs(nat)} ₸")

print("\nAılyq shyǵyndar tizimi")
s_sanaty=["Tamaq", "Jol aqysy", "Kommunalka", "Tamaq", "Kiim"]
print("Bastapqy tizim:", s_sanaty)
b_emsiz=list(set(s_sanaty))
print("Qaıtalanbaıtyn:", b_emsiz)
bjudjet=float(input("Jalpy bjudjetti engiz (teńge): "))
ozgerm=tuple(["Jalpy bjudjet", bjudjet])
print("Kortej (ózgermeıtin):", ozgerm)

print("\nMátindik izdeý")
ataular=["tamaq", "jol aqysy", "kommunalka", "kiim"]
izdeu=input("Qaı sanatty izdeısiz: ").lower()
if any(izdeu in a for a in ataular):
    print(f"'{izdeu}' sanat tabyldy!")
else:
    print(f"'{izdeu}' tizimde joq!")

print("\nShyǵyndar bazasy")
shygyn_dict = {
    "Tamaq": 60000,
    "Jol aqysy": 15000,
    "Kommunalka": 20000
}

for at, som in shygyn_dict.items():
    print(f"{at}: {som} ₸")

while True:
    print("\n1 – Shyǵyn qosy\n2 – Barlyǵyn kóru\n3 – Shyǵý")
    tandau=input("Tańdaý: ")
    if tandau=="1":
        at=input("Sanat ataýy: ")
        som=float(input("Somasy: "))
        shygyn_dict[at]=som
    elif tandau=="2":
        for k, v in shygyn_dict.items():
            print(f"{k}: {v} ₸")
    elif tandau=="3":
        print("Baǵdarlama aıaqtaldy.")
        break
    else:
        print("Qate tańdaý!")
