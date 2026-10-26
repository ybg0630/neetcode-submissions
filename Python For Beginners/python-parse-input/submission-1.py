from typing import List

def read_integers() -> List[int]:
    i = input("")
    return [int(x) for x in i.split(",")]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
