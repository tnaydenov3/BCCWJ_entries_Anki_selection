INPUT_FILE = 'BCCWJ.txt'
OUTPUT_FILE = 'BCCWJ_ordered.txt'

output_lines = []

with open(INPUT_FILE, 'r', encoding='utf-16-le') as input_file:
    for line in input_file:
        data = line.strip().split('\t')
        entry, reading, lang, pos, freq = data[3], data[2], data[5], data[7], data[9]
        output_line = '\t'.join([entry, reading, lang, pos, freq]) + '\n'
        output_lines += [output_line]

header_line = output_lines[0]
output_lines = output_lines[1:]

output_lines = sorted(output_lines, key=lambda x: x.split('\t')[0])
output_lines = sorted(output_lines, key=lambda x: int(x.split('\t')[4]), reverse=True)

output_lines = [header_line] + output_lines

with open(OUTPUT_FILE, 'w', encoding='utf-8') as output_file:
    output_file.writelines(output_lines)