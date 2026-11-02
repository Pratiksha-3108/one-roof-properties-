with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove CSS hover rules on cards
old_css_hover = '''    .stagger-content-card:hover {
      box-shadow: 0 22px 50px rgba(27, 40, 54, 0.11);
      border-color: var(--gold-accent);
    }

    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: clamp(1.4rem, 1.8vw, 1.7rem);
      margin-bottom: clamp(12px, 1.4vw, 18px);
      display: inline-block;
      flex-shrink: 0;
      transition: transform 0.3s ease;
    }
    .stagger-content-card:hover .card-top-flame-icon {
      transform: scale(1.15) rotate(6deg);
    }'''

new_css_hover = '''    /* No hover effect on content cards */
    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: clamp(1.4rem, 1.8vw, 1.7rem);
      margin-bottom: clamp(12px, 1.4vw, 18px);
      display: inline-block;
      flex-shrink: 0;
    }'''

if old_css_hover in content:
    content = content.replace(old_css_hover, new_css_hover)
    print("Removed content card hover CSS")
else:
    print("old_css_hover not matched directly")

# 2. Remove CSS hover rules on photo card (shadow, border, img scale, corner badge)
old_photo_hover = '''    .stagger-photo-card:hover {
      box-shadow: 0 28px 60px rgba(27, 40, 54, 0.16);
      border-color: rgba(217, 119, 6, 0.4);
    }

    /* SLIDER TRACK & SLIDES */
    .slider-track {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .slider-slide {
      position: relative;
      flex: 0 0 100%;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }
    .slider-slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .stagger-photo-card:hover .slider-slide img {
      transform: scale(1.06);
    }'''

new_photo_hover = '''    /* No hover effect on photo cards */
    /* SLIDER TRACK & SLIDES */
    .slider-track {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      display: flex;
      transition: transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .slider-slide {
      position: relative;
      flex: 0 0 100%;
      width: 100%;
      height: 100%;
      overflow: hidden;
    }
    .slider-slide img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }'''

if old_photo_hover in content:
    content = content.replace(old_photo_hover, new_photo_hover)
    print("Removed photo card hover CSS")
else:
    print("old_photo_hover not matched directly")

# Also remove corner badge hover
old_badge_hover = '''.stagger-photo-card:hover .photo-corner-badge {
      transform: scale(1.1);
      background: var(--gold-accent);
    }'''
new_badge_hover = '''/* Badge without hover scaling */'''

if old_badge_hover in content:
    content = content.replace(old_badge_hover, new_badge_hover)
    print("Removed badge hover CSS")

# 3. Remove JavaScript mousemove / tilt listeners (Sections 4 & 5)
js_start = content.find('// 4. Smooth 3D Perspective Tilt')
js_end = content.find('</script>', js_start)

if js_start != -1 and js_end != -1:
    content = content[:js_start] + '// Hover effects disabled as requested\n  ' + content[js_end:]
    print("Removed JavaScript mousemove/tilt listeners!")
else:
    print("JS tilt block not found")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html with no hover effects!")

