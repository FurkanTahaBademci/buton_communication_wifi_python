import ButtonComm
import time

# Kullanımı
# Buton IP adresisini giriniz
esp_ip = "192.168.4.1"


def run():
    """
    Sürekli olarak ESP8266 ile iletişim kurarak pin durumunu kontrol eder.
    """
    while True:
        result = ButtonComm.ButtonClient(esp_ip)
        print(result)

        if result == "1":
            print("Butona basıldı")
        elif result == "0":
            print("Buton serbest")

        if "bağlanılamadı" in result or "zaman aşımına uğradı" in result:
            # Bağlantı hatasında belirlenen süre kadar bekle
            time.sleep(3)
        else:
            # Normal sorgu döngüsü için kısa bir bekleme süresi
            time.sleep(0.05)


if __name__ == "__main__":
    run()
