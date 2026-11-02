import glob, re
pages = ['residential-2.html', 'residential-3.html', 'residential.html', 'plotting.html', 'plotting-1.html', 'plotting-2.html', 'plotting-3.html', 'nri-corner.html']
for p in pages:
    txt = open(p, 'r', encoding='utf-8').read()
    m = re.search(r'<li><a[^>]*>(?:NRI|NRI Support|NRI Investments)</a></li>', txt, re.IGNORECASE)
    print(p, m.group(0) if m else 'No direct match')
