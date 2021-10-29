import concurrent.futures, os

NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]

def check(element: int):
   print(f'Starting {os.getpid()}, parent {os.getppid()}')
   if element % element == 0 and element % 2 != 0 and element % 3 != 0:
      return True
   elif element == 2 or element == 3:
      return True
   else:
      return False




if __name__ == '__main__':
   with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
      result = {executor.submit(check, prime): prime for prime in NUMBERS}
      for result_submit in concurrent.futures.as_completed(result):
         answear = result[result_submit]
         try:
            data = result_submit.result()
         except Exception:
            print('Exception')
            continue
         print('%r page is %r ' % (answear, data))

   with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
      result = {executor.submit(check, prime): prime for prime in NUMBERS}
      for result_submit in concurrent.futures.as_completed(result):
         answear = result[result_submit]
         try:
            data = result_submit.result()
         except Exception:
            print('Exception')
            continue
         print('%r page is %r ' % (answear, data))


#Processes use another process, thread the same process
