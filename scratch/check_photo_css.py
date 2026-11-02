with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's inspect the current CSS for .stagger-photo-card and its children
start = content.find('/* 2. IMAGE CARD')
end = content.find('/* Corner badge', start)
print("Current photo card CSS:")
print(content[start:end])

