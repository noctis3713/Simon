import random
ip =  '.'.join('%s'%random.randint(0, 255) for x in range(4))
print(ip)
