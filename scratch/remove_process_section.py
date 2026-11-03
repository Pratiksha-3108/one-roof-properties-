file_path = r'd:\DTG\One-Roof-Properties\services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- ===================== 4-STEP PROCESS ===================== -->'
end_marker = '</section>\n\n  <!-- ===================== CTA ===================== -->'

start_idx = html.find(start_marker)
assert start_idx != -1, "start_marker not found"

end_idx = html.find(end_marker, start_idx)
assert end_idx != -1, "end_marker not found"

cut_end = end_idx + len('</section>\n\n')

target_block = html[start_idx:cut_end]
print(f"Target block to remove length: {len(target_block)} chars")
print("Target snippet:\n", target_block[:150], "...", target_block[-150:])

html = html[:start_idx] + html[cut_end:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: 4-Step Process section removed from services.html")

