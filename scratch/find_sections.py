with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

sections = re.findall(r'<section[^>]*id=["\']([^"\']+)["\']', text)
print("Section IDs:", sections)

# Also check for classes containing 'project' or 'prop' or 'develop'
classes = set(re.findall(r'class=["\']([^"\']*(?:project|property|residential|card)[^"\']*)["\']', text))
print("Matching classes:", list(classes)[:20])

