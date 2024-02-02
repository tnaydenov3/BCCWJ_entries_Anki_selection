import re

INPUT_FILE = 'BCCWJ_ordered.txt'
OUTPUT_FILE = 'BCCWJ_selected.txt'

vocabulary_data = {}
pos_counts = {}
lang_counts = {}

def katakana_to_hiragana(char):
    # Use re.sub with a custom function to convert Katakana to Hiragana
    return re.sub(r'[\u30a1-\u30f6]', lambda x: chr(ord(x.group()) - 96), char)

with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
    next(input_file)
    for line in input_file:
        data = line.strip().split('\t')
        entry, reading, lang, pos, freq = data

        if int(freq) < 20:
            continue

        if lang not in ['漢', '和', '混']:
            continue

        if not pos in ['名詞', '動詞', '副詞', '形状詞', '形容詞', '代名詞']:
            continue

        if not lang == '漢':
            reading = katakana_to_hiragana(reading)

        if not entry in vocabulary_data:
            vocabulary_data[entry] = [entry, reading, lang, pos, freq]
        elif not reading in vocabulary_data[entry][1]:
            vocabulary_data[entry][1] += f' ; {reading}'

        # Count unique occurrences for pos
        if pos not in pos_counts:
            pos_counts[pos] = 1
        else:
            pos_counts[pos] += 1

        # Count unique occurrences for lang
        if lang not in lang_counts:
            lang_counts[lang] = 1
        else:
            lang_counts[lang] += 1



with open(OUTPUT_FILE, 'w', encoding='utf-8') as output_file:
    for entry, data in vocabulary_data.items():
        line = '\t'.join(data) + '\n'
        output_file.write(line)


# Print unique occurrences for pos in descending order
print("POS Counts:")
for pos, count in sorted(pos_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{pos}: {count}")

# Print unique occurrences for lang in descending order
print("\nLang Counts:")
for lang, count in sorted(lang_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{lang}: {count}")