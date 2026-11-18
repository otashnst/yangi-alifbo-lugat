# Yangi alifbo konvertori — imlo lug‘ati

Bu repozitoriyda «Yangi alifbo konvertori» dasturining imlo lug‘ati turadi.
Dastur har safar ishga tushganda shu yerdagi `manifest.json` ni tekshiradi:
versiya raqami kattaroq bo‘lsa, lug‘at fayllarini yuklab oladi va keyin internetsiz ishlatadi.

| Fayl | Nima |
|---|---|
| `uz_UZ-2026.dic` | So‘z o‘zaklari (Hunspell, 2026 alifbosi) |
| `uz_UZ-2026.aff` | Qo‘shimchalar qoidalari |
| `freq.txt` | So‘zlar chastotasi (taklif tartibi uchun) |
| `manifest.json` | Versiya va fayllarning nazorat summasi (sha256) |

## Lug‘atni yangilash

1. `uz_UZ-2026.dic` ga yangi so‘z qo‘shing — har qatorda bitta so‘z.
   Qo‘shimchalar bilan ishlashi uchun ot so‘zlarga `/ABVIJKLMQS` belgisini qo‘shing, masalan `avariyaviy/ABVIJKLMQS`.
   Birinchi qatordagi son — so‘zlar soni; uni ham bittaga oshiring.
2. Manifestni qayta yarating (Python kerak):
   ```
   python make_dict_release.py . . 2026.12.01 "Qo‘shilgan so‘zlar haqida qisqa izoh"
   ```
   Versiya har safar avvalgisidan katta bo‘lishi shart (yil.oy.kun).
3. O‘zgargan fayllarni GitHub’ga yuklang (commit). Bir necha daqiqadan keyin barcha kompyuterlardagi dastur yangi lug‘atni oladi.

`manifest.json` dagi summa fayllarga mos kelmasa, dastur yangilanishni rad etadi va eski lug‘at bilan ishlayveradi — shuning uchun 2-qadamni o‘tkazib yubormang.

## Litsenziya

Lug‘at [bitg-hunspell](https://github.com/dtwinuz/bitg-hunspell) (uz-hunspell asosida) va
[uzb-frequent-words](https://github.com/kaharjan/uzb-frequent-words) loyihalaridan olingan, GPL-3.0.
