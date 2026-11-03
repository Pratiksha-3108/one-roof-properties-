import re

file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS: replace .card-top-flame-icon with .card-service-num
css_target = """    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: clamp(1.3rem, 1.6vw, 1.65rem);
      margin-bottom: clamp(10px, 1.2vw, 16px);
      display: inline-block;
      flex-shrink: 0;
    }"""

css_replacement = """    .card-service-num {
      font-family: var(--font-serif-head);
      font-size: clamp(1.45rem, 1.85vw, 2rem);
      font-weight: 700;
      color: var(--gold-accent);
      line-height: 1;
      letter-spacing: 0.04em;
      margin-bottom: clamp(10px, 1.2vw, 16px);
      display: inline-block;
      flex-shrink: 0;
    }"""

assert css_target in html, "CSS target for flame icon not found"
html = html.replace(css_target, css_replacement)

# 2. Replace the 6 flame icons in the 6 rows with 01, 02, 03, 04, 05, 06
row_matches = [
    ('id="service-row-1"', '<span class="card-service-num">01</span>'),
    ('id="service-row-2"', '<span class="card-service-num">02</span>'),
    ('id="service-row-3"', '<span class="card-service-num">03</span>'),
    ('id="service-row-4"', '<span class="card-service-num">04</span>'),
    ('id="service-row-5"', '<span class="card-service-num">05</span>'),
    ('id="service-row-6"', '<span class="card-service-num">06</span>'),
]

for row_id, num_tag in row_matches:
    # Find the row block
    pattern = re.compile(
        re.escape(row_id) + r'.*?<i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>',
        re.DOTALL
    )
    m = pattern.search(html)
    assert m is not None, f"Could not find flame icon in {row_id}"
    matched_text = m.group(0)
    replaced_text = matched_text.replace(
        '<i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>',
        num_tag
    )
    html = html[:m.start()] + replaced_text + html[m.end():]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Replaced all flame icons with numbers 01 to 06!")

