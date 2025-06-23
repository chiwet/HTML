import os, sys, locale
print(os.getenv("USERPROFILE"))
print(locale.getpreferredencoding())

path_bytes = os.getenv("USERPROFILE").encode('cp1251')
path_bytes.decode('utf-8') 