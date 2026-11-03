import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root or 'scratch' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.css', '.js')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fl:
                content = fl.read()
                if 'about-building' in content:
                    print(f"Found in {p}")

