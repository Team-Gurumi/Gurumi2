# node/core/resource_monitor.py

import psutil
import time
import threading

class ResourceMonitor:
    def __init__(self):
        self.cpu_usage = 0
        self.memory_usage = 0
        self.network_sent = 0
        self.network_recv = 0
        self.running = False

    def start_monitoring(self):
        self.running = True
        thread = threading.Thread(target=self.monitor)
        thread.start()

    def stop_monitoring(self):
        self.running = False

    def monitor(self):
        print("[ResourceMonitor] 자원 모니터링 시작")
        while self.running:
            self.cpu_usage = psutil.cpu_percent(interval=1)
            self.memory_usage = psutil.virtual_memory().percent
            net = psutil.net_io_counters()
            self.network_sent = net.bytes_sent
            self.network_recv = net.bytes_recv
            time.sleep(1)
