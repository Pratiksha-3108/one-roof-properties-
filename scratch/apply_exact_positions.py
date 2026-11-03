import re

file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Services CSS to support the exact 3-column layout where image is always in center column
# and left/right box sizes are identical 1:1 squares with no hover or animation.

css_pattern = re.compile(
    r'/\* =+ SERVICES:.*?/\* =+ 4-STEP PROCESS =+ \*/',
    re.DOTALL
)

new_css = """/* ===================== SERVICES: 3-COLUMN CENTERED SPINE ===================== */
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
      gap: 24px;
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
    }

    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 24px;
      align-items: stretch;
      width: 100%;
    }

    .stagger-empty-spacer {
      display: block;
      width: 100%;
      aspect-ratio: 1 / 1;
      pointer-events: none;
    }

    /* ALL BOXES HAVE EXACTLY THE SAME SIZE (1:1 square ratio) */
    .stagger-content-card,
    .stagger-photo-card {
      width: 100%;
      aspect-ratio: 1 / 1;
      border-radius: var(--radius-card);
      overflow: hidden;
      box-sizing: border-box;
      /* Static: no animation, no transform, no transition */
      transform: none !important;
      transition: none !important;
    }

    /* WHITE CONTENT CARD */
    .stagger-content-card {
      background: var(--bg-white);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06);
      padding: clamp(22px, 2.2vw, 36px);
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
      font-size: clamp(1.3rem, 1.6vw, 1.65rem);
      margin-bottom: clamp(10px, 1.2vw, 16px);
      display: inline-block;
      flex-shrink: 0;
    }

    .card-service-title {
      color: var(--gold-accent);
      font-family: 'Jost', sans-serif;
      font-size: clamp(1.3rem, 1.65vw, 1.8rem);
      font-weight: 700;
      letter-spacing: -0.02em;
      line-height: 1.15;
      margin-bottom: clamp(8px, 1vw, 12px);
      flex-shrink: 0;
    }

    .card-service-headline {
      font-family: var(--font-serif-head);
      color: var(--navy-primary);
      font-size: clamp(0.92rem, 1.05vw, 1.12rem);
      font-weight: 700;
      line-height: 1.35;
      letter-spacing: -0.2px;
      margin-bottom: clamp(8px, 0.9vw, 12px);
      flex-shrink: 0;
    }

    .card-service-desc {
      font-family: 'Jost', sans-serif;
      color: var(--text-muted);
      font-size: clamp(0.8rem, 0.88vw, 0.92rem);
      font-weight: 400;
      line-height: 1.6;
      margin-bottom: 0;
    }

    /* PHOTO CARD — centered, identical 1:1 square size, pure image */
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

    /* RESPONSIVE */
    @media (max-width: 992px) {
      .stagger-row {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 20px;
      }
      .stagger-empty-spacer {
        display: none !important;
      }
      .stagger-row.type-left .stagger-photo-card {
        order: 2;
      }
      .stagger-row.type-left .stagger-content-card {
        order: 1;
      }
    }
    @media (max-width: 680px) {
      .stagger-row {
        grid-template-columns: 1fr;
        gap: 16px;
      }
      .stagger-content-card {
        aspect-ratio: auto;
        min-height: 300px;
      }
    }

    /* ===================== 4-STEP PROCESS ===================== */"""

assert css_pattern.search(html) is not None, "CSS pattern not found"
html = css_pattern.sub(new_css, html)
print("Updated CSS")

# 2. Replace the HTML inside <section class="services-staggered-section" id="servicesGrid"> ... </section>
grid_section_pattern = re.compile(
    r'<section class="services-staggered-section" id="servicesGrid">.*?</section>',
    re.DOTALL
)

new_grid_section = """<section class="services-staggered-section" id="servicesGrid">
    <div class="container">

      <div class="section-intro-center">
        <span class="tracker-pill">INTEGRATED REAL ESTATE DISCIPLINES</span>
        <h2 class="section-headline">Comprehensive Services Engineered for <span>High-Value Outcomes</span></h2>
        <p class="section-subtext">
          Explore our signature disciplines below. Cleanly arranged with center visual showcase and alternating advisory cards.
        </p>
      </div>

      <div class="staggered-grid-container">

        <!-- ================= ROW 1: Selling Properties & Plots [Spacer] | [Photo] | [Content] ================= -->
        <div class="stagger-row type-right" id="service-row-1">
          <div class="stagger-empty-spacer"></div>
          <div class="stagger-photo-card">
            <img src="assets/service-selling-properties-plots.jpg" alt="Selling Properties &amp; Plots" loading="lazy">
          </div>
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Selling Properties &amp; Plots</h3>
            <div class="card-service-headline">Strategic Representation to Maximize High-Value Asset Realization.</div>
            <p class="card-service-desc">
              Dedicated brokerage and targeted marketing advisory for premium residential homes, bespoke luxury villas, and clear-title plotting layouts. We connect sellers with qualified buyers for discreet, high-value, and seamless transaction closures.
            </p>
          </div>
        </div>

        <!-- ================= ROW 2: Reselling and Purchasing [Content] | [Photo] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-2">
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Reselling and Purchasing</h3>
            <div class="card-service-headline">Seamless Secondary Market Acquisitions &amp; Liquidations.</div>
            <p class="card-service-desc">
              End-to-end guidance for buying and reselling pre-owned residential properties, gated plots, and commercial inventory. From forensic market valuations and physical condition audits to 30-year revenue title search and frictionless deed transfer.
            </p>
          </div>
          <div class="stagger-photo-card">
            <img src="assets/service-reselling-purchasing.jpg" alt="Reselling and Purchasing" loading="lazy">
          </div>
          <div class="stagger-empty-spacer"></div>
        </div>

        <!-- ================= ROW 3: Construction Projects [Spacer] | [Photo] | [Content] ================= -->
        <div class="stagger-row type-right" id="service-row-3">
          <div class="stagger-empty-spacer"></div>
          <div class="stagger-photo-card">
            <img src="assets/service-construction-projects.jpg" alt="Construction Projects" loading="lazy">
          </div>
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Construction Projects</h3>
            <div class="card-service-headline">Turnkey Architectural Execution from Foundation to Key Handover.</div>
            <p class="card-service-desc">
              Complete design-and-build stewardship for custom luxury villas, boutique residential buildings, and modern commercial spaces. We manage master planning, municipal statutory sanctions, premium material sourcing, and rigorous structural quality benchmarks.
            </p>
          </div>
        </div>

        <!-- ================= ROW 4: Investment Projects [Content] | [Photo] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-4">
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Investment Projects</h3>
            <div class="card-service-headline">Strategic Land &amp; Real Estate Engineered for Wealth Compounding.</div>
            <p class="card-service-desc">
              Curated high-growth investment opportunities in strategic plotting zones, pre-leased commercial assets, and emerging expressway corridors engineered for strong capital appreciation, reliable passive rental yields, and institutional wealth preservation.
            </p>
          </div>
          <div class="stagger-photo-card">
            <img src="assets/service-investment-projects.jpg" alt="Investment Projects" loading="lazy">
          </div>
          <div class="stagger-empty-spacer"></div>
        </div>

        <!-- ================= ROW 5: Redevelopment Projects [Spacer] | [Photo] | [Content] ================= -->
        <div class="stagger-row type-right" id="service-row-5">
          <div class="stagger-empty-spacer"></div>
          <div class="stagger-photo-card">
            <img src="assets/service-redevelopment-projects.jpg" alt="Redevelopment Projects" loading="lazy">
          </div>
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Redevelopment Projects</h3>
            <div class="card-service-headline">Transforming Legacy Housing Societies into Modern Landmarks.</div>
            <p class="card-service-desc">
              Specialized advisory and turnkey project management for cooperative housing societies and prime urban parcels. We navigate member consensus, developer joint ventures, maximized FSI potential, legal covenants, and guaranteed timely delivery.
            </p>
          </div>
        </div>

        <!-- ================= ROW 6: Engineer And Contractor Service [Content] | [Photo] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-6">
          <div class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Engineer And Contractor Service</h3>
            <div class="card-service-headline">Licensed Engineering, Structural Audits &amp; Civil Contracting.</div>
            <p class="card-service-desc">
              Empanelled structural engineers, certified civil contractors, and site supervisors ensuring structural durability, MEP installations, green building compliance, and precise on-schedule project completion with zero compromise on safety.
            </p>
          </div>
          <div class="stagger-photo-card">
            <img src="assets/service-engineer-contractor.jpg" alt="Engineer And Contractor Service" loading="lazy">
          </div>
          <div class="stagger-empty-spacer"></div>
        </div>

      </div>
    </div>
  </section>"""

assert grid_section_pattern.search(html) is not None, "grid_section_pattern not found"
html = grid_section_pattern.sub(new_grid_section, html)
print("Updated grid HTML")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: services.html position restored to exact 3-column layout!")

