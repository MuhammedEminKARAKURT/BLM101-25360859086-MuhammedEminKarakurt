def rle_encode(data):
    if not data:
        return ""
    encoding = ""
    prev_char = data[0]
    count = 1
    for char in data[1:]:
        if char == prev_char:
            count += 1
        else:
            encoding += str(count) + prev_char
            prev_char = char
            count = 1
    encoding += str(count) + prev_char
    return encoding

def rle_decode(data):
    decode = ""
    count = ""
    for char in data:
        if char.isdigit():
            count += char  # Sayı birden fazla basamaklı olabilir (örn: 12A)
        else:
            decode += char * int(count)
            count = ""
    return decode

# Kullanıcıdan veri girişi
veri = input("Sıkıştırılacak veriyi girin: ")
sikisik_veri = rle_encode(veri)
geri_donen_veri = rle_decode(sikisik_veri)

# Sıkıştırma oranı hesaplama
oran = (1 - (len(sikisik_veri) / len(veri))) * 100 if len(veri) > 0 else 0

# Çıktılar
print(f"Sıkıştırılmış hali: {sikisik_veri}")
print(f"Sıkıştırma Oranı: %{oran:.2f}")
print(f"Verinin geri döndürülmüş hali: {geri_donen_veri}")
