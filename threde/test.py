import time
import asyncio


class total_cal():
    def __init__(self, value):
        self.value = value
        
    async def _for_count(self):
        for i in range(int(self.value)):
            await asyncio.sleep(1)
            print(i+1)
    
    async def check_time(self):
        
        await asyncio.gather(self._for_count(), self._for_count())
        print(f"총 갯수는 {self.value}")

if __name__ == "__main__":

    a = total_cal(int(input()))        
    asyncio.run(a.check_time())
