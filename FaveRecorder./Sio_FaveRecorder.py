import openpyxl as xl

book = xl.load_workbook("favorite_people.xlsx")
sheet = book.active

person = 1
id = 1

while person <= 3:
    print(f"\nPerson {person}")

    fname = input("First Name: ")
    lname = input("Last Name: ")
    byear = eval(input("Birth Year: "))

    age = 2026 - byear

    sheet.append([id, lname, fname, byear, age])

    id += 1
    person += 1

book.save("favorite_people.xlsx")

print("\nFavorite Person Successfully Added!\n")

print("----[ Favorite Person List ]----\n")
for rows in sheet.iter_rows(values_only=True):
    print(rows)

input("\nPress enter to exit: ")
