from psutil import cpu_percent, phymem_usage, disk_usage, network_io_counters

class MachineStat():
    cpu_percent()
    phymem_usage().percent
    disk_usage("/").percent
    disk_usage("/home").percent
    network_io_counters().packets_sent
