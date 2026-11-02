with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .stagger-row, .stagger-content-card, and .stagger-photo-card CSS
old_cards_css = '''    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with EXACT SAME BOX SIZES */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px; /* Exact 20px gap matching reference */
      align-items: stretch; /* Guarantees identical height and boundary alignment */
      width: 100%;
      box-sizing: border-box;
    }

    .stagger-empty-spacer {
      display: block;
      width: 100%;
      aspect-ratio: 1 / 1;
      pointer-events: none;
    }

    /* ======================================================== */
    /* CARD SIZE DIFFERENCE: COMPACT CONTENT CARD vs TALL IMAGE */
    /* ======================================================== */

    /* 1. CONTENT CARD (COMPACT 1:1 SQUARE) */
    .stagger-content-card {
      background: var(--bg-white);
      border-radius: var(--radius-card); /* 38px rounded corners */
      padding: clamp(26px, 2.4vw, 36px);
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.05);
      width: 100%;
      aspect-ratio: 1 / 1; /* Compact 1:1 square ratio */
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
      overflow: hidden;
      opacity: 0;
      transform: translateY(45px);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.35s ease, border-color 0.35s ease;
      will-change: opacity, transform;
      text-decoration: none;
    }
    .stagger-row.is-visible .stagger-content-card {
      opacity: 1;
      transform: translateY(0);
      transition-delay: 0.12s;
    }
    /* No hover effect on content cards */
    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: clamp(1.4rem, 1.8vw, 1.7rem);
      margin-bottom: clamp(12px, 1.4vw, 18px);
      display: inline-block;
      flex-shrink: 0;
    }

    .card-service-title {
      color: var(--gold-accent);
      font-family: 'Jost', sans-serif;
      font-size: clamp(1.45rem, 1.85vw, 1.95rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.15;
      margin-bottom: clamp(10px, 1.1vw, 14px);
      flex-shrink: 0;
    }

    .card-service-headline {
      color: var(--navy-dark);
      font-size: clamp(0.92rem, 1.08vw, 1.12rem);
      font-weight: 700;
      line-height: 1.34;
      margin-bottom: clamp(8px, 0.9vw, 12px);
      flex-shrink: 0;
    }

    .card-service-desc {
      color: var(--text-muted);
      font-size: clamp(0.8rem, 0.9vw, 0.92rem);
      line-height: 1.55;
      margin-bottom: 0;
    }

    /* 2. IMAGE CARD (EXACT IDENTICAL 1:1 SQUARE SIZE TO CONTENT CARD) */
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
    }
    .stagger-row.is-visible .stagger-photo-card {
      opacity: 1;
      transform: translateY(0) scale(1);
    }'''

new_cards_css = '''    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] - EXACT SAME BOX SIZE, NO ANIMATION */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 20px;
      align-items: stretch; /* Both boxes perfectly aligned and equal height */
      width: 100%;
      box-sizing: border-box;
    }

    .stagger-empty-spacer {
      display: block;
      width: 100%;
      aspect-ratio: 1 / 1;
      pointer-events: none;
    }

    /* ======================================================== */
    /* EXACT SAME SIZE FOR BOTH BOXES - ZERO ANIMATION          */
    /* ======================================================== */

    /* 1. CONTENT CARD (EXACT 1:1 SQUARE, NO ANIMATION) */
    .stagger-content-card {
      background: var(--bg-white);
      border-radius: var(--radius-card); /* 38px rounded corners */
      padding: clamp(26px, 2.4vw, 36px);
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.05);
      width: 100%;
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      box-sizing: border-box;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
      overflow: hidden;
      text-decoration: none;
    }

    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: clamp(1.4rem, 1.8vw, 1.7rem);
      margin-bottom: clamp(12px, 1.4vw, 18px);
      display: inline-block;
      flex-shrink: 0;
    }

    .card-service-title {
      color: var(--gold-accent);
      font-family: 'Jost', sans-serif;
      font-size: clamp(1.45rem, 1.85vw, 1.95rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.15;
      margin-bottom: clamp(10px, 1.1vw, 14px);
      flex-shrink: 0;
    }

    .card-service-headline {
      color: var(--navy-dark);
      font-size: clamp(0.92rem, 1.08vw, 1.12rem);
      font-weight: 700;
      line-height: 1.34;
      margin-bottom: clamp(8px, 0.9vw, 12px);
      flex-shrink: 0;
    }

    .card-service-desc {
      color: var(--text-muted);
      font-size: clamp(0.8rem, 0.9vw, 0.92rem);
      line-height: 1.55;
      margin-bottom: 0;
    }

    /* 2. IMAGE CARD (EXACT SAME 1:1 SQUARE SIZE AS CONTENT CARD, NO ANIMATION) */
    .stagger-photo-card {
      background: #e9ecf1;
      border-radius: var(--radius-card); /* 38px rounded corners */
      width: 100%;
      aspect-ratio: 1 / 1; /* EXACT SAME 1:1 SQUARE RATIO MATCHING CONTENT CARD */
      box-sizing: border-box;
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.05);
      display: block;
    }'''

if old_cards_css in content:
    content = content.replace(old_cards_css, new_cards_css)
    print("Updated CSS to remove all card animations and enforce identical sizes!")
else:
    print("old_cards_css not matched directly")

# 2. Update JavaScript: Keep ONLY the Navbar scroll and Slider logic, REMOVE ALL SCROLL PARALLAX AND ENTRANCE ANIMATIONS
js_start = content.find('// 1. Staggered Scroll Entrance Reveal')
js_end = content.find('</script>', js_start)

# Notice slider engine: keep slider logic for images
slider_start = content.find('// 2. IMAGE CARD SLIDER ENGINE', js_start)
slider_end = content.find('// 3. Clear, Noticeable Continuous Scroll Parallax', slider_start)
slider_code = content[slider_start:slider_end].strip()

new_js = '''// Slider Engine (Smooth transitions & auto-play inside image card)
    ''' + slider_code + '''

    // All scroll animations and parallax on cards are disabled as requested
    window.addEventListener('DOMContentLoaded', updateNavbar);
  '''

content = content[:js_start] + new_js + content[js_end:]
print("Updated JS: removed all scroll parallax, float, and entrance observers!")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html cleanly!")

