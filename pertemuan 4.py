import math

#Diketahui
ketebalan_besi = 0.025
konduktivitas_termal = 45
difusivitas_termal = 1.4 * (10 ** -5)
waktu = 30
suhu_awal = 35
suhu_permukaan = 250
flux_permukaan = 3.2 * (10 ** 5)

#Kasus A
x_2alfatau = round(ketebalan_besi / (2 * math.sqrt(difusivitas_termal * waktu)), 2)
erf = round(math.erf(x_2alfatau), 5)
suhu_akhir_a = round(suhu_permukaan + (suhu_awal - suhu_permukaan) * erf, 1)

#kasus B
suhu_akhir_b = suhu_awal + ((2 * flux_permukaan * (math.sqrt(difusivitas_termal * waktu / math.pi))) / konduktivitas_termal) * math.e ** (-x_2alfatau ** 2) - ((ketebalan_besi * flux_permukaan) / konduktivitas_termal) * (1 - erf)
suhu_permukaan_b = suhu_awal + (2 * flux_permukaan * (math.sqrt(difusivitas_termal * waktu / math.pi))) / konduktivitas_termal

# Output
print("Contoh. Suatu blok besi besar (k=45W/m0C, =1,4.10-5 m2/s) awalnya memiliki suhu seragam 35 0C. Permukaannya kemudian dipapar flux panas (a) dengan tiba2 meningkatkan suhu permukaan menjadi 250 0C (b) melalui flux panas permukaan konstan 3,2.10-5 W/m2. hitunglah suhu di kedalaman 2,5 cm setelah 0,5 menit untuk kedua kasus tersebut.")
print(f"Kasus A:\n Suhu di kedalaman 2.5 cm setelah 0.5 menit adalah {suhu_akhir_a} C")
print(f"Kasus B:\n Suhu di kedalaman 2.5 cm setelah 0.5 menit adalah {round(suhu_akhir_b,1)} C pada suhu permukaan {round(suhu_permukaan_b,1)} C")
