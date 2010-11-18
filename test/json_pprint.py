import json, sys

f = sys.stdin.read()
obj = json.loads(f)

print json.dumps(obj, indent=4, ensure_ascii=False)
