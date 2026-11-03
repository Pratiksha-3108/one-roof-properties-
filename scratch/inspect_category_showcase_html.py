with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('<section id="categoryShowcaseSection">')
print("HTML Position:", pos)
print(text[pos:pos+3000])

