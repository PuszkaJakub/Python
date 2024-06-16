str1 = 'actagcgttagatcctcgta'
str2 = 'ggatcgttgcaagtaactgg'

length = len(str1)
if len(str2) > len(str1):
    length = len(str2)

def check_complementary(str1, str2):    
    pairs = {'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    pairs_count = 0
    connections = ''
    
    for nucleotide1, nucleotide2 in zip(str1, str2):
        if pairs.get(nucleotide1) == nucleotide2:
            pairs_count += 1
            connections += '|'
        else:
            connections += ' '
    
    return pairs_count, connections


max_pairs_count, connections = check_complementary(str1, str2)
str1_version = str1
str2_version = str2
shift = 0

for i in range(1, len(str2)):
    str1_temp = ' '*i + str1

    pairs_count_temp, connections_temp = check_complementary(str1_temp, str2)
    if pairs_count_temp > max_pairs_count:
        max_pairs_count = pairs_count_temp
        str1_version = str1_temp
        str2_version = str2
        connections = connections_temp
        shift = -i

    str2_temp = ' '*i + str2

    pairs_count_temp, connections_temp = check_complementary(str1, str2_temp)
    if pairs_count_temp > max_pairs_count:
        max_pairs_count = pairs_count_temp
        str1_version = str1
        str2_version = str2_temp
        connections = connections_temp
        shift = i

print('pairs:'+str(max_pairs_count) + '    ' + 'shift:'+str(shift))
print(str1_version)
print(connections)
print(str2_version)

