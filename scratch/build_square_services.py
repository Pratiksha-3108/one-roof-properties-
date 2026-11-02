services_code = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Services | Bespoke Real Estate Advisory &amp; Solutions | One Roof Properties</title>
  <meta name="description" content="Comprehensive real estate services by One Roof Properties: Luxury residential sales, clear-title plotting developments, NRI investment advisory, institutional home loans, certified title due diligence, and portfolio asset management.">
  
  <!-- Google Fonts matching index.html -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Jost:wght@300;400;500;600;700&family=Nanum+Myeongjo:wght@400;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  
  <!-- FontAwesome 6 -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    :root {
      /* Colors taken directly from home page (index.html) */
      --bg-cream: #FAF8EE;
      --bg-cream-soft: #F5F2E7;
      --bg-white: #ffffff;
      --navy-primary: #465665;
      --navy-dark: #1b2836;
      --navy-deep: #0f172a;
      --gold-accent: #d97706;
      --gold-hover: #b45309;
      --gold-light: rgba(217, 119, 6, 0.12);
      --text-dark: #1e293b;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      --border-light: rgba(70, 86, 101, 0.12);
      --border-card: rgba(70, 86, 101, 0.12);
      --radius-sm: 8px;
      --radius-md: 16px;
      --radius-card: 38px; /* Rounded corners exact to reference screenshot */
      --radius-pill: 9999px;
      --font-heading: 'Nanum Myeongjo', 'Playfair Display', Georgia, serif;
      --font-body: 'Plus Jakarta Sans', 'Jost', sans-serif;
    }

    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: var(--font-body);
    }

    body {
      background-color: var(--bg-cream);
      color: var(--text-dark);
      line-height: 1.6;
      overflow-x: hidden;
      -webkit-font-smoothing: antialiased;
    }

    a {
      text-decoration: none;
      color: inherit;
    }

    .container {
      width: min(94vw, 1200px);
      margin: 0 auto;
    }

    /* ======================================================== */
    /* FLOATING HEADER (IDENTICAL TO HOME PAGE index.html)      */
    /* ======================================================== */
    .header {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1500;
      padding: 34px 0 0;
      background: transparent;
      transition: background-color 0.3s ease, padding 0.3s ease, box-shadow 0.3s ease, transform 0.35s ease;
    }
    .header.scrolled {
      position: fixed;
      background: rgba(44, 56, 68, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      padding: 14px 0;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .holder {
      width: min(94vw, 1320px);
      margin: 0 auto;
    }
    .header-block {
      position: relative;
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      min-height: 58px;
      gap: 24px;
    }
    .header-logo {
      position: relative;
      text-align: center;
      z-index: 20;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .header-logo img {
      height: 48px;
      width: auto;
      display: block;
      object-fit: contain;
    }
    .header-nav-list {
      display: flex;
      gap: clamp(18px, 2.2vw, 36px);
      list-style: none;
      align-items: center;
      margin: 0;
      padding: 0;
    }
    .header-nav-right {
      display: flex;
      align-items: center;
      justify-content: flex-end;
    }
    .header-nav-list li {
      font-family: 'Jost', sans-serif;
      font-size: clamp(13px, 0.88vw, 15px);
      font-weight: 500;
      letter-spacing: 1.4px;
      text-transform: uppercase;
    }
    .header-nav-list a {
      color: #ffffff;
      text-decoration: none;
      position: relative;
      transition: color 0.2s ease;
      white-space: nowrap;
    }
    .header-nav-list a:hover {
      color: var(--gold-accent);
    }

    .nav-mobile-btn {
      display: none;
      background: transparent;
      border: none;
      font-size: 1.5rem;
      color: #ffffff;
      cursor: pointer;
    }

    /* ======================================================== */
    /* HERO SECTION (HOME PAGE PALETTE)                         */
    /* ======================================================== */
    .services-hero {
      position: relative;
      background: linear-gradient(135deg, #1b2836 0%, #2c3844 60%, #15222e 100%);
      color: #ffffff;
      padding: 175px 0 115px;
      overflow: hidden;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .services-hero::before {
      content: "";
      position: absolute;
      inset: 0;
      background-image: radial-gradient(rgba(217, 119, 6, 0.12) 1px, transparent 1px);
      background-size: 32px 32px;
      opacity: 0.6;
      pointer-events: none;
    }
    .hero-glow-accent {
      position: absolute;
      width: 550px;
      height: 550px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(217, 119, 6, 0.18) 0%, rgba(96, 165, 250, 0.08) 50%, transparent 70%);
      top: -100px;
      right: -80px;
      filter: blur(60px);
      pointer-events: none;
    }
    .hero-content {
      position: relative;
      z-index: 10;
      max-width: 860px;
    }
    .hero-tagline-badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 0.78rem;
      text-transform: uppercase;
      letter-spacing: 2.5px;
      color: var(--gold-accent);
      background: rgba(217, 119, 6, 0.14);
      border: 1px solid rgba(217, 119, 6, 0.3);
      padding: 6px 18px;
      border-radius: var(--radius-pill);
      margin-bottom: 22px;
    }
    .hero-tagline-badge a {
      color: #cbd5e1;
      transition: color 0.2s;
    }
    .hero-tagline-badge a:hover {
      color: #ffffff;
    }
    .hero-main-title {
      font-family: var(--font-heading);
      font-size: clamp(2.4rem, 4.6vw, 3.8rem);
      font-weight: 700;
      line-height: 1.18;
      color: #ffffff;
      margin-bottom: 22px;
      letter-spacing: -0.5px;
    }
    .hero-main-title span {
      color: var(--gold-accent);
      font-style: italic;
    }
    .hero-main-desc {
      font-size: clamp(1.02rem, 1.3vw, 1.18rem);
      color: #cbd5e1;
      line-height: 1.75;
      font-weight: 300;
      margin-bottom: 38px;
      max-width: 760px;
    }
    .hero-metrics {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 20px;
      padding-top: 32px;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }
    .metric-card {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }
    .metric-number {
      font-family: var(--font-heading);
      font-size: 1.85rem;
      font-weight: 700;
      color: #ffffff;
    }
    .metric-number em {
      color: var(--gold-accent);
      font-style: normal;
    }
    .metric-label {
      font-size: 0.78rem;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 1.2px;
    }

    /* ======================================================== */
    /* SERVICES SECTION: STAGGERED SQUARE CARDS                 */
    /* (EXACT TO USER'S CLOSE-UP SCREENSHOT)                    */
    /* ======================================================== */
    .services-staggered-section {
      background: var(--bg-cream);
      padding: 100px 0 130px;
      position: relative;
    }

    .section-intro-center {
      text-align: center;
      max-width: 760px;
      margin: 0 auto 70px;
    }
    .tracker-pill {
      font-size: 0.76rem;
      text-transform: uppercase;
      letter-spacing: 3px;
      font-weight: 700;
      color: var(--gold-accent);
      margin-bottom: 12px;
      display: inline-block;
    }
    .section-headline {
      font-family: var(--font-heading);
      font-size: clamp(2rem, 3.4vw, 2.75rem);
      color: var(--navy-dark);
      font-weight: 700;
      line-height: 1.25;
      margin-bottom: 16px;
    }
    .section-headline span {
      color: var(--gold-accent);
    }
    .section-subtext {
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.7;
    }

    /* Container for Staggered Rows */
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
    }
    .photo-bottom-tag i {
      color: var(--gold-accent);
    }

    /* ======================================================== */
    /* RESPONSIVE LAYOUT                                        */
    /* ======================================================== */
    @media (max-width: 991px) {
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
    }

    /* ======================================================== */
    /* 4-STEP METHODOLOGY SECTION                               */
    /* ======================================================== */
    .process-section {
      padding: 100px 0;
      background: var(--bg-cream-soft);
      border-top: 1px solid var(--border-light);
    }
    .process-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 24px;
      margin-top: 48px;
    }
    .process-card {
      background: var(--bg-white);
      border: 1px solid var(--border-card);
      border-radius: var(--radius-md);
      padding: 36px 28px;
      position: relative;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04);
    }
    .process-card:hover {
      transform: translateY(-6px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.08);
      border-color: var(--gold-accent);
    }
    .process-step-num {
      font-family: var(--font-heading);
      font-size: 2.2rem;
      font-weight: 800;
      color: var(--gold-accent);
      line-height: 1;
      margin-bottom: 14px;
      opacity: 0.85;
    }
    .process-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--navy-dark);
      margin-bottom: 10px;
    }
    .process-desc {
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.65;
    }

    /* ======================================================== */
    /* CONSULTATION BANNER                                      */
    /* ======================================================== */
    .cta-consult-section {
      background: linear-gradient(135deg, #1b2836 0%, #2c3844 100%);
      color: #ffffff;
      padding: 90px 0 100px;
      position: relative;
    }
    .cta-box {
      max-width: 900px;
      margin: 0 auto;
      text-align: center;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: var(--radius-card);
      padding: 60px 48px;
      backdrop-filter: blur(12px);
    }
    @media (max-width: 600px) {
      .cta-box {
        padding: 36px 24px;
      }
    }
    .cta-title {
      font-family: var(--font-heading);
      font-size: clamp(2rem, 3.4vw, 2.8rem);
      margin-bottom: 16px;
      font-weight: 700;
    }
    .cta-title span {
      color: var(--gold-accent);
    }
    .cta-text {
      color: #cbd5e1;
      font-size: 1.05rem;
      line-height: 1.7;
      max-width: 680px;
      margin: 0 auto 36px;
    }
    .cta-buttons {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .btn-gold-lg {
      background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
      color: #ffffff !important;
      font-weight: 600;
      padding: 15px 36px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 1rem;
      box-shadow: 0 8px 24px rgba(217, 119, 6, 0.35);
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .btn-gold-lg:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 30px rgba(217, 119, 6, 0.45);
    }
    .btn-outline-light {
      background: rgba(255, 255, 255, 0.08);
      color: #ffffff !important;
      border: 1px solid rgba(255, 255, 255, 0.25);
      font-weight: 600;
      padding: 15px 30px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 1rem;
      transition: background 0.2s, border-color 0.2s;
    }
    .btn-outline-light:hover {
      background: rgba(255, 255, 255, 0.18);
      border-color: rgba(255, 255, 255, 0.5);
    }

    /* ======================================================== */
    /* FOOTER (MATCHES index.html LUXURY FOOTER)                */
    /* ======================================================== */
    .nw-footer {
      background: #080b0e;
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding: 70px 0 30px;
      color: #94a3b8;
    }
    .nw-footer-inner {
      width: min(92vw, 1260px);
      margin: 0 auto;
    }
    .nw-footer-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      padding-bottom: 36px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .nw-footer-brand img {
      height: 48px;
      width: auto;
      object-fit: contain;
    }
    .nw-footer-socials {
      display: flex;
      gap: 12px;
    }
    .nw-social-pill {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #ffffff;
      transition: background 0.2s, color 0.2s;
    }
    .nw-social-pill:hover {
      background: var(--gold-accent);
      color: #ffffff;
    }
    .nw-footer-cols {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 40px;
      padding: 44px 0;
    }
    .nw-col-title {
      font-size: 0.92rem;
      font-weight: 700;
      color: #ffffff;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 20px;
    }
    .nw-col-list {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 11px;
    }
    .nw-col-list a {
      font-size: 0.88rem;
      color: #94a3b8;
      transition: color 0.2s, padding-left 0.2s;
    }
    .nw-col-list a:hover {
      color: var(--gold-accent);
      padding-left: 4px;
    }
    .nw-footer-bottom {
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
      font-size: 0.84rem;
      color: #64748b;
    }
  </style>
</head>
<body>

  <!-- ======================================================== -->
  <!-- FLOATING NAVBAR (ACTIVE ON SERVICES)                     -->
  <!-- ======================================================== -->
  <header class="header" id="mainHeader">
    <div class="holder">
      <div class="header-block">
        <!-- Left Nav Items: Home | About | Properties -->
        <ul class="header-nav-list">
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>

          <!-- Properties Dropdown with Caret Icon -->
          <li class="dropdown-parent" style="position: relative;" onmouseenter="const m=this.querySelector('.prop-dropdown'); if(m) m.style.display='block'; const c=this.querySelector('.prop-caret'); if(c) c.style.transform='rotate(180deg)';" onmouseleave="const m=this.querySelector('.prop-dropdown'); if(m) m.style.display='none'; const c=this.querySelector('.prop-caret'); if(c) c.style.transform='rotate(0deg)';">
            <a href="javascript:void(0)" onclick="const m=this.parentElement.querySelector('.prop-dropdown'); if(m){ m.style.display = (m.style.display==='block' ? 'none' : 'block'); } const c=this.querySelector('.prop-caret'); if(c){ c.style.transform = (m && m.style.display==='block' ? 'rotate(180deg)' : 'rotate(0deg)'); }" style="display: flex; align-items: center; gap: 6px;">
              Properties <i class="fa-solid fa-chevron-down prop-caret" style="font-size: 0.65rem; color: #d97706; transition: transform 0.25s ease;"></i>
            </a>

            <!-- Dropdown Card (Residential & Plotting) -->
            <div class="prop-dropdown" style="display: none; position: absolute; top: 100%; left: 0; min-width: 320px; background: rgba(10, 18, 14, 0.96); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(255,255,255,0.12); border-radius: 12px; box-shadow: 0 16px 36px rgba(0,0,0,0.5); padding: 14px; z-index: 1200; text-transform: none;">
              <!-- Residential Section -->
              <div style="padding-bottom: 10px; border-bottom: 1px solid rgba(255,255,255,0.08);">
                <a href="residential.html" style="display: flex; align-items: center; justify-content: space-between; padding: 8px 10px; border-radius: 8px; text-decoration: none; color: #ffffff; font-weight: 700; transition: background 0.15s ease;" onmouseover="this.style.background='rgba(255,255,255,0.08)';" onmouseout="this.style.background='transparent';">
                  <span style="display: flex; align-items: center; gap: 8px; font-size: 0.85rem; letter-spacing: 1px;">
                    <i class="fa-solid fa-building-user" style="color: #60a5fa;"></i> Residential Properties
                  </span>
                  <span style="font-size: 0.72rem; color: #60a5fa; font-weight: 600;">(3) &rarr;</span>
                </a>
                <div style="padding-left: 28px; display: flex; flex-direction: column; gap: 4px; margin-top: 4px;">
                  <a href="residential-1.html" style="font-size: 0.8rem; color: #94a3b8; text-decoration: none; padding: 2px 0;" onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='#94a3b8';">&bull; Skyview Residency (3-4 BHK)</a>
                  <a href="residential-2.html" style="font-size: 0.8rem; color: #94a3b8; text-decoration: none; padding: 2px 0;" onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='#94a3b8';">&bull; Palm Crest Villas (4 BHK)</a>
                  <a href="residential-3.html" style="font-size: 0.8rem; color: #94a3b8; text-decoration: none; padding: 2px 0;" onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='#94a3b8';">&bull; Skyline Imperial (5 BHK)</a>
                </div>
              </div>

              <!-- Plotting Section -->
              <div style="padding-top: 10px;">
                <a href="plotting.html" style="display: flex; align-items: center; justify-content: space-between; padding: 8px 10px; border-radius: 8px; text-decoration: none; color: #ffffff; font-weight: 700; transition: background 0.15s ease;" onmouseover="this.style.background='rgba(255,255,255,0.08)';" onmouseout="this.style.background='transparent';">
                  <span style="display: flex; align-items: center; gap: 8px; font-size: 0.85rem; letter-spacing: 1px;">
                    <i class="fa-solid fa-map-location-dot" style="color: #d97706;"></i> Plotting Developments
                  </span>
                  <span style="font-size: 0.72rem; color: #d97706; font-weight: 600;">(3) &rarr;</span>
                </a>
                <div style="padding-left: 28px; display: flex; flex-direction: column; gap: 4px; margin-top: 4px;">
                  <a href="plotting-1.html" style="font-size: 0.8rem; color: #94a3b8; text-decoration: none; padding: 2px 0;" onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='#94a3b8';">&bull; Green Valley Township Plots</a>
                  <a href="plotting-2.html" style="font-size: 0.8rem; color: #94a3b8; text-decoration: none; padding: 2px 0;" onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='#94a3b8';">&bull; Royal Meadows Farmhouse Plots</a>
                  <a href="plotting-3.html" style="font-size: 0.8rem; color: #94a3b8; text-decoration: none; padding: 2px 0;" onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='#94a3b8';">&bull; Metro Boulevard Commercial Plots</a>
                </div>
              </div>
            </div>
          </li>
        </ul>

        <!-- Center Uploaded One Roof Properties Logo -->
        <div class="header-logo">
          <a href="index.html">
            <img src="assets/one-roof-logo-white.png" alt="One Roof Properties">
          </a>
        </div>

        <!-- Right Nav Items: Services (Active) | Blog | NRI Support Dropdown | Contact Us -->
        <div class="header-nav-right">
          <ul class="header-nav-list">
            <li><a href="services.html" style="color: #d97706;">Services</a></li>
            <li><a href="blog.html">Blog</a></li>

            <!-- NRI Support Dropdown with Caret Icon -->
            <li class="dropdown-parent" style="position: relative;" onmouseenter="const m=this.querySelector('.nri-dropdown'); if(m) m.style.display='block'; const c=this.querySelector('.nri-caret'); if(c) c.style.transform='rotate(180deg)';" onmouseleave="const m=this.querySelector('.nri-dropdown'); if(m) m.style.display='none'; const c=this.querySelector('.nri-caret'); if(c) c.style.transform='rotate(0deg)';">
              <a href="javascript:void(0)" onclick="const m=this.parentElement.querySelector('.nri-dropdown'); if(m){ m.style.display = (m.style.display==='block' ? 'none' : 'block'); } const c=this.querySelector('.nri-caret'); if(c){ c.style.transform = (m && m.style.display==='block' ? 'rotate(180deg)' : 'rotate(0deg)'); }" style="display: flex; align-items: center; gap: 6px;">
                NRI Support <i class="fa-solid fa-chevron-down nri-caret" style="font-size: 0.65rem; color: #d97706; transition: transform 0.25s ease;"></i>
              </a>

              <!-- Dropdown Card (Legal Information & Loan Help) -->
              <div class="nri-dropdown" style="display: none; position: absolute; top: 100%; right: 0; min-width: 290px; background: rgba(10, 18, 14, 0.96); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border: 1px solid rgba(255,255,255,0.12); border-radius: 12px; box-shadow: 0 16px 36px rgba(0,0,0,0.5); padding: 12px; z-index: 1200; text-transform: none;">
                <!-- Legal Information -->
                <a href="legal-information.html" style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 8px; text-decoration: none; color: #ffffff; transition: background 0.15s ease;" onmouseover="this.style.background='rgba(255,255,255,0.08)';" onmouseout="this.style.background='transparent';">
                  <div style="width: 38px; height: 38px; border-radius: 8px; background: rgba(217, 119, 6, 0.2); display: flex; align-items: center; justify-content: center; color: #d97706; font-size: 1.05rem; flex-shrink: 0;">
                    <i class="fa-solid fa-scale-balanced"></i>
                  </div>
                  <div>
                    <div style="font-weight: 700; font-size: 0.88rem; color: #ffffff; letter-spacing: 0.5px;">Legal Information</div>
                    <div style="font-size: 0.74rem; color: #94a3b8; font-weight: 400; margin-top: 2px;">FEMA, RBI, Title &amp; RERA Guidance</div>
                  </div>
                </a>

                <!-- Separator -->
                <div style="height: 1px; background: rgba(255,255,255,0.08); margin: 6px 0;"></div>

                <!-- Loan Help -->
                <a href="loan-help.html" style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 8px; text-decoration: none; color: #ffffff; transition: background 0.15s ease;" onmouseover="this.style.background='rgba(255,255,255,0.08)';" onmouseout="this.style.background='transparent';">
                  <div style="width: 38px; height: 38px; border-radius: 8px; background: rgba(96, 165, 250, 0.15); display: flex; align-items: center; justify-content: center; color: #60a5fa; font-size: 1.05rem; flex-shrink: 0;">
                    <i class="fa-solid fa-hand-holding-dollar"></i>
                  </div>
                  <div>
                    <div style="font-weight: 700; font-size: 0.88rem; color: #ffffff; letter-spacing: 0.5px;">Loan Help</div>
                    <div style="font-size: 0.74rem; color: #94a3b8; font-weight: 400; margin-top: 2px;">NRI Home Loans, Eligibility &amp; Banking</div>
                  </div>
                </a>
              </div>
            </li>

            <li><a href="contact.html">Contact Us</a></li>
          </ul>
        </div>

        <button class="nav-mobile-btn" onclick="const m=document.getElementById('mobileNavModal'); if(m) m.style.display='flex';" aria-label="Toggle navigation">
          <i class="fa-solid fa-bars"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- ======================================================== -->
  <!-- HERO SECTION                                             -->
  <!-- ======================================================== -->
  <section class="services-hero">
    <div class="hero-glow-accent"></div>
    <div class="container">
      <div class="hero-content">
        <div class="hero-tagline-badge">
          <a href="index.html">Home</a>
          <i class="fa-solid fa-chevron-right" style="font-size: 0.65rem;"></i>
          <span style="color: #ffffff;">Our Services</span>
        </div>

        <h1 class="hero-main-title">
          Bespoke Real Estate Advisory &amp; <span>Asset Solutions</span>
        </h1>
        <p class="hero-main-desc">
          From curated skyline penthouses and high-yield plotting land parcels to global NRI cross-border compliance and institutional home financing, One Roof Properties delivers rigorous diligence, discreet representation, and flawless execution.
        </p>

        <div class="hero-metrics">
          <div class="metric-card">
            <div class="metric-number">₹<em>1,200+</em> Cr</div>
            <div class="metric-label">Real Estate Portfolio Transacted</div>
          </div>
          <div class="metric-card">
            <div class="metric-number"><em>30-Year</em></div>
            <div class="metric-label">Certified Clear Title Guarantee</div>
          </div>
          <div class="metric-card">
            <div class="metric-number"><em>100%</em></div>
            <div class="metric-label">MahaRERA Regulatory Compliance</div>
          </div>
          <div class="metric-card">
            <div class="metric-number"><em>18+</em> Global</div>
            <div class="metric-label">Countries NRI Client Network</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- SERVICES SECTION: 1:1 SQUARE CARDS IN STAGGERED GRID     -->
  <!-- (MATCHING USER'S CLOSE-UP AND FULL GRID SCREENSHOTS)     -->
  <!-- ======================================================== -->
  <section class="services-staggered-section" id="servicesGrid">
    <div class="container">
      
      <!-- Section Header -->
      <div class="section-intro-center">
        <span class="tracker-pill">INTEGRATED REAL ESTATE DISCIPLINES</span>
        <h2 class="section-headline">Comprehensive Services Engineered for <span>High-Value Outcomes</span></h2>
        <p class="section-subtext">
          Explore our signature disciplines below. Cleanly arranged with center visual showcase and alternating advisory cards.
        </p>
      </div>

      <!-- 3-COLUMN STAGGERED GRID (EQUAL 1:1 SQUARES, NO OVERLAP) -->
      <div class="staggered-grid-container">

        <!-- ================= ROW 1: [Spacer] | [Center Photo 1] | [Right Content 1] ================= -->
        <div class="stagger-row type-right" id="service-row-1">
          <!-- Col 1: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>

          <!-- Col 2: Center Photo Square -->
          <div class="stagger-photo-card">
            <img src="assets/pune-luxury-tower.jpg" alt="Luxury Residential Sales &amp; Penthouses" loading="lazy">
            <div class="photo-corner-badge">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </div>
            <div class="photo-bottom-tag">
              <i class="fa-solid fa-crown"></i> Prime Pune Corridors
            </div>
          </div>

          <!-- Col 3: Right Content Square -->
          <a href="residential.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Luxury Residential</h3>
            <div class="card-service-headline">Curated Living Spaces for Generational Comfort.</div>
            <p class="card-service-desc">
              Direct access to Pune's most coveted residential addresses. We represent discerning buyers in acquiring bespoke 3, 4 &amp; 5 BHK luxury residences, duplex penthouses, and private gated estates across Kothrud, Baner, and prime urban corridors.
            </p>
          </a>
        </div>

        <!-- ================= ROW 2: [Left Content 2] | [Center Photo 2] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-2">
          <!-- Col 1: Left Content Square -->
          <a href="plotting.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Sanctioned Plotting</h3>
            <div class="card-service-headline">Strategic Land Parcels with High Appreciation Potential.</div>
            <p class="card-service-desc">
              Secure prime residential plots and strategic commercial parcels engineered for wealth preservation. Every parcel in our portfolio comes master-planned with certified non-agricultural sanctions, demarcated boundaries, and ready infrastructure.
            </p>
          </a>

          <!-- Col 2: Center Photo Square -->
          <div class="stagger-photo-card">
            <img src="assets/pune-luxury-villas.jpg" alt="Sanctioned NA Plotting Developments" loading="lazy">
            <div class="photo-corner-badge">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </div>
            <div class="photo-bottom-tag">
              <i class="fa-solid fa-map-location-dot"></i> Sanctioned NA Layouts
            </div>
          </div>

          <!-- Col 3: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>
        </div>

        <!-- ================= ROW 3: [Spacer] | [Center Photo 3] | [Right Content 3] ================= -->
        <div class="stagger-row type-right" id="service-row-3">
          <!-- Col 1: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>

          <!-- Col 2: Center Photo Square -->
          <div class="stagger-photo-card">
            <img src="assets/loan-hero-bread.jpg" alt="NRI Cross-Border Investment Advisory" loading="lazy">
            <div class="photo-corner-badge">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </div>
            <div class="photo-bottom-tag">
              <i class="fa-solid fa-earth-americas"></i> 100% Remote Advisory
            </div>
          </div>

          <!-- Col 3: Right Content Square -->
          <a href="legal-information.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">NRI Global Advisory</h3>
            <div class="card-service-headline">Frictionless Real Estate Transactions for Global Indians.</div>
            <p class="card-service-desc">
              A specialized international desk eliminating distance and regulatory complexity for NRIs and OCIs residing in the USA, GCC, UK, and Singapore. We manage the entire investment lifecycle with remote documentation, notarization, and adjudication.
            </p>
          </a>
        </div>

        <!-- ================= ROW 4: [Left Content 4] | [Center Photo 4] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-4">
          <!-- Col 1: Left Content Square -->
          <a href="loan-help.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Home Loan Advisory</h3>
            <div class="card-service-headline">Preferential Mortgage Rates from 8.35% p.a.</div>
            <p class="card-service-desc">
              Capitalize on direct institutional banking alliances with State Bank of India, HDFC Bank, ICICI, Axis, and Kotak Mahindra. Our dedicated mortgage officers handle pre-approval underwriting, document audit, and fast-track disbursal.
            </p>
          </a>

          <!-- Col 2: Center Photo Square -->
          <div class="stagger-photo-card">
            <img src="assets/cta-interior-1.jpg" alt="Institutional Home Loan Advisory" loading="lazy">
            <div class="photo-corner-badge">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </div>
            <div class="photo-bottom-tag">
              <i class="fa-solid fa-hand-holding-dollar"></i> ROI From 8.35% p.a.
            </div>
          </div>

          <!-- Col 3: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>
        </div>

        <!-- ================= ROW 5: [Spacer] | [Center Photo 5] | [Right Content 5] ================= -->
        <div class="stagger-row type-right" id="service-row-5">
          <!-- Col 1: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>

          <!-- Col 2: Center Photo Square -->
          <div class="stagger-photo-card">
            <img src="assets/project-3.jpg" alt="Certified Property Valuation &amp; Due Diligence" loading="lazy">
            <div class="photo-corner-badge">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </div>
            <div class="photo-bottom-tag">
              <i class="fa-solid fa-stamp"></i> 30-Year Audit Guarantee
            </div>
          </div>

          <!-- Col 3: Right Content Square -->
          <a href="legal-information.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Title Due Diligence</h3>
            <div class="card-service-headline">Forensic Legal Scrutiny &amp; Certified Property Valuation.</div>
            <p class="card-service-desc">
              Every property represented by One Roof Properties undergoes forensic legal audit by senior empanelled solicitors. We protect our clients with 30-year revenue search reports, 7/12 extract verification, index-II scrutiny, and certified MahaRERA compliance.
            </p>
          </a>
        </div>

        <!-- ================= ROW 6: [Left Content 6] | [Center Photo 6] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-6">
          <!-- Col 1: Left Content Square -->
          <a href="contact.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Asset Management</h3>
            <div class="card-service-headline">Preserving Asset Quality while Compounding Rental Yields.</div>
            <p class="card-service-desc">
              Comprehensive real estate portfolio management for absentee homeowners, ultra-HNIs, and foreign investors. We oversee tenant acquisition for senior corporate executives, maintain property upkeep, and execute profitable exit strategies.
            </p>
          </a>

          <!-- Col 2: Center Photo Square -->
          <div class="stagger-photo-card">
            <img src="assets/opening-3.webp" alt="Corporate Leasing &amp; Asset Management" loading="lazy">
            <div class="photo-corner-badge">
              <i class="fa-solid fa-arrow-up-right-from-square"></i>
            </div>
            <div class="photo-bottom-tag">
              <i class="fa-solid fa-chart-line"></i> Optimized Rental Yields
            </div>
          </div>

          <!-- Col 3: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>
        </div>

      </div>
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- 4-STEP METHODOLOGY SECTION                               -->
  <!-- ======================================================== -->
  <section class="process-section">
    <div class="container">
      <div style="text-align: center; max-width: 720px; margin: 0 auto;">
        <span class="tracker-pill">OUR METHODOLOGY</span>
        <h2 class="section-headline">The 4-Step <span>Execution Process</span></h2>
        <p class="section-subtext">
          A transparent, methodical approach that guarantees precision, privacy, and full regulatory security from discovery to registration.
        </p>
      </div>

      <div class="process-grid">
        <div class="process-card">
          <div class="process-step-num">01</div>
          <h4 class="process-title">Discovery &amp; Profiling</h4>
          <p class="process-desc">
            We assess your lifestyle requirements, capital timeline, and tax considerations to build a bespoke investment thesis.
          </p>
        </div>

        <div class="process-card">
          <div class="process-step-num">02</div>
          <h4 class="process-title">Curated Selection</h4>
          <p class="process-desc">
            Access exclusive pre-vetted residences and land parcels matching your exact parameters with independent valuation benchmark reports.
          </p>
        </div>

        <div class="process-card">
          <div class="process-step-num">03</div>
          <h4 class="process-title">Due Diligence &amp; Terms</h4>
          <p class="process-desc">
            Our empanelled legal team inspects 30-year title records and negotiates preferred terms, payment milestones, and developer warranties.
          </p>
        </div>

        <div class="process-card">
          <div class="process-step-num">04</div>
          <h4 class="process-title">Frictionless Handover</h4>
          <p class="process-desc">
            Complete registry execution, Power of Attorney adjudication, home loan disbursal, and ongoing property asset stewardship.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- DIRECT CONSULTATION BANNER                               -->
  <!-- ======================================================== -->
  <section class="cta-consult-section">
    <div class="container">
      <div class="cta-box">
        <span class="tracker-pill" style="color: #60a5fa;">CONFIDENTIAL REAL ESTATE CONSULTATION</span>
        <h2 class="cta-title">Ready to Discuss Your <span>Real Estate Portfolio?</span></h2>
        <p class="cta-text">
          Connect with a Senior Advisory Partner at One Roof Properties. Whether you are looking to purchase a signature luxury home, invest in strategic land parcels, or structure an NRI acquisition, we provide objective, data-backed guidance.
        </p>

        <div class="cta-buttons">
          <a href="contact.html" class="btn-gold-lg">
            <i class="fa-solid fa-calendar-check"></i> Book Private Consultation
          </a>
          <a href="tel:+919494168733" class="btn-outline-light">
            <i class="fa-solid fa-phone"></i> +91 949 416 8733
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- ======================================================== -->
  <!-- LUXURY FOOTER                                            -->
  <!-- ======================================================== -->
  <footer class="nw-footer">
    <div class="nw-footer-inner">
      <div class="nw-footer-top">
        <a href="index.html" class="nw-footer-brand">
          <img src="assets/one-roof-logo-white.png" alt="One Roof Properties">
        </a>

        <div class="nw-footer-socials">
          <a href="#" class="nw-social-pill" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" class="nw-social-pill" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
          <a href="#" class="nw-social-pill" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="#" class="nw-social-pill" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
        </div>
      </div>

      <div class="nw-footer-cols">
        <div>
          <h4 class="nw-col-title">Properties</h4>
          <ul class="nw-col-list">
            <li><a href="residential.html">Residential Properties</a></li>
            <li><a href="plotting.html">Plotting Developments</a></li>
            <li><a href="residential-1.html">Skyview Residency</a></li>
            <li><a href="residential-2.html">Palm Crest Villas</a></li>
            <li><a href="residential-3.html">Skyline Imperial</a></li>
            <li><a href="plotting-1.html">Green Valley Plots</a></li>
          </ul>
        </div>

        <div>
          <h4 class="nw-col-title">Our Services</h4>
          <ul class="nw-col-list">
            <li><a href="#service-row-1">Luxury Residential Sales</a></li>
            <li><a href="#service-row-2">Sanctioned NA Plotting</a></li>
            <li><a href="#service-row-3">NRI Cross-Border Advisory</a></li>
            <li><a href="#service-row-4">Institutional Home Loans</a></li>
            <li><a href="#service-row-5">Title Verification &amp; Valuation</a></li>
            <li><a href="#service-row-6">Portfolio Asset Management</a></li>
          </ul>
        </div>

        <div>
          <h4 class="nw-col-title">NRI Corner</h4>
          <ul class="nw-col-list">
            <li><a href="nri-corner.html">NRI Advisory Hub</a></li>
            <li><a href="legal-information.html">FEMA &amp; Legal Info</a></li>
            <li><a href="loan-help.html">NRI Loan Help Desk</a></li>
            <li><a href="loan-help.html#emiCalculator">EMI Calculator</a></li>
          </ul>
        </div>

        <div>
          <h4 class="nw-col-title">Contact Us</h4>
          <p style="font-size: 0.88rem; color: #94a3b8; line-height: 1.6; margin-bottom: 8px;">
            <i class="fa-solid fa-location-dot" style="color: var(--gold-accent); margin-right: 6px;"></i> One Roof Tower, Financial District, Pune - 411045
          </p>
          <p style="font-size: 0.88rem; color: #94a3b8; line-height: 1.6; margin-bottom: 8px;">
            <i class="fa-solid fa-phone" style="color: var(--gold-accent); margin-right: 6px;"></i> +91 949 416 8733
          </p>
          <p style="font-size: 0.88rem; color: #94a3b8; line-height: 1.6;">
            <i class="fa-solid fa-envelope" style="color: var(--gold-accent); margin-right: 6px;"></i> contact@oneroofproperties.com
          </p>
        </div>
      </div>

      <div class="nw-footer-bottom">
        <div>&copy; 2026 One Roof Properties Pvt. Ltd. All rights reserved. MahaRERA Registered.</div>
        <div style="display: flex; gap: 18px;">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="legal-information.html">Terms &amp; Disclaimers</a>
          <a href="contact.html">Contact Us</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- ======================================================== -->
  <!-- JAVASCRIPT: NAVBAR SCROLL                                -->
  <!-- ======================================================== -->
  <script>
    // Header Scroll Effect matching home page
    const mainHeader = document.getElementById('mainHeader');
    function updateNavbar() {
      if (!mainHeader) return;
      if (window.scrollY > 40) {
        mainHeader.classList.add('scrolled');
      } else {
        mainHeader.classList.remove('scrolled');
      }
    }
    window.addEventListener('scroll', updateNavbar, { passive: true });
    window.addEventListener('DOMContentLoaded', updateNavbar);
  </script>
</body>
</html>
"""

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_code)

print("services.html updated with 1:1 square cards! File size:", len(services_code))

