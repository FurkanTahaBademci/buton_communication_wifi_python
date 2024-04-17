import time
import requests


def ButtonClient(ip, timeout=1, retry_interval=3):
    """
    ESP8266'dan pin durumunu sorgular ve sonucu döndürür.
    """
    try:
        response = requests.get(f"http://{ip}/", timeout=timeout)
        if response.status_code == 200:
            return response.text.strip()
        else:
            # Detaylı hata mesajları için HTTP durum koduna göre özel mesajlar
            error_message = f"Bir hata oluştu, yanıt kodu: {response.status_code}"
            if response.status_code == 404:
                error_message += " - Sayfa bulunamadı."
            elif response.status_code == 500:
                error_message += " - Sunucu iç hatası."
            return error_message
    except requests.exceptions.ConnectionError:
        return f"Cihaz uyku modunda veya ağa bağlanılamadı. {retry_interval} saniye sonra yeniden denenecek."
    except requests.exceptions.Timeout:
        return f"İstek zaman aşımına uğradı, {retry_interval} saniye sonra yeniden denenecek."
    except requests.exceptions.RequestException as e:
        return f"Genel bir istek hatası oluştu: {str(e)}"
