# secrets gera numeros aleatorios

import string as s
from secrets import SystemRandom as Sr

#print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))
print(''.join(Sr().choices(s.ascii_lowercase + s.digits, k=16)))
