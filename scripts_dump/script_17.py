python -c '
import json
with open(r"C:\Users\Hi Windows 10\.gemini\antigravity-ide\brain\57736ed5-926b-4b91-b6f2-cd8943d05347\.system_generated\logs\transcript.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        d = json.loads(line)
        if d["type"] in ("PLANNER_RESPONSE", "USER_INPUT"):
            content = d.get("content", "")
            if "bảng" in content.lower():
                print(d["type"] + ": " + content[:200].replace("\n", " "))
'