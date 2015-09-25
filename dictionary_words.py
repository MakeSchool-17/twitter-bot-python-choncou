import random
import sys
import time

start_time = time.clock()

my_file = open("/usr/share/dict/words", encoding='utf-8')
my_dictionary = my_file.read().split()
final_out = []
for i in range(int(sys.argv[1])):
    final_out.append(my_dictionary[random.randint(0, len(my_dictionary)-1)])

print(" ".join(final_out))
my_file.close()

end_time = time.clock()
print(end_time - start_time)
