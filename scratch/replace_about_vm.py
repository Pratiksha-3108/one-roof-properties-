file_path = r'd:\DTG\One-Roof-Properties\about.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

target1 = """        <!-- Image 1: Our Vision (Starts Large Center-Left -> Shrinks to Top-Left Thumbnail on Scroll) -->
        <div class="vm-img-card" id="vmImg1" title="Our Vision" style="left: 23.5%; top: 12%; width: 31%; height: 76%; border-radius: 26px; z-index: 3;">
          <img src="assets/realestate23.webp" alt="Our Vision – Making Property Dreams a Reality" loading="eager" decoding="async">
        </div>

        <!-- Image 2: Our Mission (Starts Small Bottom-Right Thumbnail -> Expands to Large Center-Left on Scroll) -->
        <div class="vm-img-card" id="vmImg2" title="Our Mission" style="left: 59.5%; top: 72%; width: 9.2%; height: 18.5%; border-radius: 14px; z-index: 4;">
          <img src="assets/realestate24.webp" alt="Our Mission – Simplifying Every Step" loading="eager" decoding="async">
        </div>"""

# Let's inspect the exact lines around vmImg1 in html
import re
pattern = re.compile(
    r'<div class="vm-img-card" id="vmImg1".*?</div>\s*<!--.*?-->\s*<div class="vm-img-card" id="vmImg2".*?</div>',
    re.DOTALL
)

m = pattern.search(html)
assert m is not None, "vmImg block not found"
print("Found block:")
print(m.group(0))

new_block = """<div class="vm-img-card" id="vmImg1" title="Our Vision" style="left: 23.5%; top: 12%; width: 31%; height: 76%; border-radius: 26px; z-index: 3;">
          <img src="assets/about-vision.jpg" alt="Our Vision – Making Property Dreams a Reality" loading="eager" decoding="async">
        </div>

        <!-- Image 2: Our Mission (Starts Small Bottom-Right Thumbnail -> Expands to Large Center-Left on Scroll) -->
        <div class="vm-img-card" id="vmImg2" title="Our Mission" style="left: 59.5%; top: 72%; width: 9.2%; height: 18.5%; border-radius: 14px; z-index: 4;">
          <img src="assets/about-mission.jpg" alt="Our Mission – Simplifying Every Step" loading="eager" decoding="async">
        </div>"""

html = pattern.sub(new_block, html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: about.html vision and mission images replaced!")

