from input_from_file import init_file, input
init_file("2608")

a = input()
b = input()

roma_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

sb = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900
}

def roma_to_arabia(roma):
    curr_roma = ""
    arabia = 0

    i = 0
    while (i < len(roma)):
        curr_key = roma[i: i + 2]

        is_found = False
        for curr_sb in sb.keys():
            if curr_key == curr_sb:
                arabia += sb[curr_key]
                i += 1
                is_found = True
                break
        if not is_found:
            curr_roma += roma[i]

        i += 1

    for i in curr_roma:
        arabia += roma_dict[i]
    return arabia

vals = []
for k, v in roma_dict.items():
    vals.append((v, k))
for k, v in sb.items():
    vals.append((v, k))
vals = sorted(vals, reverse=True)

def arabia_to_roma(arabia):
    curr_roma = ""
    for i in range(len(vals)):
        curr_val, curr_key = vals[i]
        quo = arabia // curr_val
        if quo > 0:
            arabia = arabia % curr_val
            curr_roma += curr_key * quo
    return curr_roma

a_arabia = roma_to_arabia(a)
b_arabia = roma_to_arabia(b)
result = a_arabia + b_arabia
print(result)
print(arabia_to_roma(result))