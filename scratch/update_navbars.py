import re

light_nri_dropdown = '''        <!-- NRI Support Dropdown with Caret Icon -->
        <li class="dropdown-parent" style="position: relative; padding: 8px 0;" onmouseenter="const m=this.querySelector('.nri-dropdown'); if(m) m.style.display='block'; const c=this.querySelector('.nri-caret'); if(c) c.style.transform='rotate(180deg)';" onmouseleave="const m=this.querySelector('.nri-dropdown'); if(m) m.style.display='none'; const c=this.querySelector('.nri-caret'); if(c) c.style.transform='rotate(0deg)';">
          <a href="javascript:void(0)" onclick="const m=this.parentElement.querySelector('.nri-dropdown'); if(m){ m.style.display = (m.style.display==='block' ? 'none' : 'block'); } const c=this.querySelector('.nri-caret'); if(c){ c.style.transform = (m && m.style.display==='block' ? 'rotate(180deg)' : 'rotate(0deg)'); }" style="font-size: 0.95rem; font-weight: 600; color: #334155; text-decoration: none; display: flex; align-items: center; gap: 6px;">
            NRI Support <i class="fa-solid fa-chevron-down nri-caret" style="font-size: 0.72rem; color: #d97706; transition: transform 0.25s ease;"></i>
          </a>

          <!-- Dropdown Card (Legal Information & Loan Help) -->
          <div class="nri-dropdown" style="display: none; position: absolute; top: 100%; right: 0; min-width: 290px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 12px; box-shadow: 0 12px 30px rgba(0,0,0,0.12); padding: 12px; z-index: 1200;">
            <!-- Legal Information -->
            <a href="legal-information.html" style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 8px; text-decoration: none; color: #0f172a; transition: background 0.15s ease;" onmouseover="this.style.background='#f8fafc';" onmouseout="this.style.background='transparent';">
              <div style="width: 38px; height: 38px; border-radius: 8px; background: rgba(217, 119, 6, 0.12); display: flex; align-items: center; justify-content: center; color: #d97706; font-size: 1.05rem; flex-shrink: 0;">
                <i class="fa-solid fa-scale-balanced"></i>
              </div>
              <div>
                <div style="font-weight: 700; font-size: 0.88rem; color: #0f172a; letter-spacing: 0.5px;">Legal Information</div>
                <div style="font-size: 0.74rem; color: #64748b; font-weight: 400; margin-top: 2px;">FEMA, RBI, Title &amp; RERA Guidance</div>
              </div>
            </a>

            <!-- Separator -->
            <div style="height: 1px; background: #e2e8f0; margin: 6px 0;"></div>

            <!-- Loan Help -->
            <a href="loan-help.html" style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; border-radius: 8px; text-decoration: none; color: #0f172a; transition: background 0.15s ease;" onmouseover="this.style.background='#f8fafc';" onmouseout="this.style.background='transparent';">
              <div style="width: 38px; height: 38px; border-radius: 8px; background: rgba(30, 58, 138, 0.1); display: flex; align-items: center; justify-content: center; color: #1e3a8a; font-size: 1.05rem; flex-shrink: 0;">
                <i class="fa-solid fa-hand-holding-dollar"></i>
              </div>
              <div>
                <div style="font-weight: 700; font-size: 0.88rem; color: #0f172a; letter-spacing: 0.5px;">Loan Help</div>
                <div style="font-size: 0.74rem; color: #64748b; font-weight: 400; margin-top: 2px;">NRI Home Loans, Eligibility &amp; Banking</div>
              </div>
            </a>
          </div>
        </li>'''

pages = ['residential-2.html', 'residential-3.html', 'residential.html', 'plotting.html', 'plotting-1.html', 'plotting-2.html', 'plotting-3.html', 'nri-corner.html']

for p in pages:
    txt = open(p, 'r', encoding='utf-8').read()
    pattern = re.compile(r'<li>\s*<a href="nri-corner\.html"[^>]*>.*?</a>\s*</li>', re.DOTALL | re.IGNORECASE)
    if pattern.search(txt):
        new_txt = pattern.sub(light_nri_dropdown, txt, count=1)
        open(p, 'w', encoding='utf-8').write(new_txt)
        print(f'Updated {p}')
    else:
        print(f'Pattern not found in {p}')

