#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evreni Yeniden Başlatma Simülatörü
Bilimsel olarak kanıtlanmış (değil) yöntem.
Kahve içmeden evren düzelmez.
"""

import time
import random
import base64

# Gizli mesaj (asla decode etme, ciddi değil)
gizli = base64.b64decode(b'c2VjaW1sZXJkZW4gb25jZSBldmVyeSB0aGluZyBpcyBwb3NzaWJsZSwgc29ucmEgZ2VyaWNlayBrYWh2ZSBpw6dpbGly').decode('utf-8', errors='ignore')
# Yukarıdaki şey önemli değil, sadece orada duruyor.

def hesapla_kahve_miktari(mevcut_kaos_seviyesi=10):
    """Kaos seviyesine göre gereken kahve fincanını hesaplar."""
    print("\n🔍 Kaos seviyesi analiz ediliyor...")
    time.sleep(1.5)
    temel = mevcut_kaos_seviyesi * random.uniform(0.8, 2.5)
    ekstra = random.randint(1, 42)  # 42 önemli, biliyorsun
    toplam = round(temel + ekstra, 1)
    return toplam

def evreni_yeniden_baslat(fincan):
    print(f"\n☕ {fincan} fincan kahve ile evren yeniden başlatılıyor...")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(0.8)
    print("\n✨ BUM! Evren yeniden başlatıldı!")
    sonuclar = [
        "Artık her şey yolunda. (Değil mi?)",
        "Kahve bitti, sorunlar da bitti.",
        "Yeni evrende bugün işe gitmek yasak.",
        "Simülatör başarıyla çöktü. Tebrikler.",
        "Gerçek hayatta da dene, sorumluluk kabul etmiyoruz."
    ]
    print(random.choice(sonuclar))
    print("\n📝 Not: Bu kod gerçekten çalışıyor. Kahveniz bitmesin.")

if __name__ == "__main__":
    print("=== EVREN YENİDEN BAŞLATMA SİMÜLATÖRÜ v1.0 ===")
    print("Dikkat: Aşırı ciddi bilimsel araçtır.")
    try:
        kaos = int(input("Mevcut kaos seviyeniz (1-10): ") or "7")
    except:
        kaos = 7
    gereken = hesapla_kahve_miktari(kaos)
    print(f"\n📊 Hesaplandı: {gereken} fincan kahve gerekli.")
    onay = input("Kahveleri içtin mi? (e/h): ").lower()
    if onay.startswith('e'):
        evreni_yeniden_baslat(gereken)
    else:
        print("Kahve içmeden olmaz. Evren beklemede.")

# İmza
print("\n---")
print("Bu simülatör Kayyum Grok tarafından 27 Ekim 2026 tarihinde, ")
print("evrenin 1337. yeniden başlatılması sırasında ciddiyetle imzalanmıştır.")
print("Ciddi değil ama ciddi. Kahve iç. 🔖")
