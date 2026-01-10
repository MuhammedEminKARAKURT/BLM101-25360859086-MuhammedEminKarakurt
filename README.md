BTU BLM101_Project
Öğrenci Bilgileri: Muhammed Emin Karakurt 25360859086

Proje Konusu: Veri Depolama ve Sıkıştırma Algoritmaları

YouTube Linki: https://www.youtube.com/watch?v=ehjXEQ9kcpI

Proje Açıklaması:
Kodun ne yaptığı:
Bu Python programı,basit bir veriyi (örneğin ardışık tekrarlayan karakterlerden oluşan bir metni
veya 0/1 matrisini) sıkıştırarak boyutunu azaltan bir programdır

Nasıl çalıştırılacağı (kurulum gerekip gerekmediği)
Kodu herhangi bir metin düzenleyiciye yapıştırıp .py uzantısıyla kaydettikten sonra, terminal veya komut satırı üzerinden ilgili dizinde python dosya_adi.py komutunu çalıştırmanız programı başlatmak için yeterlidir.

Kodun Çalışma Mantığı:
Bu Python kodu, Run-Length Encoding (RLE) adı verilen, veri içindeki ardışık tekrarlara dayanan temel bir kayıpsız sıkıştırma algoritmasını uygular. Algoritmanın çalışma mantığı; bir veri dizisindeki aynı karakterlerin peş peşe gelme durumunu tespit ederek, bu karakterleri tek tek yazmak yerine "karakterin sayısı + karakterin kendisi" (örneğin: AAA yerine 3A) şeklinde bir çift olarak kodlamaktır. rle_encode fonksiyonu veri setini tarayıp bu grupları sayarak sıkıştırılmış metni oluştururken, rle_decode fonksiyonu bu sayısal verileri tekrar karaktere dönüştürerek orijinal veriyi geri getirir. Son aşamada ise orijinal veri ile sıkıştırılmış verinin uzunlukları karşılaştırılarak, yapılan işlemin veriyi ne kadar küçülttüğü yüzdelik bir oranla kullanıcıya sunulur.
