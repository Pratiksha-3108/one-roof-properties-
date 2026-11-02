with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update stagger-photo-card CSS
old_photo_css = '''    /* 2. IMAGE CARD (PERFECT 1:1 SQUARE MATCHING EXACT DIMENSIONS) */
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

new_photo_css = '''    /* 2. IMAGE CARD (PERFECT 1:1 SQUARE WITH SMOOTH TORCH ANIMATION) */
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

if old_photo_css in content:
    content = content.replace(old_photo_css, new_photo_css)
    print("Replaced photo card CSS")
else:
    print("Photo card old CSS not matched")

# 2. Update script section with full Torch Sensors animation suite
old_script = '''    // Torch-inspired scroll reveal animation
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
        threshold: 0.12,
        rootMargin: '0px 0px -30px 0px'
      });
      serviceRows.forEach(row => rowObserver.observe(row));
    } else {
      serviceRows.forEach(row => row.classList.add('is-visible'));
    }'''

new_script = '''    // Torch-inspired scroll reveal animation
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

if old_script in content:
    content = content.replace(old_script, new_script)
    print("Replaced script successfully!")
else:
    print("Script old text not matched")

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved updated services.html with Torch animation!")

