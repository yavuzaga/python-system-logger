import os
import datetime


def log_system_action(action_name):
    """Sistem işlemlerini zaman damgasıyla loglar."""
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{current_time}] İşlem Gerçekleştirildi: {action_name}\n"

    print(log_message.strip())

    # Logları bir dosyaya kaydet
    with open("automation_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message)


if __name__ == "__main__":
    print("🚀 PyCharm ile Python Otomasyon Motoru Başlatıldı...")
    log_system_action("Sistem durumu kontrol edildi. Aktif.")