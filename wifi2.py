import time
import requests


class ESP8266Client:
    def __init__(self, ip, timeout=1, retry_interval=3):
        """
        ESP8266 ile iletişim kuracak olan sınıfın başlatıcısı.

        :param ip: ESP8266 cihazının IP adresi
        :param timeout: İstek zaman aşımı süresi (saniye)
        :param retry_interval: Bağlantı hatası durumunda tekrar deneme süresi (saniye)
        """
        self.ip = ip
        self.timeout = timeout
        self.retry_interval = retry_interval

    def query_pin_status(self):
        """
        ESP8266'dan pin durumunu sorgular ve sonucu döndürür.
        """
        try:
            response = requests.get(f"http://{self.ip}/", timeout=self.timeout)
            if response.status_code == 200:
                return "Pin Durumu: " + response.text.strip()
            else:
                # Detaylı hata mesajları için HTTP durum koduna göre özel mesajlar
                error_message = f"Bir hata oluştu, yanıt kodu: {response.status_code}"
                if response.status_code == 404:
                    error_message += " - Sayfa bulunamadı."
                elif response.status_code == 500:
                    error_message += " - Sunucu iç hatası."
                return error_message
        except requests.exceptions.ConnectionError:
            return f"Cihaz uyku modunda veya ağa bağlanılamadı. {self.retry_interval} saniye sonra yeniden denenecek."
        except requests.exceptions.Timeout:
            return f"İstek zaman aşımına uğradı, {self.retry_interval} saniye sonra yeniden denenecek."
        except requests.exceptions.RequestException as e:
            return f"Genel bir istek hatası oluştu: {str(e)}"

    def run(self):
        """
        Sürekli olarak ESP8266 ile iletişim kurarak pin durumunu kontrol eder.
        """
        while True:
            result = self.query_pin_status()
            print(result)
            if "bağlanılamadı" in result or "zaman aşımına uğradı" in result:
                # Bağlantı hatasında belirlenen süre kadar bekle
                time.sleep(self.retry_interval)
            else:
                # Normal sorgu döngüsü için kısa bir bekleme süresi
                time.sleep(0.05)


# Kullanımı
esp_ip = "192.168.4.1"
client = ESP8266Client(esp_ip)
client.run()
