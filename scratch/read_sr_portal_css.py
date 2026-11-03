with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.sr-node-portal' in l:
        print(f"Line {i+1}")
        for j in range(max(0, i-25), min(len(lines), i+60)):
            print(f"{j+1}: {lines[j]}", end='')
        break

