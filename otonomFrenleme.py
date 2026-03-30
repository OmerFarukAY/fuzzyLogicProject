import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

# Girdi ve çıktı değişkenlerinin tanımlandığı yer
aracinHizi = ctrl.Antecedent(np.arange(0, 181, 1), 'Aracin Hizi')
takipMesafesi = ctrl.Antecedent(np.arange(0, 101, 1), 'Takip Mesafesi')
frenSiddeti = ctrl.Consequent(np.arange(0, 101, 1), 'Fren Siddeti')


# Üyelik fonk. tanımlandığı yer
# Üyelik fonk. üçgen olarak ayarlandı

# Aracin Hizi için üyelik fonk.
aracinHizi['yavas'] = fuzzy.trimf(aracinHizi.universe, [0, 0, 70])
aracinHizi['normal'] = fuzzy.trimf(aracinHizi.universe, [50, 90, 130])
aracinHizi['hizli'] = fuzzy.trimf(aracinHizi.universe, [110, 180, 180])

# Takip Mesafesi için üyelik fonk.
takipMesafesi['cok_yakin'] = fuzzy.trimf(takipMesafesi.universe, [0, 0, 40])
takipMesafesi['yakin'] = fuzzy.trimf(takipMesafesi.universe, [20, 50, 80])
takipMesafesi['uzak'] = fuzzy.trimf(takipMesafesi.universe, [60, 100, 100])

# Frenin Şiddeti için üyelik fonk.
frenSiddeti['yok'] = fuzzy.trimf(frenSiddeti.universe, [0, 0, 20])
frenSiddeti['hafif'] = fuzzy.trimf(frenSiddeti.universe, [10, 30, 50])
frenSiddeti['orta'] = fuzzy.trimf(frenSiddeti.universe, [40, 60, 80])
frenSiddeti['sert'] = fuzzy.trimf(frenSiddeti.universe, [70, 100, 100])

# Grafikler için
#mesafe.view()
#hiz.view()
#fren.view()
#plt.show()

# Fuzzy kuralların tanımlandığı yer

# Takip Mesafesinin çok yakın olduğu durumlar
rule1 = ctrl.Rule(takipMesafesi['cok_yakin'] & aracinHizi['hizli'], frenSiddeti['sert'])
rule2 = ctrl.Rule(takipMesafesi['cok_yakin'] & aracinHizi['normal'], frenSiddeti['sert'])
rule3 = ctrl.Rule(takipMesafesi['cok_yakin'] & aracinHizi['yavas'], frenSiddeti['orta'])



# Takip Mesafesinin yakın olduğu durumlar
rule4 = ctrl.Rule(takipMesafesi['yakin'] & aracinHizi['hizli'], frenSiddeti['sert'])
rule5 = ctrl.Rule(takipMesafesi['yakin'] & aracinHizi['normal'], frenSiddeti['orta'])
rule6 = ctrl.Rule(takipMesafesi['yakin'] & aracinHizi['yavas'], frenSiddeti['hafif'])



# Takip Mesafesinin uzak olduğu durumlar
rule7 = ctrl.Rule(takipMesafesi['uzak'] & aracinHizi['hizli'], frenSiddeti['hafif'])
rule8 = ctrl.Rule(takipMesafesi['uzak'] & aracinHizi['normal'], frenSiddeti['yok'])
rule9 = ctrl.Rule(takipMesafesi['uzak'] & aracinHizi['yavas'], frenSiddeti['yok'])




# Kontrol sistemini oluşturmak için bütün kuralları girdik
frenlemeSistemi = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
frenSimulasyonu = ctrl.ControlSystemSimulation(frenlemeSistemi)

#girdilerin alındığı yer
print("\n--Otonom Frenleme Başladı--")
print("Çıkmak için 'q' harfine basabilirsiniz.\n")

while True:
    hizGirdisi = input("Aracınızın hızını girin (0-180 km/s): ")

    # Çıkış yapılmak isteniyor mu kontrol et
    if hizGirdisi.lower() == 'q':
        print("Sistem kapatılıyor. Görüşmek üzere!")
        break


    mesafeGirdisi = input("Önünüzdeki araçla aranızdaki mesafeyi girin. (0-100 m): ")

    # Çıkış yapılmak isteniyor mu kontrol et
    if mesafeGirdisi.lower() == 'q':
        print("Sistem kapatılıyor. Görüşmek üzere!")
        break


    try:
        mesafeDegeri = float(mesafeGirdisi)
        hizDegeri = float(hizGirdisi)

        # Belirlenen sınırlar içinde girdi verildi mi kontrol ediyoruz
        if not (0 <= hizDegeri <= 180) or not (0 <= mesafeDegeri <= 100):
            print("Lütfen verilern sınırlar içinde bir değer giriniz!!! (Mesafe: 0-100, Hız: 0-180)\n")
            continue

        # Girilen değerler hesaplanıyor
        frenSimulasyonu.input['Aracin Hizi'] = hizDegeri
        frenSimulasyonu.input['Takip Mesafesi'] = mesafeDegeri
        frenSimulasyonu.compute()

        # Sonuç yazdırma
        fren_sonucu = frenSimulasyonu.output['Fren Siddeti']
        print(f" FREN ŞİDDETİ: %{fren_sonucu:.2f}\n")

    except ValueError:
        print("ERROR: Lütfen girdiğiniz değerin bir sayı olmasına dikkat edin!\n")
