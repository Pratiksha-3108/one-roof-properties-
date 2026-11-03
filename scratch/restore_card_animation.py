import re

file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS
css_pattern = re.compile(
    r'/\* =+ SERVICES:.*?/\* =+ 4-STEP PROCESS =+ \*/',
    re.DOTALL
)

new_css = """/* ===================== SERVICES: 3-COLUMN CENTERED SPINE WITH SLIDE ANIMATION ===================== */
    .services-staggered-section {
      background: var(--bg-cream);
      padding: 90px 0 130px;
      position: relative;
      overflow-x: clip; /* photo cards slide sideways; never cause horizontal scroll */
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
    }

    /* WHITE CONTENT CARD — sits ON TOP so photo slides out from under it */
    .stagger-content-card {
      background: var(--bg-white);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06);
      padding: clamp(22px, 2.2vw, 36px);
      display: flex;
      flex-direction: column;
      justify-content: center;
      text-decoration: none;
      position: relative;
      z-index: 2; /* above photo card */
      cursor: default;
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

    /* PHOTO CARD — slides out from behind the content card on scroll into center column */
    .stagger-photo-card {
      background: var(--bg-cream-soft);
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(70, 86, 101, 0.06);
      position: relative;
      z-index: 1; /* below content card */
      display: block;
      will-change: transform;
      transform: translate3d(0, 0, 0);
    }

    .stagger-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
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
      .stagger-photo-card {
        transform: none !important;
      }
    }
    @media (prefers-reduced-motion: reduce) {
      .stagger-photo-card {
        transform: none !important;
      }
    }

    /* ===================== 4-STEP PROCESS ===================== */"""

assert css_pattern.search(html) is not None, "CSS pattern not found"
html = css_pattern.sub(new_css, html)
print("Updated CSS with slide animation properties")

# 2. Update JavaScript at the bottom
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

    // ---------- Card effect: photo slides out from behind the content card ----------
    // Tuning knobs
    const SLIDE_DISTANCE = 0.55; // how far the photo starts tucked behind the content card (fraction of its width)
    const START_AT = 1.0;  // slide begins when the row's top edge reaches this point of the viewport (1 = bottom edge)
    const SLIDE_SPAN = 0.34; // scroll distance (fraction of viewport height) to finish the slide -> smaller = faster
    const SMOOTHING = 0.16; // 0.05 = very floaty, 0.3 = snappy. Higher = faster catch-up

    const staggerRows = document.querySelectorAll('.stagger-row');
    const mobileQuery = window.matchMedia('(max-width: 680px)');
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const rowState = new Map(); // row -> { photo, cur, target, dir }

    staggerRows.forEach(row => {
      const photo = row.querySelector('.stagger-photo-card');
      if (!photo) return;
      rowState.set(row, {
        photo,
        cur: 0,
        target: 0,
        dir: row.classList.contains('type-right') ? 1 : -1 // right-rows hide photo to the right, left-rows to the left
      });
    });

    function effectDisabled() { return mobileQuery.matches || reducedMotion.matches; }

    // Where each photo SHOULD be (0 = tucked behind, 1 = fully out)
    function computeTargets() {
      const vh = window.innerHeight;
      rowState.forEach((s, row) => {
        const top = row.getBoundingClientRect().top;
        const p = (vh * START_AT - top) / (vh * SLIDE_SPAN);
        s.target = Math.min(1, Math.max(0, p));
      });
    }

    function applyTransform(s) {
      const eased = 1 - Math.pow(1 - s.cur, 3); // ease-out cubic
      const shift = (1 - eased) * s.photo.offsetWidth * SLIDE_DISTANCE * s.dir;
      s.photo.style.transform = `translate3d(${shift.toFixed(2)}px, 0, 0)`;
    }

    // Smooth follow loop: runs only while something is still moving
    let running = false;
    function tick() {
      let moving = false;
      rowState.forEach(s => {
        const diff = s.target - s.cur;
        if (Math.abs(diff) < 0.001) {
          s.cur = s.target;
        } else {
          s.cur += diff * SMOOTHING;
          moving = true;
        }
        applyTransform(s);
      });
      if (moving) {
        requestAnimationFrame(tick);
      } else {
        running = false;
      }
    }
    function startLoop() {
      if (running) return;
      running = true;
      requestAnimationFrame(tick);
    }

    function updateCards(instant) {
      if (effectDisabled()) {
        rowState.forEach(s => { s.photo.style.transform = ''; s.cur = s.target = 1; });
        return;
      }
      computeTargets();
      if (instant) {
        rowState.forEach(s => { s.cur = s.target; applyTransform(s); });
      } else {
        startLoop();
      }
    }

    window.addEventListener('scroll', () => {
      updateNavbar();
      updateCards(false);
    }, { passive: true });

    window.addEventListener('resize', () => updateCards(true));
    mobileQuery.addEventListener('change', () => updateCards(true));
    reducedMotion.addEventListener('change', () => updateCards(true));

    // First paint: place photos instantly (no animation on page load)
    window.addEventListener('DOMContentLoaded', () => { updateNavbar(); updateCards(true); });
    window.addEventListener('load', () => updateCards(true));
  </script>"""

assert js_pattern.search(html) is not None, "JS pattern not found"
html = js_pattern.sub(new_js, html)
print("Updated JS with card slide-out animation")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Card slide-out animation restored!")

