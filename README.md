# The Raven Language

A desktop app for practicing English–Turkish vocabulary, built with Python and Tkinter. You build your own word and phrase lists, then quiz yourself on them. My first project of real size: it grew out of [My Language Trainer](https://github.com/saitkaplan/mylanguagetrainer) while I was learning Python, between July and November 2023.

## Features

- **Word quiz** and **phrase quiz** modes on your own lists.
- **Repository:** add, edit and remove words and phrases; everything is stored in CSV files next to the app.
- **Settings:** font, font color and background color, saved between sessions.
- The interface is in Turkish.

## Run

Requires Python 3 with Tkinter (included in the standard installers). Run it from the project folder, because the data files and the logo are read from the current folder.

```bash
cd theravenlanguage
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 raven_language.py
```

## Notes

- Version 1.1.4.8, the last version from 2023. The about page and texts were updated in 2026; the rest of the code is as it was.
- `setup.py` built a Windows `.exe` with `py2exe`. It relies on `distutils`, which was removed in Python 3.12, so it no longer works on current Python versions.
- Plans: I would like to improve the app and make it run well on macOS, Windows and Linux.

## License

The source code is released under the [MIT License](LICENSE). The name "The Raven Language" and the logo files (`raven_project_logo.png`, `raven_project_logo.ico`) are not covered by the license.

---

## The Raven Language (Türkçe)

Python ve Tkinter ile yazılmış, İngilizce–Türkçe kelime çalışması için bir masaüstü uygulaması. Kendi kelime ve kalıp cümle listelerini oluşturur, sonra kendini onlarla sınarsın. İlk gerçek ölçekli projem: Python öğrenirken, Temmuz ile Kasım 2023 arasında [My Language Trainer](https://github.com/saitkaplan/mylanguagetrainer)'dan doğdu.

### Özellikler

- Kendi listelerin üzerinde **kelime sınavı** ve **kalıp cümle sınavı** modları.
- **Depo:** kelime ve kalıp cümle ekleme, düzenleme, kaldırma; hepsi uygulamanın yanındaki CSV dosyalarında tutulur.
- **Ayarlar:** yazı tipi, yazı rengi ve arka plan rengi; oturumlar arasında saklanır.
- Arayüz Türkçedir.

### Çalıştırma

Tkinter içeren Python 3 gerekir (standart kurulumlarda hazır gelir). Veri dosyaları ve logo bulunulan klasörden okunduğu için proje klasöründen çalıştır.

```bash
cd theravenlanguage
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python3 raven_language.py
```

### Notlar

- Sürüm 1.1.4.8, 2023'teki son sürüm. Hakkında sayfası ve metinler 2026'da güncellendi; kodun geri kalanı olduğu gibi duruyor.
- `setup.py`, `py2exe` ile Windows için `.exe` üretiyordu. Python 3.12'de kaldırılan `distutils` modülüne dayandığı için güncel Python sürümlerinde çalışmaz.
- Planlar: uygulamayı geliştirip macOS, Windows ve Linux'ta düzgün çalışır hâle getirmek istiyorum.

### Lisans

Kaynak kod [MIT Lisansı](LICENSE) ile yayımlanır. "The Raven Language" adı ve logo dosyaları (`raven_project_logo.png`, `raven_project_logo.ico`) lisansa dahil değildir.
