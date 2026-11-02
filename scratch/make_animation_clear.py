with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .stagger-row, .stagger-photo-card, and .stagger-content-card CSS for individual clear animations
old_cards_css = '''    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with minmax(0, 1fr) to prevent right cut-off */
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

    /* 2. IMAGE CARD (PERFECT 1:1 SQUARE WITH SMOOTH TORCH ANIMATION) */
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
      transform-style: preserve-3d;
      perspective: 1000px;
      will-change: transform;
      cursor: pointer;
      transition: box-shadow 0.4s ease, border-color 0.4s ease;
    }
    .stagger-photo-card img {
      position: absolute;
      top: -8%;
      left: -8%;
      width: 116%;
      height: 116%;
      object-fit: cover;
      display: block;
      will-change: transform;
      transition: transform 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }'''

new_cards_css = '''    /* 3-COLUMN ROW: [Col 1] [Col 2] [Col 3] with minmax(0, 1fr) */
    .stagger-row {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 22px;
      align-items: start;
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
    /* EXACT 1:1 SQUARES - CLEAR, SMOOTH TORCH ANIMATIONS       */
    /* ======================================================== */

    /* 1. CONTENT CARD (PERFECT 1:1 SQUARE WITH ENTRANCE & HOVER) */
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
      opacity: 0;
      transform: translateY(50px);
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

    /* 2. IMAGE CARD (CLEARLY VISIBLE SCROLL PARALLAX & 3D TILT) */
    .stagger-photo-card {
      background: #e9ecf1;
      border-radius: var(--radius-card); /* 38px rounded corners */
      width: 100%;
      aspect-ratio: 1 / 1; /* Exact 1:1 square ratio */
      box-sizing: border-box;
      overflow: hidden;
      position: relative;
      border: 1px solid var(--border-card);
      box-shadow: 0 12px 32px rgba(27, 40, 54, 0.06);
      display: block;
      transform-style: preserve-3d;
      perspective: 1000px;
      cursor: pointer;
      opacity: 0;
      transform: translateY(60px) scale(0.92);
      transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), transform 0.85s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.4s ease, border-color 0.4s ease;
      will-change: transform, opacity;
    }
    .stagger-row.is-visible .stagger-photo-card {
      opacity: 1;
      transform: translateY(0) scale(1);
    }
    .stagger-photo-card:hover {
      box-shadow: 0 26px 55px rgba(27, 40, 54, 0.16);
      border-color: rgba(217, 119, 6, 0.4);
    }

    /* The photo inside: oversized by 24% to allow clearly visible smooth parallax glide */
    .stagger-photo-card img {
      position: absolute;
      top: -12%;
      left: -12%;
      width: 124%;
      height: 124%;
      object-fit: cover;
      display: block;
      will-change: transform;
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
      pointer-events: none;
    }
    .stagger-photo-card:hover img {
      filter: contrast(1.04) brightness(1.02);
    }

    /* Subtle light sheen reflection across photo card */
    .stagger-photo-card::after {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 60%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.22), transparent);
      transform: skewX(-25deg);
      transition: left 0.75s ease;
      pointer-events: none;
      z-index: 4;
    }
    .stagger-photo-card:hover::after {
      left: 150%;
    }'''

if old_cards_css in content:
    content = content.replace(old_cards_css, new_cards_css)
    print("Updated cards CSS successfully!")
else:
    print("Cards old CSS not matched directly")

# 2. Update the JavaScript for pronounced, continuous Torch-style animation
old_js_block = '''    // Torch-inspired scroll reveal animation
    const serviceRows = document.querySelectorAll('.stagger-row');
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
        rootMargin: '0px 0px -20px 0px'
      });
      serviceRows.forEach(row => rowObserver.observe(row));
    } else {
      serviceRows.forEach(row => row.classList.add('is-visible'));
    }

    // ========================================================
    // TORCH SENSORS SIGNATURE SMOOTH SCROLL PARALLAX & TILT
    // ========================================================
    const photoCards = document.querySelectorAll('.stagger-photo-card');
    const contentCards = document.querySelectorAll('.stagger-content-card');
    let isTicking = false;

    // 1. Continuous smooth scroll parallax for card images & cards
    function updateTorchScrollParallax() {
      const vh = window.innerHeight;
      photoCards.forEach(card => {
        const rect = card.getBoundingClientRect();
        // Check if card is within or near viewport
        if (rect.bottom >= -150 && rect.top <= vh + 150) {
          const centerDelta = (rect.top + rect.height / 2) - (vh / 2);
          const progress = centerDelta / (vh / 2);
          const clamped = Math.max(-1.1, Math.min(1.1, progress));

          const img = card.querySelector('img');
          if (img && !card.dataset.hovered) {
            // Parallax shift inside the rounded window
            const imgShiftY = clamped * 24; // Smooth 24px vertical motion
            const scale = 1.07 + Math.abs(clamped) * 0.03;
            img.style.transform = `translate3d(0, ${imgShiftY}px, 0) scale(${scale})`;
          }

          if (!card.dataset.hovered) {
            // Subtle card float
            const cardFloatY = clamped * -12;
            card.style.transform = `translate3d(0, ${cardFloatY}px, 0)`;
          }
        }
      });
      isTicking = false;
    }

    window.addEventListener('scroll', () => {
      if (!isTicking) {
        window.requestAnimationFrame(updateTorchScrollParallax);
        isTicking = true;
      }
    }, { passive: true });

    window.addEventListener('DOMContentLoaded', () => {
      updateNavbar();
      updateTorchScrollParallax();
    });

    // 2. Interactive Smooth 3D Tilt on Photo Cards (Exact Torch feel)
    photoCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        card.dataset.hovered = 'true';
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotX = ((y - centerY) / centerY) * -7;
        const rotY = ((x - centerX) / centerX) * 7;

        card.style.transition = 'transform 0.12s ease-out, box-shadow 0.3s ease';
        card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-6px) scale(1.02)`;
        card.style.boxShadow = '0 24px 50px rgba(27, 40, 54, 0.14)';

        const img = card.querySelector('img');
        if (img) {
          img.style.transition = 'transform 0.15s ease-out';
          img.style.transform = `translate3d(${(x - centerX) * 0.04}px, ${(y - centerY) * 0.04}px, 0) scale(1.12)`;
        }
      });

      card.addEventListener('mouseleave', () => {
        card.dataset.hovered = '';
        card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease';
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1)';
        card.style.boxShadow = '0 10px 30px rgba(27, 40, 54, 0.05)';

        const img = card.querySelector('img');
        if (img) {
          img.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        }
        setTimeout(updateTorchScrollParallax, 600);
      });
    });

    // 3. Subtle interactive lift on Content Cards
    contentCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotX = ((y - centerY) / centerY) * -5;
        const rotY = ((x - centerX) / centerX) * 5;

        card.style.transition = 'transform 0.12s ease-out, box-shadow 0.3s ease, border-color 0.3s ease';
        card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-5px)`;
        card.style.boxShadow = '0 20px 45px rgba(27, 40, 54, 0.09)';
        card.style.borderColor = 'var(--gold-accent)';
      });

      card.addEventListener('mouseleave', () => {
        card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.6s ease';
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
        card.style.boxShadow = '0 10px 30px rgba(27, 40, 54, 0.05)';
        card.style.borderColor = 'var(--border-card)';
      });
    });'''

new_js_block = '''    // ========================================================
    // CLEAR & PROMINENT TORCH SENSORS SCROLL PARALLAX & ENTRANCE
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
        threshold: 0.12,
        rootMargin: '0px 0px -40px 0px'
      });
      serviceRows.forEach(row => rowObserver.observe(row));
    } else {
      serviceRows.forEach(row => row.classList.add('is-visible'));
    }

    // 2. Clear, Noticeable Continuous Scroll Parallax (Smooth & Prominent)
    let isTicking = false;
    function updateTorchParallax() {
      const vh = window.innerHeight;
      photoCards.forEach(card => {
        const rect = card.getBoundingClientRect();
        // Check if card is visible or near viewport
        if (rect.bottom >= -100 && rect.top <= vh + 100) {
          // Progress from -1 (top of screen) to +1 (bottom of screen)
          const centerDelta = (rect.top + rect.height / 2) - (vh / 2);
          const progress = centerDelta / (vh / 2);
          const clamped = Math.max(-1.2, Math.min(1.2, progress));

          // PROMINENT PARALLAX:
          // 1) The image inside glides by ±44px with active dynamic scale
          const img = card.querySelector('img');
          if (img && !card.dataset.hovered) {
            const imgShiftY = clamped * 44; // Clearly visible 44px glide
            const zoom = 1.14 + Math.abs(clamped) * 0.06; // Active zoom 1.14 to 1.20
            img.style.transform = `translate3d(0, ${imgShiftY.toFixed(1)}px, 0) scale(${zoom.toFixed(3)})`;
          }

          // 2) The photo card itself floats vertically by ±24px relative to the grid
          if (!card.dataset.hovered) {
            const cardFloatY = clamped * -24; // Noticeable float counter-movement
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
      // Ensure above-fold cards are immediately visible
      serviceRows.forEach(row => {
        const r = row.getBoundingClientRect();
        if (r.top < window.innerHeight * 0.85) {
          row.classList.add('is-visible');
        }
      });
    });

    // 3. Clear, High-Impact 3D Tilt on Photo Card Hover
    photoCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        card.dataset.hovered = 'true';
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotX = ((y - centerY) / centerY) * -10; // 10deg clear 3D tilt
        const rotY = ((x - centerX) / centerX) * 10;

        card.style.transition = 'transform 0.1s ease-out, box-shadow 0.3s ease';
        card.style.transform = `perspective(1000px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateY(-8px) scale(1.03)`;
        card.style.boxShadow = '0 28px 60px rgba(27, 40, 54, 0.18)';

        const img = card.querySelector('img');
        if (img) {
          img.style.transition = 'transform 0.1s ease-out';
          const panX = (x - centerX) * 0.08;
          const panY = (y - centerY) * 0.08;
          img.style.transform = `translate3d(${panX.toFixed(1)}px, ${panY.toFixed(1)}px, 0) scale(1.22)`;
        }

        const badge = card.querySelector('.photo-corner-badge');
        if (badge) {
          badge.style.transform = 'scale(1.15)';
          badge.style.background = 'var(--gold-accent)';
        }
      });

      card.addEventListener('mouseleave', () => {
        card.dataset.hovered = '';
        card.style.transition = 'transform 0.7s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.7s ease';
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1)';
        card.style.boxShadow = '0 12px 32px rgba(27, 40, 54, 0.06)';

        const img = card.querySelector('img');
        if (img) {
          img.style.transition = 'transform 0.7s cubic-bezier(0.16, 1, 0.3, 1)';
        }

        const badge = card.querySelector('.photo-corner-badge');
        if (badge) {
          badge.style.transform = 'scale(1)';
          badge.style.background = 'rgba(15, 23, 42, 0.88)';
        }

        setTimeout(updateTorchParallax, 700);
      });
    });

    // 4. Subtle Tactile Lift on Content Cards
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

if old_js_block in content:
    content = content.replace(old_js_block, new_js_block)
    print("Updated JavaScript successfully!")
else:
    print("Old JS block not matched directly")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html with prominent clear animations!")

