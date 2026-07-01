
import json

log_path = r'C:\Users\Hi Windows 10\.gemini\antigravity-ide\brain\57736ed5-926b-4b91-b6f2-cd8943d05347\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['type'] in ('PLANNER_RESPONSE', 'USER_INPUT'):
            content = data.get('content', '')
            if 'bảng' in content.lower() or 'tabular' in content.lower():
                print(f'{data[\"type\"]}: {content[:150]}')
