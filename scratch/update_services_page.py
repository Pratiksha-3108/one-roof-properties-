import re

file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace CSS from /* ===================== SERVICES: STAGGERED CARDS ===================== */
# to /* ===================== 4-STEP PROCESS ===================== */
css_pattern = re.compile(
    r'/\* ===================== SERVICES: STAGGERED CARDS ===================== \*/.*?/\* ===================== 4-STEP PROCESS ===================== \*/',
    re.DOTALL
)

new_css = """/* ===================== SERVICES: 2-COLUMN EQUAL CARDS ===================== */
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

    .services-grid-container {
      display: flex;
      flex-direction: column;
      gap: 36px;
      max-width: 1120px;
      width: 100%;
      margin: 0 auto;
    }

    .service-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 32px;
      align-items: stretch;
      width: 100%;
    }

    /* EQUAL SIZE ON BOTH BOXES - mathematically identical 1:1 square ratio, zero animation, zero hover */
    .service-content-card,
    .service-photo-card {
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: var(--radius-card);
      overflow: hidden;
      box-sizing: border-box;
      transform: none !important;
      transition: none !important;
    }

    /* WHITE CONTENT CARD */
    .service-content-card {
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
    .service-content-card:hover,
    .service-photo-card:hover {
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
    .service-photo-card {
      background: var(--bg-cream-soft);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06);
      position: relative;
    }
    .service-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transform: none !important;
      transition: none !important;
    }

    /* Responsive */
    @media (max-width: 820px) {
      .service-row {
        grid-template-columns: 1fr;
        gap: 20px;
      }
      .service-content-card {
        aspect-ratio: auto;
        min-height: 320px;
      }
      .service-row.row-reverse .service-photo-card {
        order: 2;
      }
      .service-row.row-reverse .service-content-card {
        order: 1;
      }
    }

    /* ===================== 4-STEP PROCESS ===================== */"""

assert css_pattern.search(content) is not None, "CSS pattern not found"
content = css_pattern.sub(new_css, content)

# Replace the HTML inside <section class="services-staggered-section" id="servicesGrid"> ... </section>
html_pattern = re.compile(
    r'<section class="services-staggered-section" id="servicesGrid">.*?</section>',
    re.DOTALL
)

new_html = """<section class="services-staggered-section" id="servicesGrid">
    <div class="container">

      <div class="section-intro-center">
        <span class="tracker-pill">INTEGRATED REAL ESTATE DISCIPLINES</span>
        <h2 class="section-headline">Comprehensive Services Engineered for <span>High-Value Outcomes</span></h2>
        <p class="section-subtext">
          Explore our signature disciplines below. Cleanly arranged side-by-side with balanced content and visual showcases.
        </p>
      </div>

      <div class="services-grid-container">

        <!-- ================= ROW 1: Selling Properties & Plots ================= -->
        <div class="service-row" id="service-row-1">
          <div class="service-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Selling Properties &amp; Plots</h3>
            <div class="card-service-headline">Strategic Representation to Maximize High-Value Asset Realization.</div>
            <p class="card-service-desc">
              Dedicated brokerage and targeted marketing advisory for premium residential homes, bespoke luxury villas, and clear-title plotting layouts. We connect sellers with qualified buyers for discreet, high-value, and seamless transaction closures.
            </p>
          </div>
          <div class="service-photo-card">
            <img src="assets/service-selling-properties-plots.jpg" alt="Selling Properties &amp; Plots" loading="lazy">
          </div>
        </div>

        <!-- ================= ROW 2: Reselling and Purchasing ================= -->
        <div class="service-row row-reverse" id="service-row-2">
          <div class="service-photo-card">
            <img src="assets/service-reselling-purchasing.jpg" alt="Reselling and Purchasing" loading="lazy">
          </div>
          <div class="service-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Reselling and Purchasing</h3>
            <div class="card-service-headline">Seamless Secondary Market Acquisitions &amp; Liquidations.</div>
            <p class="card-service-desc">
              End-to-end guidance for buying and reselling pre-owned residential properties, gated plots, and commercial inventory. From forensic market valuations and physical condition audits to 30-year revenue title search and frictionless deed transfer.
            </p>
          </div>
        </div>

        <!-- ================= ROW 3: Construction Projects ================= -->
        <div class="service-row" id="service-row-3">
          <div class="service-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Construction Projects</h3>
            <div class="card-service-headline">Turnkey Architectural Execution from Foundation to Key Handover.</div>
            <p class="card-service-desc">
              Complete design-and-build stewardship for custom luxury villas, boutique residential buildings, and modern commercial spaces. We manage master planning, municipal statutory sanctions, premium material sourcing, and rigorous structural quality benchmarks.
            </p>
          </div>
          <div class="service-photo-card">
            <img src="assets/service-construction-projects.jpg" alt="Construction Projects" loading="lazy">
          </div>
        </div>

        <!-- ================= ROW 4: Investment Projects ================= -->
        <div class="service-row row-reverse" id="service-row-4">
          <div class="service-photo-card">
            <img src="assets/service-investment-projects.jpg" alt="Investment Projects" loading="lazy">
          </div>
          <div class="service-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Investment Projects</h3>
            <div class="card-service-headline">Strategic Land &amp; Real Estate Engineered for Wealth Compounding.</div>
            <p class="card-service-desc">
              Curated high-growth investment opportunities in strategic plotting zones, pre-leased commercial assets, and emerging expressway corridors engineered for strong capital appreciation, reliable passive rental yields, and institutional wealth preservation.
            </p>
          </div>
        </div>

        <!-- ================= ROW 5: Redevelopment Projects ================= -->
        <div class="service-row" id="service-row-5">
          <div class="service-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Redevelopment Projects</h3>
            <div class="card-service-headline">Transforming Legacy Housing Societies into Modern Landmarks.</div>
            <p class="card-service-desc">
              Specialized advisory and turnkey project management for cooperative housing societies and prime urban parcels. We navigate member consensus, developer joint ventures, maximized FSI potential, legal covenants, and guaranteed timely delivery.
            </p>
          </div>
          <div class="service-photo-card">
            <img src="assets/service-redevelopment-projects.jpg" alt="Redevelopment Projects" loading="lazy">
          </div>
        </div>

        <!-- ================= ROW 6: Engineer And Contractor Service ================= -->
        <div class="service-row row-reverse" id="service-row-6">
          <div class="service-photo-card">
            <img src="assets/service-engineer-contractor.jpg" alt="Engineer And Contractor Service" loading="lazy">
          </div>
          <div class="service-content-card">
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

assert html_pattern.search(content) is not None, "HTML pattern not found"
content = html_pattern.sub(new_html, content)

# Replace the JS at the bottom (remove card scrolling animation, keep glass navbar scroll)
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

assert js_pattern.search(content) is not None, "JS pattern not found"
content = js_pattern.sub(new_js, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully updated services.html!")
