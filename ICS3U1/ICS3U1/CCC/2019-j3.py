def encode(line):
    get_current_char = None
    current_char_count = 0
    encoded_line = ""
    for charactor in line:
        if not get_current_char:
            get_current_char = charactor
            current_char_count = 1
        elif get_current_char != charactor:
            encoded_line += f"{current_char_count} {get_current_char}"
            get_current_char = charactor
            current_char_count = 1
        else:
            current_char_count += 1
    return encoded_line


n = int(input())

lines = []




for i in range(n):
    line = input()
    lines.append(line)
for i in range(n):
    print(encode(lines[i]))