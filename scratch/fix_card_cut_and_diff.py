with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update services-staggered-section container CSS
old_section = '''    .services-staggered-section {
      background: var(--bg-cream);
      padding: 100px 0 140px;
      position: relative;
    }
    .services-staggered-section .container {
      width: min(95vw, 1460px);
      max-width: 1460px;
      margin: 0 auto;
    }'''

new_section = '''    .services-staggered-section {
      background: var(--bg-cream);
      padding: 90px 0 130px;
      position: relative;
    }
    .services-staggered-section .container {
      width: min(92vw, 1280px);
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 16px;
      box-sizing: border-box;
    }'''

if old_section in content:
    content = content.replace(old_section, new_section)
    print("Replaced section container")
else:
    print("Section container old text not matched")

# 2. Update staggered-grid-container and cards CSS
old_grid = '''    /* Container for Staggered Rows - EXPANDED FOR PROMINENT LARGE CARDS */
    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 24px; /* Crisp gap matching reference */
      max-width: 1460px;
      width: 100%;
      margin: 0 auto;
    }

    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      align-items: stretch;
      opacity: 0;
      transform: translateY(32px);
      transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1), transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
    }
    .stagger-row.is-visible {
      opacity: 1;
      transform: translateY(0);
    }

    .stagger-empty-spacer {
      display: block;
    }

    /* ======================================================== */
    /* 1:1 SQUARE CARD STYLING (PROMINENT LARGE SQUARES)        */
    /* ======================================================== */

    /* 1. CONTENT CARD (LARGE WHITE SQUARE WITH ACCENT TEXT) */
    .stagger-content-card {
      background: var(--bg-white);
      border-radius: var(--radius-card); /* 38px rounded corners */
      padding: clamp(38px, 3.4vw, 52px);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 36px rgba(27, 40, 54, 0.05);
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      min-height: 460px;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
      text-decoration: none;
    }
    .stagger-content-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 20px 50px rgba(27, 40, 54, 0.09);
      border-color: var(--gold-accent);
    }

    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: 1.95rem;
      margin-bottom: 22px;
      display: inline-block;
    }

    .card-service-title {
      color: var(--gold-accent);
      font-family: 'Jost', sans-serif;
      font-size: clamp(1.75rem, 2.3vw, 2.35rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.15;
      margin-bottom: 18px;
    }

    .card-service-headline {
      color: var(--navy-dark);
      font-size: clamp(1.06rem, 1.28vw, 1.22rem);
      font-weight: 700;
      line-height: 1.36;
      margin-bottom: 16px;
    }

    .card-service-desc {
      color: var(--text-muted);
      font-size: clamp(0.92rem, 1.05vw, 1.02rem);
      line-height: 1.68;
      margin-bottom: 0;
    }

    /* 2. IMAGE CARD (LARGE PHOTO SQUARE MATCHING IDENTICAL DIMENSIONS) */
    .stagger-photo-card {
      background: #e2e8f0;
      border-radius: var(--radius-card); /* 38px rounded corners */
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      min-height: 460px;
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 36px rgba(27, 40, 54, 0.05);
      display: flex;
    }
    .stagger-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .stagger-photo-card:hover img {
      transform: scale(1.06);
    }'''

new_grid = '''    /* Container for Staggered Rows */
    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 22px;
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
      box-sizing: border-box;
    }

    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with minmax(0, 1fr) to prevent right cut-off */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 22px;
      align-items: start;
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.75s cubic-bezier(0.16, 1, 0.3, 1), transform 0.75s cubic-bezier(0.16, 1, 0.3, 1);
      will-change: opacity, transform;
      width: 100%;
      box-sizing: border-box;
    }
    .stagger-row.is-visible {
      opacity: 1;
      transform: translateY(0);
    }

    .stagger-empty-spacer {
      display: block;
      width: 100%;
      aspect-ratio: 1 / 1;
      pointer-events: none;
    }

    /* ======================================================== */
    /* EXACT 1:1 SQUARES - ZERO DIFFERENCE BETWEEN PHOTO & TEXT */
    /* ======================================================== */

    /* 1. CONTENT CARD (PERFECT 1:1 SQUARE) */
    .stagger-content-card {
      background: var(--bg-white);
      border-radius: var(--radius-card); /* 38px rounded corners */
      padding: clamp(26px, 2.5vw, 38px);
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
      transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
      text-decoration: none;
    }
    .stagger-content-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 18px 45px rgba(27, 40, 54, 0.09);
      border-color: var(--gold-accent);
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

    /* 2. IMAGE CARD (PERFECT 1:1 SQUARE MATCHING EXACT DIMENSIONS) */
    .stagger-photo-card {
      background: #e2e8f0;
      border-radius: var(--radius-card); /* 38px rounded corners */
      width: 100%;
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      box-sizing: border-box;
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.05);
      display: block;
    }
    .stagger-photo-card img {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .stagger-photo-card:hover img {
      transform: scale(1.06);
    }'''

if old_grid in content:
    content = content.replace(old_grid, new_grid)
    print("Replaced grid and cards CSS")
else:
    print("Grid old text not matched")

# 3. Update Responsive CSS
old_resp = '''    @media (max-width: 1080px) {
      .stagger-row {
        grid-template-columns: 1fr 1fr; /* 2 equal squares side-by-side on tablet */
        gap: 20px;
      }
      .stagger-empty-spacer {
        display: none !important;
      }
      .stagger-row.type-left .stagger-photo-card {
        order: 1;
      }
      .stagger-row.type-left .stagger-content-card {
        order: 2;
      }
    }

    @media (max-width: 680px) {
      .stagger-row {
        grid-template-columns: 1fr; /* Stack vertically on phones */
      }
      .stagger-content-card,
      .stagger-photo-card {
        aspect-ratio: auto;
        min-height: 340px;
      }
    }'''

new_resp = '''    @media (max-width: 1024px) {
      .stagger-row {
        grid-template-columns: repeat(2, minmax(0, 1fr)); /* 2 equal squares side-by-side */
        gap: 18px;
      }
      .stagger-empty-spacer {
        display: none !important;
      }
      .stagger-row.type-left .stagger-photo-card {
        order: 1;
      }
      .stagger-row.type-left .stagger-content-card {
        order: 2;
      }
    }

    @media (max-width: 680px) {
      .stagger-row {
        grid-template-columns: 1fr; /* Clean single column stack on mobile */
        gap: 16px;
      }
      .stagger-content-card,
      .stagger-photo-card {
        aspect-ratio: 1 / 1;
        width: 100%;
      }
    }'''

if old_resp in content:
    content = content.replace(old_resp, new_resp)
    print("Replaced responsive CSS")
else:
    print("Responsive old text not matched")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html!")

