from psutil import cpu_percent, phymem_usage, disk_usage, network_io_counters

class MachineStat():
    ''' Get basics machine stats '''
    def get_cpu(self):
        return cpu_percent()*1.0/100
    
    def get_ram(self):
        return phymem_usage().percent*1.0/100
    
    def get_disk_usage(self):
        return disk_usage("/").percent*1.0/100
        #disk_usage("/home").percent
    
    def get_network(self):
        return network_io_counters().packets_sent
