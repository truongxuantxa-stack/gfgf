Set-Content -Path "recover_script.py" -Value @"
import json

log_path = r'C:\Users\Hi Windows 10\.gemini\antigravity-ide\brain\57736ed5-926b-4b91-b6f2-cd8943d05347\.system_generated\logs\transcript_full.jsonl'
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['type'] == 'PLANNER_RESPONSE':
            tool_calls = data.get('tool_calls', [])
            for tc in tool_calls:
                if tc['name'] == 'run_command':
                    args = tc.get('args', {})
                    cmd = args.get('CommandLine', '')
                    if 'Bảng' in cmd and 'replacements =' in cmd:
                        with open('bad_script.py', 'w', encoding='utf-8') as out:
                            # Strip the python -c wrapper
                            cmd = cmd.strip()
                            if cmd.startswith('python -c '):
                                cmd = cmd[10:].strip()
                            if cmd.startswith('"') and cmd.endswith('"'):
                                # It's json-escaped string? Actually if it was run in powershell, it's just a string.
                                # Let's just dump it raw first
                                out.write(cmd)
                        print('Recovered bad script to bad_script.py')
"@
python recover_script.py