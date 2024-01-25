import os


def dosya_var_mi(dosya_yolu):
    """
    Belirtilen dosya yolunda bir dosyanın var olup olmadığını kontrol eder.

    Args:
    dosya_yolu (str): Kontrol edilecek dosyanın tam yolu.

    Returns:
    bool: Dosya varsa True, yoksa False döner.
    """
    return os.path.exists(dosya_yolu)


def dosya_olustur(dosya_yolu):
    """
    Belirtilen dosya yolunda bir dosya oluşturur.

    Args:
    dosya_yolu (str): Oluşturulacak dosyanın tam yolu.
    """
    with open(dosya_yolu, 'w'):
        pass


dosya_yolu = "C:\\Users\\mehmetakif.erdem\\Desktop\\Bel22.pdf"  # Dosyanın tam yolunu buraya girin
if dosya_var_mi(dosya_yolu):
    print("Dosya mevcut.")
else:
    print("Dosya mevcut değil.")
    dosya_olustur(dosya_yolu)
    print("Dosya oluşturuldu.")

def string_to_dict(input_string):
    board_dict = {}
    lines = input_string.strip().split("\n")
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            board_name = " ".join(parts[:-1])
            fqbn = parts[-1]
            board_dict[board_name] = fqbn
    return board_dict


input_string = """
Deneyap Kart       deneyap:esp32:dydk_mpv10
Deneyap Kart 1A    deneyap:esp32:dydk1a_mpv10
Deneyap Kart 1A v2 deneyap:esp32:dydk1a_mpv20
Deneyap Kart G     deneyap:esp32:dyg_mpv10
Deneyap Mini       deneyap:esp32:dym_mpv10
Deneyap Mini v2    deneyap:esp32:dym_mpv20
"""

board_dict = string_to_dict(input_string)
print(board_dict)