import json

def open_json_file(filename):
    with open(filename, encoding='utf8') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print('JSON 데이터 파싱 실패. 사유={0}'.format(e))
            return None

#message.json 파일은 같은 디렉터리에 있어야 합니다.
json_data = open_json_file('message1.json')
if not json_data:
    # 더 이상 로직을 진행할 수 없으므로 종료합니다.
    exit(0)

# 정수
num_value = json_data['number']
# 실수
float_value = json_data['pi']
# 문자열
str_value = json_data['str']
# 빈 키 (None)
empty_value = json_data['null_key']

print('num_value={0}'.format(num_value))
print('float_value={0}'.format(float_value))
print('str_value={0}'.format(str_value))
print('empty_value={0}'.format(empty_value))

# 객체 안 객체 접근
json_data2 = json_data['object']
print('json_data[\'object\'][\'str2\']={0}'.format(json_data2['str2']))

# 배열 접근
json_array = json_data['num_array']
for n in json_array:
    print('n={0}'.format(n))