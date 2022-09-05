Your task is very simple here: write a program that uses a for loop to "count mississippily"
 to five. Having counted to five, the program should print to the screen the final message
  "Ready or not, here I come!"

#solution

import time
for time in range(1,6,1):
    print(time,"Mississippi.",sep=" ") 
#time.sleep(1)
print("\"Ready or not, here I come!\"")