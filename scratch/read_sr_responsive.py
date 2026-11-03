with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '.sr-node-portal' in l and i > 2350:
        print(f"Responsive at line {i+1}")
        for j in range(max(0, i-10), min(len(lines), i+30)):
            print(f"{j+1}: {lines[j]}", end='')
        break

