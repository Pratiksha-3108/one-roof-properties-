import json

with open(r'C:\Users\Admin\.gemini\antigravity\brain\6ea31858-5b2b-44bd-ac91-9f917ce239ee\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('type') == 'USER_INPUT':
            content = obj.get('content', '')
            for term in ['shrink', 'small circle', 'circle', 'tangent', 'horizontal', 'showcase', 'slider', 'right side']:
                if term in content.lower():
                    clean = content.split('<USER_REQUEST>')[1].split('</USER_REQUEST>')[0].strip() if '<USER_REQUEST>' in content else content
                    print(f"{obj.get('step_index')}: {clean[:120].encode('ascii', 'replace').decode('ascii')}")
                    break
