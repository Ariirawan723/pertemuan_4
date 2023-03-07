import math

# Diketahui
soal = "Contoh pelat datar dipanasi pada seluruh panjangnya untuk suatu sistem aliran pada contoh diatas, asumsikan pelat dipanasi pada seluruh panjangnya menjadi 60 0C. hitunglah perpindahan panas (a) pada jarak 20 cm dan (b) pada jarak 40 cm suhu film"

v = 17.36 * (10 ** -6)
k = 0.02749
Pr = 0.7  # angka Prandtl
jarak_b = 0.4  # m
jarak_a = 0.2  # m
suhu_a = 60
suhu_b = 27

class HeatTransfer:
    def __init__(self, jarak, Pr, k, v):
        self.jarak = jarak
        self.Pr = Pr
        self.k = k
        self.v = v
    def Rex(self):
        return round((2 * self.jarak) / self.v, 0)
    def Nux(self):
        return round(0.332 * math.sqrt(self.Rex()) * (self.Pr ** (1 / 3)), 2)
    def Hx(self):
        return round(self.Nux() * self.k / self.jarak, 3)
    def Hh(self):
        return round(self.Hx() * 2, 3)
    def Q(self, suhu_a, suhu_b):
        return round(self.Hh() * self.jarak * (suhu_a - suhu_b), 2)

# Menghitung perpindahan panas pada jarak 20 cm
heat_transfer_a = HeatTransfer(jarak_a, Pr, k, v)
hasil_a = heat_transfer_a.Q(suhu_a, suhu_b)
print(soal)
print(f"Perpindahan panas pada jarak {jarak_a} m adalah {hasil_a}W")
    
# Menghitung perpindahan panas pada jarak 40 cm
heat_transfer_b = HeatTransfer(jarak_b, Pr, k, v)
hasil_b = heat_transfer_b.Q(suhu_a, suhu_b)
print(f"Perpindahan panas pada jarak {jarak_b} m adalah {hasil_b}W")
