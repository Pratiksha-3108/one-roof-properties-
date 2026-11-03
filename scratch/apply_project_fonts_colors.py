file_path = r'd:\DTG\One-Roof-Properties\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .sr-title-text to use home page serif font 'Nanum Myeongjo', 'Playfair Display', Georgia, serif
old_title_text = """    .sr-title-text {
      position: absolute;
      bottom: clamp(10px, 1.4vw, 18px);
      left: 0;
      font-family: 'Jost', 'Plus Jakarta Sans', sans-serif;
      font-size: clamp(2.6rem, 5.0vw, 5.2rem);
      font-weight: 700;
      color: #465665;
      line-height: 1.15;
      letter-spacing: -1.5px;
      margin: 0;
      padding-bottom: 6px;
      white-space: nowrap;
      transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.5s ease;
    }"""

new_title_text = """    .sr-title-text {
      position: absolute;
      bottom: clamp(10px, 1.4vw, 18px);
      left: 0;
      font-family: 'Nanum Myeongjo', 'Playfair Display', Georgia, serif;
      font-size: clamp(2.6rem, 5.0vw, 5.2rem);
      font-weight: 700;
      color: #465665;
      line-height: 1.15;
      letter-spacing: -1px;
      margin: 0;
      padding-bottom: 6px;
      white-space: nowrap;
      transition: transform 0.6s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.5s ease;
    }"""

assert old_title_text in html, "old_title_text not found"
html = html.replace(old_title_text, new_title_text)
print("Updated .sr-title-text font to Nanum Myeongjo")

# 2. Update .sr-node-sub, .sr-node-name, .sr-node-detail, .sr-node-link
old_node_typography = """    .sr-node-sub {
      font-family: 'Jost', sans-serif;
      font-size: 0.72rem;
      font-weight: 600;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #d97706;
      margin-bottom: 6px;
    }
    .sr-node-name {
      font-family: 'Nanum Myeongjo', Georgia, serif;
      font-size: clamp(1.35rem, 1.8vw, 1.95rem);
      font-weight: 700;
      color: #ffffff;
      margin: 0 0 6px 0;
      line-height: 1.25;
      text-shadow: 0 2px 12px rgba(0,0,0,0.6);
    }
    .sr-node-detail {
      font-family: 'Jost', sans-serif;
      font-size: 0.84rem;
      font-weight: 400;
      color: rgba(255, 255, 255, 0.92);
      line-height: 1.5;
      max-width: 270px;
      margin: 0 0 12px 0;
      text-shadow: 0 1px 8px rgba(0,0,0,0.5);
    }
    .sr-node-link {
      font-family: 'Jost', sans-serif;
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #FAF8EE;
      background: rgba(217, 119, 6, 0.9);
      padding: 6px 16px;
      border-radius: 999px;
      backdrop-filter: blur(6px);
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.35);
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }"""

new_node_typography = """    .sr-node-sub {
      font-family: 'Jost', sans-serif;
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 2.2px;
      text-transform: uppercase;
      color: #d97706; /* Homepage gold accent */
      margin-bottom: 6px;
    }
    .sr-node-name {
      font-family: 'Nanum Myeongjo', 'Playfair Display', Georgia, serif;
      font-size: clamp(1.28rem, 1.6vw, 1.8rem);
      font-weight: 700;
      color: #FAF8EE; /* Homepage architectural cream */
      margin: 0 0 6px 0;
      line-height: 1.22;
      text-shadow: 0 2px 14px rgba(0, 0, 0, 0.7);
    }
    .sr-node-detail {
      font-family: 'Jost', sans-serif;
      font-size: 0.84rem;
      font-weight: 400;
      color: rgba(250, 248, 238, 0.88); /* Homepage cream-tinted body */
      line-height: 1.55;
      max-width: 260px;
      margin: 0 0 14px 0;
      text-shadow: 0 1px 8px rgba(0, 0, 0, 0.6);
    }
    .sr-node-link {
      font-family: 'Jost', sans-serif;
      font-size: 0.76rem;
      font-weight: 600;
      letter-spacing: 1.6px;
      text-transform: uppercase;
      color: #FAF8EE;
      background: #d97706; /* Homepage gold accent */
      padding: 7px 18px;
      border-radius: 999px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
      transition: all 0.25s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }"""

assert old_node_typography in html, "old_node_typography not found"
html = html.replace(old_node_typography, new_node_typography)
print("Updated project card typography and colors")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html Project Section fonts and colors updated to match homepage palette!")

