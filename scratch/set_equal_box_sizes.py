with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .stagger-row alignment and gap
old_row_css = '''    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with center alignment for card size difference */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 26px;
      align-items: center; /* Creates the distinct Torch vertical offset between tall & compact cards */
      width: 100%;
      box-sizing: border-box;
    }'''

new_row_css = '''    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with EXACT SAME BOX SIZES */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px; /* Exact 20px gap matching reference */
      align-items: stretch; /* Guarantees identical height and boundary alignment */
      width: 100%;
      box-sizing: border-box;
    }'''

if old_row_css in content:
    content = content.replace(old_row_css, new_row_css)
    print("Updated stagger-row CSS")
else:
    print("old_row_css not matched directly")

# 2. Update .stagger-photo-card to be EXACT 1:1 SQUARE IDENTICAL TO CONTENT CARD
old_photo_css = '''    /* 2. IMAGE CARD (TALLER LUXURY CARD WITH IMAGE SLIDER EFFECT) */
    .stagger-photo-card {
      background: #e9ecf1;
      border-radius: var(--radius-card); /* 38px rounded corners */
      width: 100%;
      aspect-ratio: 1 / 1.25; /* TALLER LUXURY SHOWCASE CARD MATCHING TORCH VIDEO */
      min-height: 460px;
      box-sizing: border-box;
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 14px 36px rgba(27, 40, 54, 0.07);
      display: block;
      transform-style: preserve-3d;
      perspective: 1000px;
      cursor: pointer;
      opacity: 0;
      transform: translateY(60px) scale(0.94);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.4s ease;
      will-change: transform, opacity;
    }'''

new_photo_css = '''    /* 2. IMAGE CARD (EXACT IDENTICAL 1:1 SQUARE SIZE TO CONTENT CARD) */
    .stagger-photo-card {
      background: #e9ecf1;
      border-radius: var(--radius-card); /* 38px rounded corners */
      width: 100%;
      aspect-ratio: 1 / 1; /* EXACT SAME 1:1 SQUARE RATIO AS CONTENT CARD */
      box-sizing: border-box;
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.05);
      display: block;
      transform-style: preserve-3d;
      perspective: 1000px;
      cursor: pointer;
      opacity: 0;
      transform: translateY(45px);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.4s ease;
      will-change: transform, opacity;
    }'''

if old_photo_css in content:
    content = content.replace(old_photo_css, new_photo_css)
    print("Updated photo card CSS to exact same 1:1 square!")
else:
    print("old_photo_css not matched directly")

# 3. Update container gap and responsive styles
old_container_css = '''    /* Container for Staggered Rows */
    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 32px;
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
      box-sizing: border-box;
    }'''

new_container_css = '''    /* Container for Staggered Rows */
    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 20px; /* Exact 20px gap matching reference */
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
      box-sizing: border-box;
    }'''

if old_container_css in content:
    content = content.replace(old_container_css, new_container_css)
    print("Updated container gap to 20px")

# Also ensure on mobile/tablet both cards remain equal:
old_resp_photo = '''      .stagger-photo-card {
        aspect-ratio: 1 / 1;
        min-height: 320px;
      }'''

new_resp_photo = '''      .stagger-content-card,
      .stagger-photo-card {
        aspect-ratio: 1 / 1;
        width: 100%;
      }'''

if old_resp_photo in content:
    content = content.replace(old_resp_photo, new_resp_photo)
    print("Updated responsive photo card CSS")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html with equal square card sizes!")

