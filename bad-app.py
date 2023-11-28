from tempfile import mkstemp
from tempfile import mktemp
# import pickle
import os

# 1
fd, fname = mkstemp()
print("Created a temp file", fname)
os.close(fd)

# 2
fd, fname = mkstemp()
print("Created another temp file", fname)
os.close(fd)

# 3
# obj = pickle.loads("file.object")
# print("Loaded a file using pickle")

