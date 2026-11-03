import json

with open(r'C:\Users\Admin\.gemini\antigravity\brain\6ea31858-5b2b-44bd-ac91-9f917ce239ee\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    lines = [json.loads(l) for l in f]

user_steps = [x for x in lines if x.get('type') == 'USER_INPUT']
for x in user_steps[-30:]:
    content = x.get('content', '')
    if '<USER_REQUEST>' in content:
        req = content.split('<USER_REQUEST>')[1].split('</USER_REQUEST>')[0].strip()
        print(f"{x.get('step_index')}: {req.encode('ascii', 'replace').decode('ascii')}")

