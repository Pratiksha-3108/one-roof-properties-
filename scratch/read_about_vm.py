with open('about.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'visionMissionSection' in l:
        print(f"Start at line {i+1}")
        for j in range(max(0, i-5), min(len(lines), i+80)):
            print(f"{j+1}: {lines[j]}", end='')
        break

