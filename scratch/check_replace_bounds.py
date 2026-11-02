with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect the CSS of .stagger-row, .stagger-content-card, .stagger-photo-card
start_css = html.find('/* Container for Staggered Rows */')
end_css = html.find('/* ======================================================== */\n    /* RESPONSIVE LAYOUT', start_css)
print("CSS to replace length:", end_css - start_css)

