import time
begin = time.clock_gettime(time.CLOCK_BOOTTIME)
val = input()
end = time.clock_gettime(time.CLOCK_BOOTTIME)

print(end-begin)