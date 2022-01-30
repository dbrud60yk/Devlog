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
if json_data:
    print(json_data)