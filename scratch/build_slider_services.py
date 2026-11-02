import re

# Read current services.html
with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. New CSS for Card Size Difference & Slider Effect
css_start = html.find('/* Container for Staggered Rows */')
css_end = html.find('/* ======================================================== */\n    /* RESPONSIVE LAYOUT', css_start)

new_cards_styling = '''/* Container for Staggered Rows */
    .staggered-grid-container {
      display: flex;
      flex-direction: column;
      gap: 32px;
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
      box-sizing: border-box;
    }

    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with center alignment for card size difference */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 26px;
      align-items: center; /* Creates the distinct Torch vertical offset between tall & compact cards */
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
    .stagger-content-card:hover {
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

    /* 2. IMAGE CARD (TALLER LUXURY CARD WITH IMAGE SLIDER EFFECT) */
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
    }
    .stagger-row.is-visible .stagger-photo-card {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
    .stagger-photo-card:hover {
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
    }

    /* SLIDER CONTROLS: PREV / NEXT CHEVRONS */
    .slider-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      cursor: pointer;
      z-index: 10;
      opacity: 0;
      transition: opacity 0.3s ease, background 0.2s ease, transform 0.2s ease;
    }
    .slider-btn.prev-btn {
      left: 14px;
    }
    .slider-btn.next-btn {
      right: 14px;
    }
    .stagger-photo-card:hover .slider-btn {
      opacity: 1;
    }
    .slider-btn:hover {
      background: var(--gold-accent);
      transform: translateY(-50%) scale(1.1);
    }

    /* SLIDER PAGINATION DOTS */
    .slider-dots {
      position: absolute;
      bottom: 18px;
      right: 20px;
      display: flex;
      gap: 6px;
      z-index: 10;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      padding: 5px 9px;
      border-radius: 20px;
      border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .slider-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.45);
      cursor: pointer;
      transition: all 0.3s ease;
    }
    .slider-dot.active {
      width: 18px;
      border-radius: 10px;
      background: var(--gold-accent);
    }

    /* Corner badge */
    .photo-corner-badge {
      position: absolute;
      top: 20px;
      right: 20px;
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      border: 1px solid rgba(255, 255, 255, 0.15);
      z-index: 8;
      transition: transform 0.25s, background 0.25s;
    }
    .stagger-photo-card:hover .photo-corner-badge {
      transform: scale(1.1);
      background: var(--gold-accent);
    }

    /* Bottom location tag */
    .photo-bottom-tag {
      position: absolute;
      bottom: 18px;
      left: 20px;
      z-index: 8;
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
    '''

html = html[:css_start] + new_cards_styling + html[css_end:]
print("CSS replaced!")

# 2. Update Grid Markup with 6 rows containing Sliders & Card Size Difference
grid_start = html.find('<!-- 3-COLUMN STAGGERED GRID')
grid_end = html.find('<!-- ======================================================== -->\n  <!-- METHODOLOGY / 4-STEP PROCESS')

new_grid_html = '''<!-- 3-COLUMN STAGGERED GRID (CARD SIZE DIFFERENCE & SLIDER EFFECT) -->
      <div class="staggered-grid-container">

        <!-- ================= ROW 1: [Spacer] | [Tall Photo Slider 1] | [Compact Content 1] ================= -->
        <div class="stagger-row type-right" id="service-row-1">
          <!-- Col 1: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>

          <!-- Col 2: Tall Photo Card with Slider Effect -->
          <div class="stagger-photo-card card-slider-container" data-slider-id="slider-1">
            <div class="slider-track">
              <div class="slider-slide"><img src="assets/pune-luxury-tower.jpg" alt="Skyline Towers" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/cta-interior-1.jpg" alt="Luxury Living Room" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/opening-1.webp" alt="Penthouse Architecture" loading="lazy"></div>
            </div>
            <div class="photo-corner-badge"><i class="fa-solid fa-arrow-up-right-from-square"></i></div>
            <button class="slider-btn prev-btn" aria-label="Previous Slide" onclick="event.preventDefault(); event.stopPropagation(); slidePrev(this);"><i class="fa-solid fa-chevron-left"></i></button>
            <button class="slider-btn next-btn" aria-label="Next Slide" onclick="event.preventDefault(); event.stopPropagation(); slideNext(this);"><i class="fa-solid fa-chevron-right"></i></button>
            <div class="slider-dots">
              <span class="slider-dot active" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 0);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 1);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 2);"></span>
            </div>
            <div class="photo-bottom-tag"><i class="fa-solid fa-crown"></i> Prime Pune Corridors</div>
          </div>

          <!-- Col 3: Compact Content Square -->
          <a href="residential.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Luxury Residential</h3>
            <div class="card-service-headline">Curated Living Spaces for Generational Comfort.</div>
            <p class="card-service-desc">
              Direct access to Pune's most coveted residential addresses. We represent discerning buyers in acquiring bespoke 3, 4 &amp; 5 BHK luxury residences, duplex penthouses, and private gated estates across Kothrud, Baner, and prime urban corridors.
            </p>
          </a>
        </div>

        <!-- ================= ROW 2: [Compact Content 2] | [Tall Photo Slider 2] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-2">
          <!-- Col 1: Compact Content Square -->
          <a href="plotting.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Sanctioned Plotting</h3>
            <div class="card-service-headline">Strategic Land Parcels with High Appreciation Potential.</div>
            <p class="card-service-desc">
              Secure prime residential plots and strategic commercial parcels engineered for wealth preservation. Every parcel in our portfolio comes master-planned with certified non-agricultural sanctions, demarcated boundaries, and ready infrastructure.
            </p>
          </a>

          <!-- Col 2: Tall Photo Card with Slider Effect -->
          <div class="stagger-photo-card card-slider-container" data-slider-id="slider-2">
            <div class="slider-track">
              <div class="slider-slide"><img src="assets/pune-luxury-villas.jpg" alt="Villa Estates" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/project-1.jpg" alt="Green Valley Plots" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/realestate23.webp" alt="Sanctioned NA Land" loading="lazy"></div>
            </div>
            <div class="photo-corner-badge"><i class="fa-solid fa-arrow-up-right-from-square"></i></div>
            <button class="slider-btn prev-btn" aria-label="Previous Slide" onclick="event.preventDefault(); event.stopPropagation(); slidePrev(this);"><i class="fa-solid fa-chevron-left"></i></button>
            <button class="slider-btn next-btn" aria-label="Next Slide" onclick="event.preventDefault(); event.stopPropagation(); slideNext(this);"><i class="fa-solid fa-chevron-right"></i></button>
            <div class="slider-dots">
              <span class="slider-dot active" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 0);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 1);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 2);"></span>
            </div>
            <div class="photo-bottom-tag"><i class="fa-solid fa-map-location-dot"></i> Sanctioned NA Layouts</div>
          </div>

          <!-- Col 3: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>
        </div>

        <!-- ================= ROW 3: [Spacer] | [Tall Photo Slider 3] | [Compact Content 3] ================= -->
        <div class="stagger-row type-right" id="service-row-3">
          <!-- Col 1: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>

          <!-- Col 2: Tall Photo Card with Slider Effect -->
          <div class="stagger-photo-card card-slider-container" data-slider-id="slider-3">
            <div class="slider-track">
              <div class="slider-slide"><img src="assets/loan-hero-bread.jpg" alt="NRI Luxury Property" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/project-2.jpg" alt="Signature Estate" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/opening-2.webp" alt="Luxury Living" loading="lazy"></div>
            </div>
            <div class="photo-corner-badge"><i class="fa-solid fa-arrow-up-right-from-square"></i></div>
            <button class="slider-btn prev-btn" aria-label="Previous Slide" onclick="event.preventDefault(); event.stopPropagation(); slidePrev(this);"><i class="fa-solid fa-chevron-left"></i></button>
            <button class="slider-btn next-btn" aria-label="Next Slide" onclick="event.preventDefault(); event.stopPropagation(); slideNext(this);"><i class="fa-solid fa-chevron-right"></i></button>
            <div class="slider-dots">
              <span class="slider-dot active" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 0);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 1);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 2);"></span>
            </div>
            <div class="photo-bottom-tag"><i class="fa-solid fa-earth-americas"></i> Global NRI Hub</div>
          </div>

          <!-- Col 3: Compact Content Square -->
          <a href="nri-corner.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">NRI Global Advisory</h3>
            <div class="card-service-headline">Frictionless Real Estate Transactions for Global Indians.</div>
            <p class="card-service-desc">
              Cross-border investment advisory tailored for Non-Resident Indians across the GCC, USA, UK, and Singapore. We handle FEMA statutory compliance, repatriation via NRE/NRO accounts, verified Power of Attorney, and virtual site inspections.
            </p>
          </a>
        </div>

        <!-- ================= ROW 4: [Compact Content 4] | [Tall Photo Slider 4] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-4">
          <!-- Col 1: Compact Content Square -->
          <a href="loan-help.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Home Loan Advisory</h3>
            <div class="card-service-headline">Preferential Mortgage Rates from 8.35% p.a.</div>
            <p class="card-service-desc">
              Fast-track institutional mortgage approvals through our premier banking desk. As empanelled partners with SBI, HDFC, ICICI, and Axis Bank, we secure preferential interest rates, loan sanctions up to 85% of property value, and fast-track processing.
            </p>
          </a>

          <!-- Col 2: Tall Photo Card with Slider Effect -->
          <div class="stagger-photo-card card-slider-container" data-slider-id="slider-4">
            <div class="slider-track">
              <div class="slider-slide"><img src="assets/cta-interior-2.jpg" alt="Luxury Modern Villa" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/project-3.jpg" alt="Residential High-Rise" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/realestate24.webp" alt="Prime Property" loading="lazy"></div>
            </div>
            <div class="photo-corner-badge"><i class="fa-solid fa-arrow-up-right-from-square"></i></div>
            <button class="slider-btn prev-btn" aria-label="Previous Slide" onclick="event.preventDefault(); event.stopPropagation(); slidePrev(this);"><i class="fa-solid fa-chevron-left"></i></button>
            <button class="slider-btn next-btn" aria-label="Next Slide" onclick="event.preventDefault(); event.stopPropagation(); slideNext(this);"><i class="fa-solid fa-chevron-right"></i></button>
            <div class="slider-dots">
              <span class="slider-dot active" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 0);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 1);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 2);"></span>
            </div>
            <div class="photo-bottom-tag"><i class="fa-solid fa-percent"></i> 8.35% Banking Desk</div>
          </div>

          <!-- Col 3: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>
        </div>

        <!-- ================= ROW 5: [Spacer] | [Tall Photo Slider 5] | [Compact Content 5] ================= -->
        <div class="stagger-row type-right" id="service-row-5">
          <!-- Col 1: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>

          <!-- Col 2: Tall Photo Card with Slider Effect -->
          <div class="stagger-photo-card card-slider-container" data-slider-id="slider-5">
            <div class="slider-track">
              <div class="slider-slide"><img src="assets/cta-building-luxury.jpg" alt="Commercial &amp; Residential Towers" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/project-4.jpg" alt="Master Planned Development" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/opening-3.webp" alt="Tower Complex" loading="lazy"></div>
            </div>
            <div class="photo-corner-badge"><i class="fa-solid fa-arrow-up-right-from-square"></i></div>
            <button class="slider-btn prev-btn" aria-label="Previous Slide" onclick="event.preventDefault(); event.stopPropagation(); slidePrev(this);"><i class="fa-solid fa-chevron-left"></i></button>
            <button class="slider-btn next-btn" aria-label="Next Slide" onclick="event.preventDefault(); event.stopPropagation(); slideNext(this);"><i class="fa-solid fa-chevron-right"></i></button>
            <div class="slider-dots">
              <span class="slider-dot active" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 0);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 1);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 2);"></span>
            </div>
            <div class="photo-bottom-tag"><i class="fa-solid fa-scale-balanced"></i> 30-Year Audit Guarantee</div>
          </div>

          <!-- Col 3: Compact Content Square -->
          <a href="legal-information.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Title Due Diligence</h3>
            <div class="card-service-headline">Forensic Legal Scrutiny &amp; Certified Property Valuation.</div>
            <p class="card-service-desc">
              Every property represented by One Roof Properties undergoes forensic legal audit by senior empanelled solicitors. We protect our clients with 30-year revenue search reports, 7/12 extract verification, index-II scrutiny, and certified MahaRERA compliance.
            </p>
          </a>
        </div>

        <!-- ================= ROW 6: [Compact Content 6] | [Tall Photo Slider 6] | [Spacer] ================= -->
        <div class="stagger-row type-left" id="service-row-6">
          <!-- Col 1: Compact Content Square -->
          <a href="residential.html" class="stagger-content-card">
            <i class="fa-solid fa-fire-flame-curved card-top-flame-icon"></i>
            <h3 class="card-service-title">Asset Management</h3>
            <div class="card-service-headline">Preserving Asset Quality while Compounding Rental Yields.</div>
            <p class="card-service-desc">
              Holistic property management for high-net-worth individuals and NRI property owners. Our end-to-end stewardship includes verified tenant onboarding, routine physical asset maintenance, periodic digital inspection audits, and timely lease renewals.
            </p>
          </a>

          <!-- Col 2: Tall Photo Card with Slider Effect -->
          <div class="stagger-photo-card card-slider-container" data-slider-id="slider-6">
            <div class="slider-track">
              <div class="slider-slide"><img src="assets/cta-interior-3.jpg" alt="Interior Penthouse Suite" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/project-5.jpg" alt="Modern Residence" loading="lazy"></div>
              <div class="slider-slide"><img src="assets/realestate25.webp" alt="Portfolio Estate" loading="lazy"></div>
            </div>
            <div class="photo-corner-badge"><i class="fa-solid fa-arrow-up-right-from-square"></i></div>
            <button class="slider-btn prev-btn" aria-label="Previous Slide" onclick="event.preventDefault(); event.stopPropagation(); slidePrev(this);"><i class="fa-solid fa-chevron-left"></i></button>
            <button class="slider-btn next-btn" aria-label="Next Slide" onclick="event.preventDefault(); event.stopPropagation(); slideNext(this);"><i class="fa-solid fa-chevron-right"></i></button>
            <div class="slider-dots">
              <span class="slider-dot active" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 0);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 1);"></span>
              <span class="slider-dot" onclick="event.preventDefault(); event.stopPropagation(); goToSlide(this, 2);"></span>
            </div>
            <div class="photo-bottom-tag"><i class="fa-solid fa-shield-halved"></i> Turnkey Stewardship</div>
          </div>

          <!-- Col 3: Empty Spacer -->
          <div class="stagger-empty-spacer"></div>
        </div>

      </div>
    </div>
  </section>
  '''

html = html[:grid_start] + new_grid_html + html[grid_end:]
print("Grid replaced!")

# 3. Update JavaScript section with Slider Engine + Torch Scroll Animation
js_start = html.find('// ========================================================')
js_end = html.find('</script>', js_start)

new_js = '''// ========================================================
    // CLEAR & PROMINENT TORCH SENSORS SCROLL & SLIDER ENGINE
    // ========================================================
    const serviceRows = document.querySelectorAll('.stagger-row');
    const photoCards = document.querySelectorAll('.stagger-photo-card');
    const contentCards = document.querySelectorAll('.stagger-content-card');

    // 1. Staggered Scroll Entrance Reveal
    if ('IntersectionObserver' in window) {
      const rowObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            obs.unobserve(entry.target);
          }
        });
      }, {
        threshold: 0.10,
        rootMargin: '0px 0px -40px 0px'
      });
      serviceRows.forEach(row => rowObserver.observe(row));
    } else {
      serviceRows.forEach(row => row.classList.add('is-visible'));
    }

    // 2. IMAGE CARD SLIDER ENGINE (Smooth slide transitions & auto-play)
    const sliders = document.querySelectorAll('.card-slider-container');
    const sliderStates = new Map();

    sliders.forEach((container, idx) => {
      const track = container.querySelector('.slider-track');
      const slides = container.querySelectorAll('.slider-slide');
      const dots = container.querySelectorAll('.slider-dot');
      sliderStates.set(container, {
        currentIndex: 0,
        total: slides.length,
        track: track,
        dots: dots,
        timer: null
      });

      // Auto-slide every 4.5s with staggered start per card
      function startAutoSlide() {
        const state = sliderStates.get(container);
        if (state.timer) clearInterval(state.timer);
        state.timer = setInterval(() => {
          if (!container.dataset.hovered) {
            goToSlideIndex(container, (state.currentIndex + 1) % state.total);
          }
        }, 4200 + (idx * 500));
      }
      startAutoSlide();

      // Pause on hover
      container.addEventListener('mouseenter', () => {
        container.dataset.hovered = 'true';
      });
      container.addEventListener('mouseleave', () => {
        container.dataset.hovered = '';
      });
    });

    function goToSlideIndex(container, targetIndex) {
      const state = sliderStates.get(container);
      if (!state) return;
      state.currentIndex = targetIndex;
      state.track.style.transform = `translateX(-${targetIndex * 100}%)`;
      state.dots.forEach((dot, i) => {
        if (i === targetIndex) {
          dot.classList.add('active');
        } else {
          dot.classList.remove('active');
        }
      });
    }

    window.slidePrev = function(btn) {
      const container = btn.closest('.card-slider-container');
      const state = sliderStates.get(container);
      if (!state) return;
      const nextIdx = (state.currentIndex - 1 + state.total) % state.total;
      goToSlideIndex(container, nextIdx);
    };

    window.slideNext = function(btn) {
      const container = btn.closest('.card-slider-container');
      const state = sliderStates.get(container);
      if (!state) return;
      const nextIdx = (state.currentIndex + 1) % state.total;
      goToSlideIndex(container, nextIdx);
    };

    window.goToSlide = function(dot, targetIndex) {
      const container = dot.closest('.card-slider-container');
      goToSlideIndex(container, targetIndex);
    };

    // 3. Clear, Noticeable Continuous Scroll Parallax (Smooth & Prominent)
    let isTicking = false;
    function updateTorchParallax() {
      const vh = window.innerHeight;
      photoCards.forEach(card => {
        const rect = card.getBoundingClientRect();
        // Check if card is visible or near viewport
        if (rect.bottom >= -100 && rect.top <= vh + 100) {
          const centerDelta = (rect.top + rect.height / 2) - (vh / 2);
          const progress = centerDelta / (vh / 2);
          const clamped = Math.max(-1.2, Math.min(1.2, progress));

          // Parallax float on the taller image card
          if (!card.dataset.hovered) {
            const cardFloatY = clamped * -26; // Prominent 26px float
            card.style.transform = `translate3d(0, ${cardFloatY.toFixed(1)}px, 0)`;
          }
        }
      });
      isTicking = false;
    }

    window.addEventListener('scroll', () => {
      if (!isTicking) {
        window.requestAnimationFrame(updateTorchParallax);
        isTicking = true;
      }
    }, { passive: true });

    window.addEventListener('DOMContentLoaded', () => {
      updateNavbar();
      updateTorchParallax();
      serviceRows.forEach(row => {
        const r = row.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.85) {
          row.classList.add('is-visible');
        }
      });
    });

    // 4. Smooth 3D Perspective Tilt on Hover
    photoCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        card.dataset.hovered = 'true';
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotX = ((y - centerY) / centerY) * -8;
        const rotY = ((x - centerX) / centerX) * 8;

        card.style.transition = 'transform 0.1s ease-out, box-shadow 0.3s ease';
        card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-8px) scale(1.02)`;
        card.style.boxShadow = '0 28px 60px rgba(27, 40, 54, 0.18)';
      });

      card.addEventListener('mouseleave', () => {
        card.dataset.hovered = '';
        card.style.transition = 'transform 0.7s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.7s ease';
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1)';
        card.style.boxShadow = '0 14px 36px rgba(27, 40, 54, 0.07)';
        setTimeout(updateTorchParallax, 700);
      });
    });

    // 5. Subtle Tactile Lift on Content Cards
    contentCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotX = ((y - centerY) / centerY) * -6;
        const rotY = ((x - centerX) / centerX) * 6;

        card.style.transition = 'transform 0.1s ease-out, box-shadow 0.3s ease, border-color 0.3s ease';
        card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-6px)`;
        card.style.boxShadow = '0 24px 50px rgba(27, 40, 54, 0.12)';
        card.style.borderColor = 'var(--gold-accent)';
      });

      card.addEventListener('mouseleave', () => {
        card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.6s ease';
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
        card.style.boxShadow = '0 10px 30px rgba(27, 40, 54, 0.05)';
        card.style.borderColor = 'var(--border-card)';
      });
    });'''

html = html[:js_start] + new_js + html[js_end:]
print("JavaScript replaced!")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved updated services.html successfully!")
