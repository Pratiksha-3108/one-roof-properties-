import re

file_path = r'd:\DTG\One-Roof-Properties\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update image in #aboutImageExpandBox
old_img_block = re.compile(
    r'<div class="about-image-expand-box" id="aboutImageExpandBox">.*?</div>',
    re.DOTALL
)

new_img_block = """<div class="about-image-expand-box" id="aboutImageExpandBox">
        <img src="assets/one-roof-office-about.jpg" alt="One Roof Properties Corporate Office" loading="eager" decoding="async">
      </div>"""

assert old_img_block.search(html) is not None, "aboutImageExpandBox not found"
html = old_img_block.sub(new_img_block, html)
print("Updated aboutImageExpandBox image tag")

# 2. Update object-position from center bottom to center center in .about-image-expand-box img
old_css = """    .about-image-expand-box img {
      position: absolute;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center bottom;
    }"""

new_css = """    .about-image-expand-box img {
      position: absolute;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center center;
    }"""

assert old_css in html, "CSS rule for .about-image-expand-box img not found"
html = html.replace(old_css, new_css)
print("Updated CSS object-position to center center")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: index.html About section image successfully updated!")

