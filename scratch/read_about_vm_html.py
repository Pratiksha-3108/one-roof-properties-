with open('about.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<section id="visionMissionSection"' in l or 'id="visionMissionSection"' in l and '<section' in l:
        print(f"HTML starts at line {i+1}")
        for j in range(i, min(len(lines), i+60)):
            print(f"{j+1}: {lines[j]}", end='')
        break

