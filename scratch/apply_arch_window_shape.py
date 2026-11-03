import re

file_path = r'd:\DTG\One-Roof-Properties\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update CSS for desktop project nodes
old_desktop_css = """    .sr-project-node {
      position: relative;
      flex-shrink: 0;
      width: clamp(480px, 46vw, 680px);
      height: clamp(480px, 46vw, 680px);
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      will-change: transform, opacity;
    }
    /* The large outer circle outside the image circle */
    .sr-node-ring {
      position: absolute;
      inset: 0;
      border-radius: 50%;
      border: none !important;
      display: none !important; /* Removed bluish outer circular outline */
      pointer-events: none;
    }
    .sr-project-node:hover .sr-node-ring {
      display: none !important;
    }

    /* Circular Architectural Window Frame (Inner Image Circle that scales Big <-> Small) */
    .sr-node-portal {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(1);
      transform-origin: center center;
      width: clamp(380px, 35vw, 520px);
      height: clamp(380px, 35vw, 520px);
      border-radius: 50%;
      overflow: hidden;
      background: #111a22;
      box-shadow: 0 20px 45px rgba(70, 86, 101, 0.16);
      transition: filter 0.3s ease;
      will-change: transform;
    }
    .sr-node-portal img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      filter: brightness(1);
      transition: transform 0.7s cubic-bezier(0.22, 1, 0.36, 1), filter 0.4s ease;
    }
    .sr-project-node:hover .sr-node-portal img {
      transform: scale(1.08);
      filter: brightness(1.04);
    }

    /* Window Overlay Caption (Project Content on Circle) */
    .sr-node-overlay {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at center, rgba(17, 26, 34, 0.25) 0%, rgba(17, 26, 34, 0.78) 100%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: clamp(18px, 3.5vw, 36px);
      box-sizing: border-box;
      transition: opacity 0.3s ease;
      pointer-events: none;
      z-index: 5;
    }"""

new_desktop_css = """    .sr-project-node {
      position: relative;
      flex-shrink: 0;
      width: clamp(420px, 38vw, 540px);
      height: clamp(520px, 46vw, 650px);
      display: flex;
      align-items: center;
      justify-content: center;
      text-decoration: none;
      will-change: transform, opacity;
    }
    /* The large outer ring outside the image */
    .sr-node-ring {
      position: absolute;
      inset: 0;
      border-radius: 9999px 9999px 0 0;
      border: none !important;
      display: none !important;
      pointer-events: none;
    }
    .sr-project-node:hover .sr-node-ring {
      display: none !important;
    }

    /* Arched Architectural Window Frame (Window Shape like Raheja Vistas Reference) */
    .sr-node-portal {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%) scale(1);
      transform-origin: center center;
      width: clamp(340px, 30vw, 440px);
      height: clamp(470px, 42vw, 590px);
      border-radius: 9999px 9999px 0 0; /* Pure Roman Arched Window Shape */
      overflow: hidden;
      background: #111a22;
      box-shadow: 0 24px 50px rgba(70, 86, 101, 0.18);
      transition: filter 0.3s ease, box-shadow 0.3s ease;
      will-change: transform;
    }
    .sr-node-portal img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      filter: brightness(1);
      transition: transform 0.7s cubic-bezier(0.22, 1, 0.36, 1), filter 0.4s ease;
    }
    .sr-project-node:hover .sr-node-portal img {
      transform: scale(1.08);
      filter: brightness(1.04);
    }
    .sr-project-node:hover .sr-node-portal {
      box-shadow: 0 30px 60px rgba(70, 86, 101, 0.28);
    }

    /* Window Overlay Caption (Project Content on Arch Window) */
    .sr-node-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(17, 26, 34, 0.08) 0%, rgba(17, 26, 34, 0.35) 45%, rgba(17, 26, 34, 0.88) 100%);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
      text-align: center;
      padding: clamp(20px, 3vw, 36px) clamp(16px, 2.5vw, 28px);
      box-sizing: border-box;
      transition: background 0.3s ease, opacity 0.3s ease;
      pointer-events: none;
      z-index: 5;
    }
    .sr-project-node:hover .sr-node-overlay {
      background: linear-gradient(180deg, rgba(17, 26, 34, 0.15) 0%, rgba(17, 26, 34, 0.5) 45%, rgba(17, 26, 34, 0.94) 100%);
    }"""

assert old_desktop_css in html, "Old desktop CSS not found"
html = html.replace(old_desktop_css, new_desktop_css)
print("Replaced desktop CSS")

# 2. Update responsive mobile CSS
old_mobile_css = """      .sr-project-node {
        width: 290px;
        height: 290px;
      }
      .sr-node-portal {
        width: 220px;
        height: 220px;
      }"""

new_mobile_css = """      .sr-project-node {
        width: 270px;
        height: 380px;
      }
      .sr-node-portal {
        width: 240px;
        height: 340px;
        border-radius: 9999px 9999px 0 0;
      }"""

assert old_mobile_css in html, "Old mobile CSS not found"
html = html.replace(old_mobile_css, new_mobile_css)
print("Replaced mobile CSS")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html project cards updated to arched window shape!")

