import socket
import time

print("=== Port Scanner ===")

target = input("Hedef IP veya domain gir: ").strip()
start_port = int(input("Başlangıç portu: "))
end_port = int(input("Bitiş portu: "))

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hedef çözümlenemedi. Domain veya IP hatalı olabilir.")
    exit()

print(f"\nHedef: {target} ({target_ip})")
print(f"Taranan aralık: {start_port}-{end_port}")
print("Tarama başlatılıyor...\n")

open_ports = []
start_time = time.time()

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "bilinmiyor"

            print(f"[AÇIK] Port {port} - Servis: {service}")
            open_ports.append((port, service))

        sock.close()

    except KeyboardInterrupt:
        print("\nTarama kullanıcı tarafından durduruldu.")
        break
    except socket.error:
        print(f"Port {port} taranırken hata oluştu.")

end_time = time.time()
elapsed_time = end_time - start_time

print("\n=== Tarama Tamamlandı ===")
print(f"Toplam süre: {elapsed_time:.2f} saniye")

if open_ports:
    print("\nAçık portlar:")
    for port, service in open_ports:
        print(f"- {port} ({service})")
else:
    print("\nAçık port bulunamadı.")