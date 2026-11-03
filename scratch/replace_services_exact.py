import re

file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero section CSS if needed (keep hero banner with loan-hero-bread.jpg)
# Let's check if the hero is already the hero banner or if it still has the metrics
if '<div class="hero-metrics">' in html:
    print("Found hero-metrics, updating hero to clean banner...")
    # Replace hero CSS
    hero_css_pattern = re.compile(
        r'/\* =+ HERO =+ \*/.*?/\* =+ SERVICES: STAGGERED CARDS =+ \*/',
        re.DOTALL
    )
    new_hero_css = """/* ===================== HERO BANNER ===================== */
    .services-hero {
      position: relative;
      height: 48vh;
      min-height: 380px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #17222d;
      overflow: hidden;
      text-align: center;
    }
    .hero-banner-bg {
      position: absolute;
      inset: 0;
      background: url('assets/loan-hero-bread.jpg') center center / cover no-repeat;
      filter: brightness(0.72);
      transform: scale(1.02);
    }
    .hero-banner-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(7, 14, 10, 0.45) 0%, rgba(7, 14, 10, 0.72) 100%);
    }
    .hero-banner-content {
      position: relative;
      z-index: 10;
      padding: 0 20px;
      margin-top: 50px;
    }
    .hero-title {
      font-family: var(--font-sans);
      font-size: clamp(2.6rem, 5vw, 3.8rem);
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.5px;
      margin-bottom: 8px;
      line-height: 1.15;
      text-shadow: 0 2px 14px rgba(0, 0, 0, 0.4);
    }
    .hero-breadcrumb {
      font-family: var(--font-sans);
      font-size: 0.98rem;
      color: rgba(255, 255, 255, 0.92);
      font-weight: 400;
      letter-spacing: 0.5px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
      text-shadow: 0 1px 8px rgba(0, 0, 0, 0.5);
    }
    .hero-breadcrumb a {
      color: rgba(255, 255, 255, 0.92);
      text-decoration: none;
      transition: color 0.2s ease;
    }
    .hero-breadcrumb a:hover {
      color: var(--gold-accent);
    }
    .hero-breadcrumb .sep {
      color: rgba(255, 255, 255, 0.75);
      font-size: 1.05rem;
    }

    /* ===================== SERVICES: STAGGERED CARDS ===================== */"""
    
    if hero_css_pattern.search(html):
        html = hero_css_pattern.sub(new_hero_css, html)
        print("Updated hero CSS")
    
    # Replace hero HTML
    hero_html_pattern = re.compile(
        r'<!-- =+ HERO =+ -->\s*<section class="services-hero">.*?</section>',
        re.DOTALL
    )
    new_hero_html = """<!-- ===================== HERO BANNER ===================== -->
  <section class="services-hero">
    <div class="hero-banner-bg"></div>
    <div class="hero-banner-overlay"></div>
    <div class="hero-banner-content">
      <h1 class="hero-title">Services</h1>
      <p class="hero-breadcrumb">
        <a href="index.html">Home</a>
        <span class="sep">&rarr;</span>
        <span>Services</span>
      </p>
    </div>
  </section>"""
    if hero_html_pattern.search(html):
        html = hero_html_pattern.sub(new_hero_html, html)
        print("Updated hero HTML")

# 2. Update CSS for 2-column equal cards (no animation, no hover shift)
services_css_pattern = re.compile(
    r'/\* =+ SERVICES: STAGGERED CARDS =+ \*/.*?/\* =+ 4-STEP PROCESS =+ \*/',
    re.DOTALL
)

new_services_css = """/* ===================== SERVICES: 2-COLUMN EQUAL CARDS ===================== */
    .services-staggered-section {
      background: var(--bg-cream);
      padding: 90px 0 130px;
      position: relative;
    }
    .section-intro-center { text-align: center; max-width: 760px; margin: 0 auto 70px; }
    .tracker-pill {
      font-family: 'Jost', sans-serif;
      font-size: 0.78rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 2.8px;
      color: var(--navy-primary);
      background: rgba(70, 86, 101, 0.08);
      padding: 6px 18px;
      border-radius: var(--radius-pill);
      border: 1px solid rgba(70, 86, 101, 0.12);
      margin-bottom: 16px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }
    .section-headline {
      font-family: var(--font-serif-head);
      font-size: clamp(2.1rem, 3.5vw, 3.2rem);
      color: var(--navy-primary);
      font-weight: 700;
      line-height: 1.2;
      letter-spacing: -0.5px;
      margin-bottom: 16px;
    }
    .section-headline span { color: var(--gold-accent); }
    .section-subtext {
      font-family: 'Jost', sans-serif;
      color: var(--text-muted);
      font-size: 1.05rem;
      font-weight: 400;
      line-height: 1.7;
    }

    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 36px;
      max-width: 1120px;
      width: 100%;
      margin: 0 auto;
    }

    .stagger-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      align-items: stretch;
      width: 100%;
    }

    /* EQUAL SIZE ON BOTH BOXES - mathematically identical 1:1 square ratio, zero animation, zero hover */
    .stagger-content-card,
    .stagger-photo-card {
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: var(--radius-card);
      overflow: hidden;
      box-sizing: border-box;
      transform: none !important;
      transition: none !important;
    }

    /* WHITE CONTENT CARD */
    .stagger-content-card {
      background: var(--bg-white);
      padding: clamp(28px, 3.2vw, 48px);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06);
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-decoration: none;
      cursor: default;
    }
    .stagger-content-card:hover,
    .stagger-photo-card:hover {
      transform: none !important;
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06) !important;
    }

    .card-top-flame-icon {
      color: var(--gold-accent);
      font-size: clamp(1.4rem, 1.8vw, 1.75rem);
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
      line-height: 1.18;
      margin-bottom: clamp(10px, 1.1vw, 14px);
      flex-shrink: 0;
    }
    .card-service-headline {
      font-family: var(--font-serif-head);
      color: var(--navy-primary);
      font-size: clamp(0.98rem, 1.15vw, 1.2rem);
      font-weight: 700;
      line-height: 1.35;
      letter-spacing: -0.2px;
      margin-bottom: clamp(8px, 0.9vw, 12px);
      flex-shrink: 0;
    }
    .card-service-desc {
      font-family: 'Jost', sans-serif;
      color: var(--text-muted);
      font-size: clamp(0.85rem, 0.95vw, 0.98rem);
      font-weight: 400;
      line-height: 1.65;
      margin-bottom: 0;
    }

    /* PHOTO CARD - purely the image, identical size, zero overlay, zero hover */
    .stagger-photo-card {
      background: var(--bg-cream-soft);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06);
      position: relative;
    }
    .stagger-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transform: none !important;
      transition: none !important;
    }

    /* Responsive */
    @media (max-width: 820px) {
      .stagger-row {
        grid-template-columns: 1fr;
        gap: 20px;
      }
      .stagger-content-card {
        aspect-ratio: auto;
        min-height: 320px;
      }
      .stagger-row.type-left .stagger-photo-card {
        order: 2;
      }
      .stagger-row.type-left .stagger-content-card {
        order: 1;
      }
    }

    /* ===================== 4-STEP PROCESS ===================== */"""

assert services_css_pattern.search(html) is not None, "services_css_pattern not found"
html = services_css_pattern.sub(new_services_css, html)
print("Updated services CSS")

# 3. Replace the 6 service rows HTML inside <div class="staggered-grid-container"> ... </div>
grid_pattern = re.compile(
    r'<div class="staggered-grid-container">.*?</div>\s*</div>\s*</section>',
    re.DOTALL
)

new_grid_html = """<div class="staggered-grid-container">

        <!-- ================= ROW 1: Selling Properties & Plots ================= -->
        <div class="stagger-row type-right" id="service-row-1">
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Selling Properties &amp; Plots</h3>
            <div class="card-service-headline">Strategic Representation to Maximize High-Value Asset Realization.</div>
            <p class="card-service-desc">
              Dedicated brokerage and targeted marketing advisory for premium residential homes, bespoke luxury villas, and clear-title plotting layouts. We connect sellers with qualified buyers for discreet, high-value, and seamless transaction closures.
            </p>
          </div>
          <div class="stagger-photo-card">
            <img src="assets/service-selling-properties-plots.jpg" alt="Selling Properties &amp; Plots" loading="lazy">
          </div>
        </div>

        <!-- ================= ROW 2: Reselling and Purchasing ================= -->
        <div class="stagger-row type-left" id="service-row-2">
          <div class="stagger-photo-card">
            <img src="assets/service-reselling-purchasing.jpg" alt="Reselling and Purchasing" loading="lazy">
          </div>
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Reselling and Purchasing</h3>
            <div class="card-service-headline">Seamless Secondary Market Acquisitions &amp; Liquidations.</div>
            <p class="card-service-desc">
              End-to-end guidance for buying and reselling pre-owned residential properties, gated plots, and commercial inventory. From forensic market valuations and physical condition audits to 30-year revenue title search and frictionless deed transfer.
            </p>
          </div>
        </div>

        <!-- ================= ROW 3: Construction Projects ================= -->
        <div class="stagger-row type-right" id="service-row-3">
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Construction Projects</h3>
            <div class="card-service-headline">Turnkey Architectural Execution from Foundation to Key Handover.</div>
            <p class="card-service-desc">
              Complete design-and-build stewardship for custom luxury villas, boutique residential buildings, and modern commercial spaces. We manage master planning, municipal statutory sanctions, premium material sourcing, and rigorous structural quality benchmarks.
            </p>
          </div>
          <div class="stagger-photo-card">
            <img src="assets/service-construction-projects.jpg" alt="Construction Projects" loading="lazy">
          </div>
        </div>

        <!-- ================= ROW 4: Investment Projects ================= -->
        <div class="stagger-row type-left" id="service-row-4">
          <div class="stagger-photo-card">
            <img src="assets/service-investment-projects.jpg" alt="Investment Projects" loading="lazy">
          </div>
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Investment Projects</h3>
            <div class="card-service-headline">Strategic Land &amp; Real Estate Engineered for Wealth Compounding.</div>
            <p class="card-service-desc">
              Curated high-growth investment opportunities in strategic plotting zones, pre-leased commercial assets, and emerging expressway corridors engineered for strong capital appreciation, reliable passive rental yields, and institutional wealth preservation.
            </p>
          </div>
        </div>

        <!-- ================= ROW 5: Redevelopment Projects ================= -->
        <div class="stagger-row type-right" id="service-row-5">
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Redevelopment Projects</h3>
            <div class="card-service-headline">Transforming Legacy Housing Societies into Modern Landmarks.</div>
            <p class="card-service-desc">
              Specialized advisory and turnkey project management for cooperative housing societies and prime urban parcels. We navigate member consensus, developer joint ventures, maximized FSI potential, legal covenants, and guaranteed timely delivery.
            </p>
          </div>
          <div class="stagger-photo-card">
            <img src="assets/service-redevelopment-projects.jpg" alt="Redevelopment Projects" loading="lazy">
          </div>
        </div>

        <!-- ================= ROW 6: Engineer And Contractor Service ================= -->
        <div class="stagger-row type-left" id="service-row-6">
          <div class="stagger-photo-card">
            <img src="assets/service-engineer-contractor.jpg" alt="Engineer And Contractor Service" loading="lazy">
          </div>
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Engineer And Contractor Service</h3>
            <div class="card-service-headline">Licensed Engineering, Structural Audits &amp; Civil Contracting.</div>
            <p class="card-service-desc">
              Empanelled structural engineers, certified civil contractors, and site supervisors ensuring structural durability, MEP installations, green building compliance, and precise on-schedule project completion with zero compromise on safety.
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>"""

assert grid_pattern.search(html) is not None, "grid_pattern not found"
html = grid_pattern.sub(new_grid_html, html)
print("Updated grid HTML")

# 4. Update Footer Our Services links
footer_services_pattern = re.compile(
    r'<h4 class="nw-col-title">Our Services</h4>\s*<ul class="nw-col-list">.*?</ul>',
    re.DOTALL
)

new_footer_services = """<h4 class="nw-col-title">Our Services</h4>
          <ul class="nw-col-list">
            <li><a href="#service-row-1">Selling Properties &amp; Plots</a></li>
            <li><a href="#service-row-2">Reselling &amp; Purchasing</a></li>
            <li><a href="#service-row-3">Construction Projects</a></li>
            <li><a href="#service-row-4">Investment Projects</a></li>
            <li><a href="#service-row-5">Redevelopment Projects</a></li>
            <li><a href="#service-row-6">Engineer &amp; Contractor Service</a></li>
          </ul>"""

if footer_services_pattern.search(html):
    html = footer_services_pattern.sub(new_footer_services, html)
    print("Updated footer links")

# 5. Remove card scroll animation from JS
js_pattern = re.compile(
    r'<script>.*?const mainHeader = document\.getElementById\(\'mainHeader\'\);.*?</script>',
    re.DOTALL
)

new_js = """<script>
    // ---------- Navbar scroll state ----------
    const mainHeader = document.getElementById('mainHeader');
    function updateNavbar() {
      if (!mainHeader) return;
      mainHeader.classList.toggle('scrolled', window.scrollY > 40);
    }
    window.addEventListener('scroll', updateNavbar, { passive: true });
    window.addEventListener('DOMContentLoaded', updateNavbar);
  </script>"""

assert js_pattern.search(html) is not None, "js_pattern not found"
html = js_pattern.sub(new_js, html)
print("Updated JS")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: services.html has been completely updated with the 6 services!")

