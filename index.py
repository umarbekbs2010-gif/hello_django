import sys

products = []
next_id = 1


def add_products():
    global next_id
    try:
        count = int(input("      Nechta product qo'shmoqchisiz?: "))
        if count <= 0:
            print("      [!] Noldan katta son kiriting.")
            return

        for _ in range(count):
            name = input(f"        Product nomini kiriting: ")
            price = input(f"        Product narxini kiriting: ")
            products.append({"id": next_id, "name": name, "price": price})
            next_id += 1

        print(f"      {count} ta product muvaffaqiyatli qo'shildi\n")
    except ValueError:
        print("      [!] Iltimos, faqat butun son kiriting.\n")


def delete_products():
    if not products:
        print("      [!] Ro'yxatda mahsulot mavjud emas.\n")
        return

    try:
        count = int(input("      Nechta product o'chirmoqchisiz?: "))
        if count <= 0:
            print("      [!] Noldan katta son kiriting.\n")
            return

        if count > len(products):
            print(
                f"      [!] Hozirda faqat {len(products)} ta product bor.\n"
            )
            return

        for _ in range(count):
            products.pop()

        print(f"      {count} ta product muvaffaqiyatli o'chirildi\n")
    except ValueError:
        print("      [!] Iltimos, faqat butun son kiriting.\n")


def update_product():
    if not products:
        print("      [!] Ro'yxatda mahsulot mavjud emas.\n")
        return

    try:
        p_id = int(
            input(
                "    Update qilmoqchi bo'lgan productingizning ID sini kiriting: "
            )
        )
        found = False

        for prod in products:
            if prod["id"] == p_id:
                new_name = input("        Yangi nomni kiriting: ")
                new_price = input("        Yangi narxni kiriting: ")
                prod["name"] = new_name
                prod["price"] = new_price
                print(
                    f"      ID {p_id} bo'lgan product muvaffaqiyatli yangilandi!\n"
                )
                found = True
                break

        if not found:
            print(f"      [!] ID {p_id} bo'lgan product topilmadi.\n")
    except ValueError:
        print("      [!] Iltimos, to'g'ri ID kiriting.\n")


def show_products():
    if not products:
        print("      [!] Ro'yxat bo'sh.\n")
        return

    print("\n--- PRODUCTLAR RO'YHATI ---")
    for prod in products:
        print(
            f"ID: {prod['id']} | Nomi: {prod['name']} | Narxi: {prod['price']}"
        )
    print("---------------------------\n")


def main():
    print("Start bosildi 👉\n")

    while True:
        print("ASOSIY MENYU==>")
        print("1)Product qo'shish")
        print("2)Product o'chirish")
        print("3)Product update")
        print("4)Productlar ro'yhati")
        print("5)Chiqish")

        choice = input("Tanlovingizni kiriting (1-5): ").strip()

        if choice == "1":
            add_products()
        elif choice == "2":
            delete_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            show_products()
        elif choice == "5":
            print("Dastur yakunlandi.")
            sys.exit()
        else:
            print("      [!] Noto'g'ri tanlov, qaytadan urinib ko'ring.\n")


if name == "main":
    main()