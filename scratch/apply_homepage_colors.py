import re

file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Update .card-service-title and .card-service-headline
# in CSS to strictly use home page colors:
# Title -> var(--navy-primary) / #465665 with font-family var(--font-serif-head)
# Subtitle/Headline -> var(--navy-dark) / #1f343f (or #7b8791)
# Description -> var(--text-muted) / #7b8791

target = """    .card-service-title {
      color: var(--gold-accent);
      font-family: 'Jost', sans-serif;
      font-size: clamp(1.3rem, 1.65vw, 1.8rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.15;
      margin-bottom: clamp(8px, 1vw, 12px);
      flex-shrink: 0;
    }

    .card-service-headline {
      font-family: var(--font-serif-head);
      color: var(--navy-primary);
      font-size: clamp(0.92rem, 1.05vw, 1.12rem);
      font-weight: 700;
      line-height: 1.35;
      letter-spacing: -0.2px;
      margin-bottom: clamp(8px, 0.9vw, 12px);
      flex-shrink: 0;
    }"""

replacement = """    .card-service-title {
      color: var(--navy-primary); /* #465665 from home page */
      font-family: var(--font-serif-head); /* 'Nanum Myeongjo', Georgia, serif */
      font-size: clamp(1.35rem, 1.7vw, 1.85rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.2;
      margin-bottom: clamp(8px, 1vw, 12px);
      flex-shrink: 0;
    }

    .card-service-headline {
      font-family: 'Jost', sans-serif;
      color: var(--navy-dark); /* #1f343f deep contrast subtitle from home page */
      font-size: clamp(0.94rem, 1.08vw, 1.15rem);
      font-weight: 600;
      line-height: 1.4;
      letter-spacing: -0.2px;
      margin-bottom: clamp(8px, 0.9vw, 12px);
      flex-shrink: 0;
    }"""

assert target in html, "Target CSS block not found"
html = html.replace(target, replacement)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Updated title and subtitle colors to match home page!")

