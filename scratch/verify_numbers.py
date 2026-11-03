import urllib.request, re

resp = urllib.request.urlopen('http://localhost:3000/services.html')
assert resp.status == 200
html = resp.read().decode('utf-8')
nums = re.findall(r'<span class="card-service-num">(\d+)</span>', html)
print('Numbers found:', nums)
assert nums == ['01', '02', '03', '04', '05', '06']
assert 'fa-fire-flame-curved' not in html
print('Verified: All 6 cards now use numbers 01-06 with zero flame icons!')

