# 1d cellular automaton
from random import *

def num_to_digits(x):
    if x == "0":
        return "_"
    elif x == "1":
        return "*"

random_seq = []

with open("C:\\Users\\puszk\\Documents\\cell_autom_rules.txt", "r") as read_file:
    for line in read_file:
        if "Rule" in line:
            rule = list(line.split(":")[1].strip())
        elif "Sequence length" in line:
            n = int(line.split(":")[1].strip())
        elif "Steps to complete" in line:
            steps = int(line.split(":")[1].strip())
        elif "Sequence" in line:
            random_seq = list(line.split(":")[1].strip())

print("File opened successfully")
print("Rule: " + ("".join(str(x) for x in rule)) + "\n"
      + "Sequence length: " + str(n) + "\n"
      + "Steps to complete: " + str(steps) + "\n"
      + "Sequence: " + ("".join(str(x) for x in random_seq)))
print()

set_of_rules = {
    '***': num_to_digits(rule[0]),
    '**_': num_to_digits(rule[1]),
    '*_*': num_to_digits(rule[2]),
    '*__': num_to_digits(rule[3]),
    '_**': num_to_digits(rule[4]),
    '_*_': num_to_digits(rule[5]),
    '__*': num_to_digits(rule[6]),
    '___': num_to_digits(rule[7]),
}

# # Polecenie 2
#
# for i in range (n):
#     random_seq.append(randint(0,1))
#
# # Polecenie 5
#
# for i in range (n//2):
#     random_seq.append(0)
# random_seq.append(1)
# for i in range(n//2):
#     random_seq.append(0)

result = [0] * n

for i in range (steps):
    # Przepelnienie licznika, trzeba zaladowac nowa mape
    if (i%n == 0 and i > 0):
        random_seq = result.copy()

    pattern = ""
    pattern += str(random_seq[(i - 1) % n])
    pattern += str(random_seq[(i) % n])
    pattern += str(random_seq[(i + 1) % n])
    result[i%n] = set_of_rules[pattern]

print("Result sequence = " + ("".join(str(x) for x in result)))

with open("C:\\Users\\puszk\\Documents\\cellular_automaton.txt", "w") as save_file:
    save_file.write("Rule: " + "".join(str(x) for x in rule) + "\n")
    save_file.write("Sequence length: " + str(n) + "\n")
    save_file.write("Steps to complete: " + str(steps) + "\n")
    save_file.write("Result sequence = " + ("".join(str(x) for x in result)))

print("Results saved to \"C:\\Users\\puszk\\Documents\\cellular_automaton.txt\"")