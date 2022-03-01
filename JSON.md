
# JSON
JavaScript Object Notation  
숫자, 문자, 참 또는 거짓 등 여러 형태의 데이터를 키(key)와 값(value)으로 구조화된 객체(object)에 담아 처리하는 규격  
가공된 JSON 데이터는 텍스트 기반이기 때문에 사람이 쉽게 저장된 데이터를 읽고 수정할 수 있고 디버깅도 편리

# JSON 특징

## 문자열 인코딩
UTF-8 인코딩만 허용하고 BOM을 허용하지 않음  
라이브러리에 따라 BOM을 암묵적으로 허용하는 경우도 있으나, 원칙적으로는 허용하지 않음

## 주석
JSON은 주석을 지원하지 않음  
라이브러리에 따라 주석을 사용할 수 있지만, 다른 서버나 클라이언트가 주석이 있는 JSON 파일이나 메시지를 읽지 못해 문제가 생길 확률이 높음  
주석이 필요하다면 XML이나 YAML처럼 주석을 지원하는 메시지 규격을 사용하는 것이 좋음

# JSON 구조
```json
//message1.json

{
    "number": 12345,
    "pi": 3.14,
    "str": "문자열 값",
    "null_key": null,
    "object": {
        "str2": "문자열 값2",
        "object2": {
            "number2": 12345
        }
    },
    "num_array": [1, 2, 3, 4, 5],
    "str_array": ["one", "two", "three", "four", "five"]
}
```
모든 JSON 데이터는 객체 형태를 의미하는 중괄호({})로 시작하거나 배열 형태를 의미하는 대괄호([])로 시작  
실무에서는 대부분 객체({})를 선호

## 키와 값
키(key) : 큰 따옴표로 감싼 문자열 데이터  
값(value) : 콜론 뒤에 오는 데이터, 콜론 앞에 있는 키에 대한 값을 의미  
값은 정수, 실수, 문자열, 널값, 객체, 배열 등 여러 형태를 사용할 수 있음  
키와 값을 여러 개 나열할 때 쉼표(,)로 구분  
마지막 키와 값에는 쉼표를 사용하지 않음

### 문자 이스케이프
```json
{
    "str": "큰 따옴표는 \"이렇게\" 표현합니다.",
    "str2": "첫 번째 줄입니다.\n두\t번째 줄입니다."
}
```

# JSON 메시지 읽고 쓰기
실무 개발 환경에서는 파일보단 HTTP 요청 메시지에 있는 문자열을 JSON으로 읽어 사용하는 경우가 많지만, JSON 파일인 message1.json을 사용하여 JSON 메시지를 다루는 방범을 설명
```py
#open_json_file.py

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
```

터미널 실행 결과 (open_json_file.py 파일 우클릭 - Run Python File in Terminal)
```
{'number': 12345, 'pi': 3.14, 'str': '문자열 값', 'null_key': None, 'object': {'str2': '문자열 값2', 'object2': {'number2': 12345}}, 'num_array': [1, 2, 3, 4, 5], 'str_array': ['one', 'two', 'three', 'four', 'five']}
```

## JSON 키와 값 읽기
```py
#json_reader.py

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
```
터미널 실행 결과 (json_reader.py 파일 우클릭 - Run Python File in Terminal)
```
num_value=12345
float_value=3.14
str_value=문자열 값
empty_value=None
json_data['object']['str2']=문자열 값2
n=1
n=2
n=3
n=4
n=5
```

키 값이 null인 경우는 None, null, nil로 표기되는 게 원칙  
라이브러리에 따라 false, 0,  "" 등 기본값으로 표기할 수도 있음

파이썬, 자바 c#과 같은 고수준 언어(high-level-language)에서 제공한 JSON 라이브러리는 읽어들인 JSON 데이터를 클래스, 맵, 리스트 등의 객체로 변환해주는 기능이 있음 -> 직렬화(serialization)  
반대로 클래스, 맵, 리스트 데이터를 JSON 문자열로 바꿔주는 기능 -> 역직렬화(deserialization)

### 키를 읽을 때 주의할 점
실무 개발 환경에서는 버그, 잘못된 요청, 해커의 변조 등의 이유로 키 자체가 존재하지 않거나, 읽어야 할 키는 존재하지만 예상하지 못한 값이 나오는 경우가 많음  
존재하지 않는 키에 접근했을 때 예외가 발생
```py
# 'unknown_key'를 읽는 잘못된 방법
unknown_value = json_data['unknown_key']
print('unknown_value={0}'.format(unknown_value))
```
터미널 실행 결과
```
Traceback (most recent call last):
  File "/Users/dbrud60yk/Repositories/Devlog/json_reader.py", line 41, in <module>
    unknown_value = json_data['unknown_key']
KeyError: 'unknown_key'
```

예외 발생 제어하는 방법 1 : try-catch 구문
```py
# 'unknown_key'를 읽는 올바른 방법 1
try:
    unknown_value = json_data['unknown_key']
    print('unknown_value={0}'.format(unknown_value))
except KeyError:
    print('\'unknown_key\'는 존재하지 않습니다.')
```
터미널 실행 결과
```
'unknown_key'는 존재하지 않습니다.
```

예외 발생 제어하는 방법 2 : 사용하는 모든 키가 존재하는지 검사
```py
# 'unknown_key'를 읽는 올바른 방법 2
if 'unknown_value' in json_data:
    unknown_value = json_data['unknown_key']
    print('unknown_value={0}'.format(unknown_value))
else:
    print('\'unknown_key\'는 존재하지 않습니다.')
```
터미널 실행 결과
```
'unknown_key'는 존재하지 않습니다.
```

키를 검사할 때는 키 존재 여부 외에 키에 대응하는 값이 올바른 형태인지도 함께 검사해야 함  
디버깅 환경에서만 동작하는 assert를 사용하여 검사하는 게 좋음
```py
#float_value가 3 이상 3.2 미만인지 검사
assert(3 <= float_value < 3.2)
#str_value가 null이 아니고 문자열 길이가 0 이상인지 검사
assert(str_value and len(str_value) > 0)
```

## JSON 파일 만들기
```py
# json_writer.py

import json

# 유니코드 문자열을 명시하기 위해 u를 붙임
message2 = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': u'문자열 값',
    u'null_key': None,
    u'object': {
        u'str2': u'문자열 값 2',
        u'object2': {
            u'number2': 12345
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}

# ensure_ascii=True인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX로 표기함
with open('message2.json', 'w', encoding='UTF8') as file:
    json.dump(message2, file, ensure_ascii=False)
    # 들여쓰기 추가
    # json.dump(message2, file, ensure_ascii=False, indent=2)
    # 키 정렬 필요한 경우
    # json.dump(message2, file, ensure_ascii=False, indent=2, sort_keys=True)
```
실행하면 message2.json이 생성됨

### JSON 메시지를 만들 때 유의할 점
null을 사용하지 않는 게 좋음  
어떤 키가 null을 가리키고 있다면, 그 키가 어떤 형태의 데이터를 담고 있는지 알 수 없기 떄문  
빈 값을 보낼 때 다음과 같은 형태로 메시지를 쓰는 게 좋음  
숫자(정수 또는 실수) -> "키": 0  
문자열 -> "키": ""  
객체 -> "키": {}  
배열 -> "키": []

### JSON 키 이름 형식
표준이나 관례가 없음  
프로그래밍 언어나 소프트웨어 프레잌워크, API마다 이름 짓는 방법이 조금씩 다름  
실무에서 하나의 규칙을 정하고 통일해 사용하는 게 유지 보수 측면에서 좋음

# JSON 한계
## 1. 불필요한 트래픽 오버헤드
텍스트 기반이기 때문에 실질적인 데이터를 표현하는 데 드는 비용이 큼 cf. 바이너리 기반  
JSON 메시지를 압축하면 바이너리 데이터와 비슷한 효과를 볼 수 있지만 CPU 자원을 많이 사용해야 함
## 2. 메시지 호환성 유지의 어려움
모든 텍스트 기반 데이터의 단점이기도 한 유지 보수의 어려움  
클라이언트와 서버가 같은 규격의 JSON 파일을 사용하여 통신할 때, 서버에서 파일을 업데이트하면 같은 규격의 JSON 키와 값을 사용하여 통신하는 모든 클라이언트 프로그램도 변경했던 규격을 동일하게 반영해야 함 -> 클라이언트에서 서버에 적용한 메시지 구조를 제대로 반영하지 못하면 문제 발생

# 레퍼런스
학교에서 알려주지 않는 17가지 실무 개발 기술 / 이기곤 지음 / 한빛미디어