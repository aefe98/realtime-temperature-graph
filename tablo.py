import time
import random
import matplotlib
matplotlib.use('TkAgg')  # Grafik penceresi için backend seç

import matplotlib.pyplot as plt

zaman = []
sicaklik = []

start_time = time.time()

for i in range(20):
    su_an = round(time.time() - start_time)
    yeni_sicaklik = round(random.uniform(36.0, 41.0), 1)

    zaman.append(su_an)
    sicaklik.append(yeni_sicaklik)

    print(f"{su_an}s: {yeni_sicaklik}°C")

    time.sleep(1)

plt.plot(zaman, sicaklik, 'r-o')
plt.xlabel('Zaman (saniye)')
plt.ylabel('Sıcaklık (°C)')
plt.title('20 Saniyelik Vücut Sıcaklığı Grafiği')
plt.ylim(35, 42)
plt.grid(True)
plt.show()
plt.savefig('sicaklik_grafik.png')
print("Grafik 'sicaklik_grafik.png' olarak kaydedildi.")

