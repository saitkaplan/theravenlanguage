from distutils.core import setup
import py2exe

# setup(windows=['raven_project.py'])

setup(
    windows=[{
        'script': 'raven_project.py',
        'icon_resources': [(0, 'raven_project_logo.ico')]  # İkonunuzu eklemek isterseniz
    }],
    options={
        'py2exe': {
            'bundle_files': 1,  # Dizinlerin ve kütüphanelerin tek bir EXE dosyasında birleştirilmesini sağlar
            'compressed': True,  # Sıkıştırılmış dosyaları oluşturur
            'optimize': 0,  # Kodunuzu optimize eder (0 iyidir iyi)
            'dll_excludes': ['w9xpopen.exe'],  # dosyasının boyutunu biraz azaltır ve uyumluluk sorunlarını engeller.
        },
    },
    zipfile=None,  # Tüm kütüphanelerin tek bir zip dosyası halinde değil,
                   # ayrı ayrı dosyalar olarak oluşturulmasını sağlar
)