import threading
import time


class UpTime:

    def __init__(self, interval=1):

        self._interval = interval
        self._start = time.time()
        self._uptime = 0.0

        self._run_uptime = True
        self._lock = threading.Lock()
        self._uptime_thread = threading.Thread(target=self._count_time, args=())
        self._uptime_thread.daemon = False
        self._uptime_thread.start()

    def __del__(self):
        self.stop()

    @staticmethod
    def _display_time(now):
        mins, secs = divmod(int(now), 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(f'Uptime : {timeformat}')

    def _count_time(self):

        while self._run_uptime:
            time.sleep((1.0 / 100) + self._interval)
            now = time.time()
            with self._lock:
                self._uptime = now - self._start
            self._display_time(self._uptime)

        print("Finalizando Contador!")

    def stop(self):
        self._run_uptime = False
        self._uptime_thread.join()
        print('End!')

u = UpTime()
time.sleep(5)
u.stop()