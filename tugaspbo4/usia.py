from datetime import date

def age(yearBorn) :
    return date.today().year - yearBorn

yearBorn = int(input("Tambahkan tahun lahir kamu : "))

print(f"Kamu usia {age(yearBorn)} tahun sekarang ")
