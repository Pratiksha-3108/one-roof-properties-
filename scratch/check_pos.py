with open('about.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = 49498
print(text[pos-100:pos+150])

