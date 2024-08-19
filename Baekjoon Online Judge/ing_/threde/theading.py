from threading import Thread
import time

class TotalCal:
    def __init__(self, value):
        self.value = value
        
    def _for_count(self):
        for i in range(int(self.value)):
            time.sleep(1)
            print(i+1)
    
    def check_time(self):
        thread1 = Thread(target=self._for_count)
        thread2 = Thread(target=self._for_count)

        thread1.start()
        thread2.start()
        
        thread1.join()
        thread2.join()
        
        print(f"총 갯수는 {self.value}")
    

if __name__ == "__main__":
    a = TotalCal(int(input()))        
    a.check_time()