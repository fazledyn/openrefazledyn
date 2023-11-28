from tempfile import mkstemp
from tempfile import mktemp
import pickle


# 1
fname = mktemp()
print("Created a temp file", fname)

# 2
_, fname = mkstemp()
print("Created another temp file", fname)

# 3
obj = pickle.loads("file.object")
print("Loaded a file using pickle")

