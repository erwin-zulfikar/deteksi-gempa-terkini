"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""

def ekstraksi_data():
    """
    Tanggal: 24 November 2022
    Waktu: 11:51:32 WIB
    Magnitudo: 3.8
    Kedalaman: 10 km
    Lokasi: LS=3.80 BT=128.50
    Pusat gempa: Pusat gempa berada di laut 30 km barat daya Maluku Tengah
    Dirasakan: Dirasakan (Skala MMI): I-II Ambon
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '24 November 2022'
    hasil['waktu'] = '11:51:32 WIB'
    hasil['magnitudo'] = 3.8
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls': 3.80, 'bt': 128.50}
    hasil['pusat'] = 'Pusat gempa berada di laut 30 km barat daya Maluku Tengah'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): I-II Ambon'

    return hasil


def tampilkan_data(result):
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)