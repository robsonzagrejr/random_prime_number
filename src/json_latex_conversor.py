import json

name = {
    'mr': 'Miller-Rabin',
    'mt': 'Marsenne Twiste',
    'bbs': 'Blum Blum Shub',
}
keys = json.load(open('test_keys_seed.json'))
file_out = 'latex_table.txt'
str_out = ""

for combination, numbers in keys.items():
    test_name, prng_name = combination.split('|') 
    test_name = name[test_name]
    prng_name = name[prng_name]
    for b_size, n_time in numbers.items():
        str_out += f"{test_name} & {prng_name} & {b_size} & "
        str_out += "\\begin{tabular}[c]{@{}l@{}}"
        str_out += "\\\ ".join(
                [ str(n_time['key'])[s:s+15]
                    for s in range(0,len(str(n_time['key'])),15)
                ]
        )
        str_out += "\\end{tabular} "
        str_out += f"& {n_time['time']} & \\\ "
        str_out += "\hline\n"

print(str_out)
