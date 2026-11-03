import re

file_path = r'd:\DTG\One-Roof-Properties\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Desktop size
old_desktop = """    .sr-project-node {
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
    }"""

new_desktop = """    .sr-project-node {
      position: relative;
      flex-shrink: 0;
      width: clamp(340px, 30vw, 430px);
      height: clamp(430px, 38vw, 530px);
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
      width: clamp(280px, 24vw, 350px);
      height: clamp(390px, 34vw, 480px);
      border-radius: 9999px 9999px 0 0; /* Pure Roman Arched Window Shape */
      overflow: hidden;
      background: #111a22;
      box-shadow: 0 20px 45px rgba(70, 86, 101, 0.16);
      transition: filter 0.3s ease, box-shadow 0.3s ease;
      will-change: transform;
    }"""

assert old_desktop in html, "Old desktop CSS not found"
html = html.replace(old_desktop, new_desktop)

# 2. Update Mobile size
old_mobile = """      .sr-project-node {
        width: 270px;
        height: 380px;
      }
      .sr-node-portal {
        width: 240px;
        height: 340px;
        border-radius: 9999px 9999px 0 0;
      }"""

new_mobile = """      .sr-project-node {
        width: 230px;
        height: 320px;
      }
      .sr-node-portal {
        width: 200px;
        height: 285px;
        border-radius: 9999px 9999px 0 0;
      }"""

assert old_mobile in html, "Old mobile CSS not found"
html = html.replace(old_mobile, new_mobile)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: Reduced arched window size in index.html!")

