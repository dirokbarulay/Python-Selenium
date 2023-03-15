students = []

def addStudent():
    print("\n\n --- Öğrenci Ekleme ---")
    nameSurname = input("Lütfen adınızı ve soyadınızı giriniz: ")
    students.append(nameSurname.title())
    return()

def addMultipleStudent():
    print("\n\n --- Birden Fazla Öğrenci Ekleme ---")
    count = int(input("Eklenilecek öğrenci sayısı giriniz: "))
    for student in range(count):
        addStudent()

def allStudents():
    print("\n\n --- Tüm Öğrenciler ---")
    for student in students:
        print(student)

def schoolNumber():
    print("\n\n --- Öğrenci Numarası ---")
    nameSurname = input("Öğrenci isim ve soyismini giriniz: ").title()
    print("Öğrenci numarası: " + str(students.index(nameSurname)))

def removeStudent():
    print("\n\n --- Öğrenci Silme ---")
    nameSurname = input("Lütfen adınızı ve soyadınızı giriniz: ").title()
    students.remove(nameSurname)
    print("Öğrenci silindi.")

def removeMultipleStudent():
    print("\n\n --- Birden Fazla Öğrenci Silme ---")
    print("Çıkmak için x'e basınız.")
    while True:
        nameSurname = input("Lütfen öğrencinin isim ve soyismini giriniz: ").title()
        if nameSurname == "x" or nameSurname == "X":
            break
        students.remove(nameSurname)
        print("Öğrenci silindi.")


addStudent()
addMultipleStudent()
allStudents()
schoolNumber()
removeStudent()
removeMultipleStudent()