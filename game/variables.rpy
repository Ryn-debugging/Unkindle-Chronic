# Kode ini dijalankan saat game pertama kali dimuat
init python:
    # Class untuk status pemain
    class MainCharacter:
        def __init__(self, name, hp, mp, sanity):
            self.name = name
            self.max_hp = hp
            self.hp = hp
            self.max_mp = mp
            self.mp = mp
            self.sanity = sanity
            self.inventory = ["Ramuan HP"] # Pemain mulai dengan 1 ramuan

    # Class untuk status heroine (Alicia)
    class Heroine:
        def __init__(self, name, affection):
            self.name = name
            self.love = affection
            self.is_corrupted = False

# Mendaftarkan variabel ke sistem Ren'Py
default p = MainCharacter("Pahlawan", 100, 50, 100)
default alicia = Heroine("Alicia", 0)