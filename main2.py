import json
try:
    f = open("out1.txt", 'r', encoding="utf-8")
    data = json.loads(f.read())
    f.close()

    f = open('out.json', 'w')
    f.write(json.dumps(data, indent=2))
    f.close()
except Exception as e:
    print(e)

input('done')