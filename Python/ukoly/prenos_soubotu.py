
# Převedeme 250 KiB na bajty
data_size_bites = 250 * 1024 * 8

# Převedeme rychlost 100 Mb/s na bajty za sekundu
transfer_rate_bytes_per_second = 1e8 # 1*10^8 = 100*1000*1000

# Vypočítáme čas přenosu
transfer_time_seconds = data_size_bites / transfer_rate_bytes_per_second * 1000

print(f"Čas přenosu je aproximně {transfer_time_seconds} milisekundy.")


def transfer_time(file_sice, unit ="KiB", ethernet_speed = 10):
    if unit == "KiB":
        data_size_bites = file_sice * 1024
    elif unit == "MiB":
        data_size_bites = file_sice * 1024 * 1024
    elif unit == "GiB":
        data_size_bites = file_sice * 1024 * 1024 * 1024
    file_size_bites = data_size_bites * 8
    return file_size_bites / (ethernet_speed * 1e6)

print(transfer_time(80, unit = "KiB", ethernet_speed = 100))
