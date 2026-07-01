import json
import os

log_path = r'C:\Users\Hi Windows 10\.gemini\antigravity-ide\brain\57736ed5-926b-4b91-b6f2-cd8943d05347\.system_generated\logs\transcript_full.jsonl'
os.makedirs('scripts_dump', exist_ok=True)
count = 0
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['type'] == 'PLANNER_RESPONSE':
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                if tc['name'] == 'run_command':
                    args = tc.get('args', {})
                    cmd = args.get('CommandLine', '')
                    if 'python -c' in cmd and 're.sub' not in cmd:
                        count += 1
                        with open(f'scripts_dump/script_{count}.py', 'w', encoding='utf-8') as out:
                            c = cmd.strip()
                            if c.startswith('python -c "'):
                                c = c[11:-1]
                            out.write(c)
