oop = PolozeniPredmet("Objektno Orjentisano Programiranje", "Bla Bla BlA", 10)
mat = PolozeniPredmet("Matematika 2", "Bla Bla BlA", 10)
stp = PolozeniPredmet("Strukture Podataka I Algoritme", "Bla Bla BlA", 10)
mreze = PolozeniPredmet("Mreze", "Bla Bla BlA", 10)

npoop = NepolozeniPredmet("Objektno Orjentisano Programiranje", "Bla Bla BlA", 2)
npmat = NepolozeniPredmet("Matematika 2", "Bla Bla BlA", 3)
npstp = NepolozeniPredmet("Strukture Podataka I Algoritme", "Bla Bla BlA", 4)
npmreze = NepolozeniPredmet("Mreze", "Bla Bla BlA", 5)



# Inicijalnoi podaci o Studentu
data = []
data.append(Student("2018/703", "Marko Markovic", [oop, mat, stp, mreze], []))
data.append(Student("2018/116", "Pera Peric", [oop], [npmat, npstp, npmreze]))
data.append(Student("2018/980", "Stanko Stankovic", [mat], [npoop, npstp, npmreze]))