import re
from collections import Counter

# İncelenecek log dosyasının adı (Kod ile aynı klasörde olmalıdır)
# Test etmek için kendi auth.log dosyanızı bu dizine ekleyebilirsiniz.
log_path = "auth.log" 

# Başarısız giriş denemelerini ve IP adreslerini yakalayan Regex (Düzenli İfade) deseni
pattern = re.compile(r"Failed password.* from (\d+\.\d+\.\d+\.\d+)")

ips = []

try:
    # Log dosyasını okuma işlemi
    with open(log_path, "r", errors="ignore") as f:
        for line in f:
            m = pattern.search(line)
            if m:
                ips.append(m.group(1))

    # IP adreslerini sayma ve en çok saldıran 10 IP'yi listeleme
    c = Counter(ips)
    
    print("-" * 40)
    print(f"🚨 TESPİT EDİLEN TOP 10 SALDIRGAN IP 🚨")
    print("-" * 40)
    
    for ip, count in c.most_common(10):
        print(f"IP Adresi: {ip:<15} | Başarısız Deneme: {count}")
    print("-" * 40)

except FileNotFoundError:
    print(f"Hata: '{log_path}' adlı dosya bulunamadı. Lütfen log dosyasının kod ile aynı klasörde olduğundan emin olun.")