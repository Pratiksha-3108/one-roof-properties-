file_path = r'd:\DTG\One-Roof-Properties\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update .sr-brand-block and .sr-projects-viewport
old_brand_css = """    .sr-brand-block {
      position: relative;
      z-index: 20;
      width: clamp(380px, 36vw, 560px);
      flex-shrink: 0;
      pointer-events: auto;
    }"""

new_brand_css = """    .sr-brand-block {
      position: relative;
      z-index: 20;
      width: clamp(380px, 36vw, 560px);
      flex-shrink: 0;
      pointer-events: auto;
      background: #FAF8EE; /* Solid cream matching page, guarantees no cards show through */
    }"""

assert old_brand_css in html, "old_brand_css not found"
html = html.replace(old_brand_css, new_brand_css)
print("Updated .sr-brand-block CSS")

old_viewport_css = """    .sr-projects-viewport {
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: visible;
      z-index: 5;
    }"""

new_viewport_css = """    .sr-projects-viewport {
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: visible;
      z-index: 5;
      /* Hard boundary: Never allow any card to enter or overlap the left div words */
      clip-path: inset(-60px 0 -60px clamp(380px, 36vw, 560px));
    }"""

assert old_viewport_css in html, "old_viewport_css not found"
html = html.replace(old_viewport_css, new_viewport_css)
print("Updated .sr-projects-viewport CSS")

# 2. Update updateTrainPositions
old_train_code = """          // Smoothly fade out card only as it exits past active position into left margin
          if (normDist < 0) {
            const exitOpacity = Math.max(0, 1.0 - 1.25 * Math.abs(normDist));
            node.style.opacity = exitOpacity.toFixed(2);
            node.style.pointerEvents = exitOpacity > 0.3 ? 'auto' : 'none';
          } else {
            node.style.opacity = '1';
            node.style.pointerEvents = 'auto';
          }"""

new_train_code = """          // Counter-translate and rapidly dissolve exiting cards so they NEVER go back into left div words
          if (normDist < 0) {
            const holdX = Math.abs(dist) * 0.88;
            node.style.transform = `translate3d(${holdX.toFixed(1)}px, 0, 0)`;
            const exitOpacity = Math.max(0, 1.0 - 3.2 * Math.abs(normDist));
            node.style.opacity = exitOpacity.toFixed(2);
            node.style.pointerEvents = exitOpacity > 0.4 ? 'auto' : 'none';
          } else {
            node.style.transform = 'translate3d(0, 0, 0)';
            node.style.opacity = '1';
            node.style.pointerEvents = 'auto';
          }"""

assert old_train_code in html, "old_train_code not found"
html = html.replace(old_train_code, new_train_code)
print("Updated updateTrainPositions loop")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html updated successfully!")

