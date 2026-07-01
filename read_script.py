import json

log_path = r'C:\Users\Hi Windows 10\.gemini\antigravity-ide\brain\57736ed5-926b-4b91-b6f2-cd8943d05347\.system_generated\logs\transcript.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['type'] == 'PLANNER_RESPONSE':
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                if tc['name'] == 'run_command':
                    args = tc.get('args', {})
                    cmd = args.get('CommandLine', '')
                    if 'python' in cmd and 're.sub' in cmd:
                        print('Found python script:\\n' + cmd[:1000])
