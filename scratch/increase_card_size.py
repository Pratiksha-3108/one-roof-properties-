with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update services-staggered-section container width
old_section_css = '''    .services-staggered-section {
      background: var(--bg-cream);
      padding: 100px 0 130px;
      position: relative;
    }'''

new_section_css = '''    .services-staggered-section {
      background: var(--bg-cream);
      padding: 100px 0 140px;
      position: relative;
    }
    .services-staggered-section .container {
      width: min(95vw, 1460px);
      max-width: 1460px;
      margin: 0 auto;
    }'''

if old_section_css in content:
    content = content.replace(old_section_css, new_section_css)
    print("Updated services-staggered-section container CSS")
else:
    print("old_section_css not matched directly")

# 2. Update staggered-grid-container and card sizes
old_grid_css = '''    /* Container for Staggered Rows */
    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 20px; /* Exact tight row gap matching reference */
      max-width: 1140px;
      margin: 0 auto;
    }

    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px; /* Exact 20px gap matching reference */
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
    /* 1:1 SQUARE CARD STYLING (IMAGE & CONTENT SQUARES)        */
    /* ======================================================== */

    /* 1. CONTENT CARD (WHITE SQUARE WITH ACCENT TEXT) */
    .stagger-content-card {
      background: var(--bg-white);
      border-radius: var(--radius-card); /* 38px rounded corners */
      padding: clamp(32px, 3.4vw, 44px);
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.04);
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      position: relative;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
    }
    .stagger-content-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 18px 45px rgba(27, 40, 54, 0.08);
      border-color: var(--gold-accent);
    }

    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: 1.6rem;
      margin-bottom: 24px;
      display: inline-block;
    }

    .card-service-title {
      color: var(--gold-accent);
      font-family: 'Jost', sans-serif;
      font-size: clamp(1.45rem, 1.9vw, 1.9rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.18;
      margin-bottom: 20px;
    }

    .card-service-headline {
      color: var(--navy-dark);
      font-size: clamp(0.96rem, 1.15vw, 1.12rem);
      font-weight: 700;
      line-height: 1.38;
      margin-bottom: 14px;
    }

    .card-service-desc {
      color: var(--text-muted);
      font-size: clamp(0.85rem, 0.98vw, 0.94rem);
      line-height: 1.62;
      margin-bottom: auto;
    }

    /* 2. IMAGE CARD (PHOTO SQUARE MATCHING IDENTICAL DIMENSIONS) */
    .stagger-photo-card {
      background: #e2e8f0;
      border-radius: var(--radius-card); /* 38px rounded corners */
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 10px 30px rgba(27, 40, 54, 0.04);
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
    }

    /* Corner badge exact to reference screenshot */
    .photo-corner-badge {
      position: absolute;
      top: 20px;
      right: 20px;
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      border: 1px solid rgba(255, 255, 255, 0.15);
      z-index: 5;
      transition: transform 0.25s, background 0.25s;
    }
    .stagger-photo-card:hover .photo-corner-badge {
      transform: scale(1.1);
      background: var(--gold-accent);
    }

    /* Bottom subtle location tag */
    .photo-bottom-tag {
      position: absolute;
      bottom: 20px;
      left: 20px;
      z-index: 5;
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-pill);
      padding: 5px 14px;
      font-size: 0.72rem;
      font-weight: 600;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 6px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }'''

new_grid_css = '''    /* Container for Staggered Rows - EXPANDED FOR PROMINENT LARGE CARDS */
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
    }

    /* Corner badge exact to reference screenshot */
    .photo-corner-badge {
      position: absolute;
      top: 24px;
      right: 24px;
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.05rem;
      border: 1px solid rgba(255, 255, 255, 0.15);
      z-index: 5;
      transition: transform 0.25s, background 0.25s;
    }
    .stagger-photo-card:hover .photo-corner-badge {
      transform: scale(1.1);
      background: var(--gold-accent);
    }

    /* Bottom subtle location tag */
    .photo-bottom-tag {
      position: absolute;
      bottom: 24px;
      left: 24px;
      z-index: 5;
      background: rgba(15, 23, 42, 0.82);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-pill);
      padding: 7px 16px;
      font-size: 0.78rem;
      font-weight: 600;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 6px;
      text-transform: uppercase;
      letter-spacing: 0.8px;
    }'''

if old_grid_css in content:
    content = content.replace(old_grid_css, new_grid_css)
    print("Updated staggered-grid-container and card sizes successfully!")
else:
    print("old_grid_css not matched directly")

# Also update responsive breakpoint for smooth adaptation
old_resp = '''    @media (max-width: 991px) {
      .stagger-row {
        grid-template-columns: 1fr 1fr; /* 2 equal squares side-by-side on tablet */
        gap: 16px;
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
    }'''

new_resp = '''    @media (max-width: 1080px) {
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
    }'''

if old_resp in content:
    content = content.replace(old_resp, new_resp)
    print("Updated responsive CSS")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html!")

