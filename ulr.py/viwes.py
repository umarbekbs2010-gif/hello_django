# Restoran projekt!
users = {}
taomlar = {}
balans = 0

while True:
    print("\n=== Asosiy menyu ===")
    print("1. Bankomat")
    print("2. Bank")
    print("3. Restoran")
    print("4. Dasturdan chiqish")
    tanlov = input(">> ")

    if tanlov == "1":
        print("--- Bankomat bo'limi (Hali ishga tushmagan) ---")
    elif tanlov == "2":
        print("--- Bank bo'limi (Hali ishga tushmagan) ---")
    elif tanlov == "3":

        while True:
            print("1. Ro'yhatdan o'tish")
            print("2. Kirish")
            print("3. Orqaga qaytish")
            restoran_tanlov = input(">> ")

            if restoran_tanlov == "1":
                isim = input("Yangi usernameni kiriting: ")
                parol = input("Yangi parolni kiriting: ")
                users[isim] = 1234
                print("<< Siz ro'yhatdan muvaffaqiyatli o'tdingiz!")


            elif restoran_tanlov == "2":
                login = input("Usernameni kiriting: ")
                parol = input("Parolni kiriting: ")

                if login in users and users[login] == 1234:
                    print(f"<< Xush kelibsiz, {login}!")

                    while True:
                        print("\n=== RESTORAN ASOSIY MENYU ===")
                        print("1. Taom qo'shish")
                        print("2. Taomlar ro'yhati")
                        print("3. Taom sotib olish")
                        print("4. Balansni ko'rish")
                        print("5. Chiqish (Restoran menyusidan)")
                        r_menyu = input(">> ")

                        if r_menyu == "1":
                            nomi = input("Taom nomini kiriting: ")
                            narxi = int(input("Taom narxini kiriting: "))
                            taomlar[nomi] = ([35,40,50,100,20])
                            print(f"{nomi} menyuga qo'shildi!")

                        elif r_menyu == "2":
                            print("\n--- Taomlar ro'yhati ---")
                            if not taomlar:
                                print("Hozircha taomlar yo'q.")
                            else:
                                for taom, narx in taomlar.items():
                                    print(f"{taom} - {narx} so'm")

                        elif r_menyu == "3":
                            sotib_olish = input("Qaysi taomni sotib olmoqchisiz?: ")
                            if sotib_olish in taomlar:
                                narx = taomlar[sotib_olish]
                                if balans >= narx:
                                    balans -= narx
                                    print(f"Yoqimli ishtaha! {sotib_olish} xarid qilindi.")
                                else:
                                    print("Mablag' yetarli emas!")
                            else:
                                print("Bunday taom menyuda yo'q!")

                        elif r_menyu == "4":
                            print(f"\nSizning balansingiz: {balans} so'm")

                        elif r_menyu == "5":
                            break
                        else:
                            print("Noto'g'ri tanlov!")
                else:
                    print("Username yoki parol xato!")

            elif restoran_tanlov == "3":
                break
            else:
                print("Noto'g'ri tanlov!")

    elif tanlov == "4":
        print("Dastur to'xtatildi.")
        break
    else:
        print("Noto'g'ri buyruq kiritdingiz!")