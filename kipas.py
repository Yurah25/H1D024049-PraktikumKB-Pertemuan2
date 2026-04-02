import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kecepatan = ctrl.Consequent(np.arange(0, 101, 1), 'kecepatan')

suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['sedang'] = fuzz.trimf(suhu.universe, [10, 20, 30])
suhu['panas'] = fuzz.trimf(suhu.universe, [20, 40, 40])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['normal'] = fuzz.trimf(kelembapan.universe, [25, 50, 75])
kelembapan['basah'] = fuzz.trimf(kelembapan.universe, [50, 100, 100])

kecepatan['lambat'] = fuzz.trimf(kecepatan.universe, [0, 0, 50])
kecepatan['sedang'] = fuzz.trimf(kecepatan.universe, [25, 50, 75])
kecepatan['cepat'] = fuzz.trimf(kecepatan.universe, [50, 100, 100])

rule1 = ctrl.Rule(suhu['dingin'] | kelembapan['kering'], kecepatan['lambat'])
rule2 = ctrl.Rule(suhu['sedang'] & kelembapan['normal'], kecepatan['sedang'])
rule3 = ctrl.Rule(suhu['panas'] & kelembapan['basah'], kecepatan['cepat'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
kipas_simulasi = ctrl.ControlSystemSimulation(kipas_ctrl)

print("Input Sistem Logika Fuzzy Kecepatan Kipas")
suhu_input = float(input("Masukkan nilai Suhu (0-40 °C)       : "))
kelembapan_input = float(input("Masukkan nilai Kelembapan (0-100 %) : "))

kipas_simulasi.input['suhu'] = suhu_input
kipas_simulasi.input['kelembapan'] = kelembapan_input

kipas_simulasi.compute()

print("\nHasil Simulasi")
print(f"Output Kecepatan Kipas : {kipas_simulasi.output['kecepatan']:.2f} (Skala 0-100)")