import json

j={
    "employee":
    [
        {"id":111, "name":"Mike"},
        {"id":222, "name":"Nancy"}
    ]
}

print(j)
print("②##########")

a = json.dumps(j)
print(json.loads(a))

### jsonファイルk書き込み
with open('test.json', 'w') as f:
    json.dump(j, f)
print("③##########")

### jsonファイル読み込み
with open('test.json', 'r') as f:
    print(json.load(f))

