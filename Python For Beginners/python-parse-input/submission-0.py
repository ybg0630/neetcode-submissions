from typing import List

def read_integers() -> List[int]:
    input_string = input("")
    output = input_string.split(",")
    for i in range(len(output)):
        output[i] = int(output[i])
    return output

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
