import random

Array_MethodList = ["pop()", "배열에 저장된 데이터 중 마지막 인덱스에 저장된 데이터를 삭제",

"push(새 데이터)",  "배열 객체의 마지막 인덱스에 '새 데이터'를 삽입",

"shift()", "배열 객체에 저장된 데이터 중 첫번째 인덱스에 저장된 데이터를 삭제",

"unshift(새 데이터)" , "배열 객체의 첫번째 인덱스에 '새 데이터'를 삽입",

"reverse()", "배열 객체의 데이터 순서를 역순으로 바꿈",

"sort()", "배열 객체의 데이터를 오름차순으로 정렬",

"concat(다른 배열)","현재 배열에 다른 배열의 원소들을 덧붙여 만든 새로운 배열 리턴",

"join(연결 문자)" ,"배열 객체의 데이터를 연결문자로 이어 붙여 1개의 문자형 데이터를 리턴",

"slice(index1 , index2)","배열 객체의 데이터 중 원하는 인덱스 구간만큼 잘라서 새로운 배열 반환 - index1 생략시 0부터 index2 생략시 맨 끝까지",

"splice(시작 인덱스, 삭제할 데이터 갯수, 추가할 데이터)", "배열 객체의 시작 인덱스부터 추가할 데이터를 삽입, 삭제할 데이터 개수 생략시 끝까지 삭제/ 추가할 데이터 생략 시 삭제만 수행] 입력 형식 : (시작 인덱스, 삭제할 데이터 갯수, 추가할 데이터)",
]

Date_MethodList = [
"getFullYear()", "4자리 연도 리턴",
"getMonth()", "월을 나타내는 정수 리턴 (1월:0, 2월:1, ... 12월:11)",
"getDate()" , "날짜 리턴(1~31)",
"getDay()", "요일을 나타내는 정수 리턴(일:0, 월:1,... 토:6)",
"getHours()", "0~23 사이의 정수 시간 리턴",
"getMinutes()", "0~59 사이의 정수 분 리턴",
"getSeconds()", "0~59 사이의 정수 초 리턴",
"getMilliseconds()", "0~999 사이의 정수 밀리초 리턴",
"getTime()", "1970년 1월1일 0시0분0초를 기준으로 현재시간까지 경과된 밀리초 리턴",
"setFullYear(year)" , "year를 년도 값으로 저장",
"setMonth(month)", "month(0~11)를 월 값으로 저장",
"setDate(date)", "date(1~31)를 날짜 값으로 저장",
"setHours(hour)", "hour(0~23)를 시간 값으로 저장",
"setMinutes(minute)", "minute(0~59)를 분 값으로 저장",
"setSeconds(second)" , "second(0~59)를 초 값으로 저장",
"setMilliseconds(ms)" , "ms(0~999)를 밀리초 값으로 저장",
"setTime(t)", "밀리초 단위인 t값으로 시간 저장",
"toGMTString()", "객체에 든 시간 정보를 GMT 표준 표기 방식의 문자열로 리턴 (Tue, 03 Sep 2020 03:07:15 GMT)",
"toLocaleString()", "객체에 든 날짜, 시간 정보를 로컬 표현의 문자열로 리턴 (2020. 9. 3. 오후 12:07:15)"
"toLocaleTimeString()", "객체에 든 시간 정보를 문자열 형식으로 리턴(오전 10:12:32)",
"toLocaleDateString()", "객체에 든 날짜 정보를 문자열 형식으로 리턴(2020. 9. 3.)"

]

String_MethodList = [

"charAt(idx)", "인덱스 위치 idx에 있는 문자 리턴",
"concat(s1, s2)", "현재 문자열 뒤에 문자열 s1, s2를 연결한 새로운 문자열 리턴",

"indexOf('str', idx)" , "인덱스 idx위치부터 검사하며 문자열 str이 처음으로 나타나는 인덱스 값 리턴 (idx 생략 시 처음부터 검색. 존재하지 않으면 -1 리턴)",

"replace('s1', 's2')",  "문자열 's1'을 찾아 's2'로 변경하여 새로운 문자열 리턴",

"split('구분자', 크기)" , "'구분자'를 기준으로 문자데이터를 나누어 배열에 저장 후 반환.’크기’로 배열의 크기 지정 가능(크기 생략가능)",

"toLowerCase()",  "소문자로 변환한 문자열 리턴",
"toUpperCase()",  "대문자로 변환한 문자열 리턴",

"substr(idx, len)", "인덱스 idx 위치에서부터 len개수만큼 자른 새로운 문자열 리턴 (len 생략시 끝까지)",

"slice(idx1, idx2)", "인덱스 idx1에서 idx2 전까지 문자열을 복사하여 리턴(idx2 생략시 끝까지)",

"trim()",  "문자열의 앞뒤 공백 문자를 제거한 새로운 문자열 리턴 (빈칸, 탭, 엔터키 제거)",
]

Math_MethodList = [

"PI" , "원주율 상수 리턴(3.141592...)",
"abs(x)",  "x의 절대값 리턴",

"sin(x),cos(x),tan(x)", "삼각함수",

"exp(x)", "e의 x제곱 값 리턴",
"pow(x,y)", "x의 y제곱 값 리턴",

"sqrt(x)", "x의 제곱근 리턴(√)",


"floor(x)", "x보다 작거나 같은 수 중 가장 큰 정수 리턴 (내림)",
"ceil(x)", "X보다 크거나 같은 수 중 가장 작은 정수 리턴 (올림)",
"round(x)", "x를 반올림한 정수 리턴",
"max(x,y,z,...)", "x,y,z 중 최댓값",
"min(x,y,z,...)", "x,y,z 중 최솟값",
"random()", "0부터 1보다 작은 임의의 실수 리턴(0≤ 난수 <1)"
]

print("1. Array_MethodList,  2. Date_MethodList,  3. String_MethodList,  4. Math_MethodList")

Select = int(input())

if Select == 1:
    while True:
        b = random.randrange(20)
        if b % 2 != 0:
            print(Array_MethodList[b])
            Answer = input()
            if Answer == Array_MethodList[b-1]:
             print("정-답")

            else:
                print("틀렸습니다.. 정답은 " + Array_MethodList[b-1] + " 입니다")

elif Select == 2:
    while True:
        b = random.randrange(40)
        if b % 2 != 0:
            print(Date_MethodList[b])
            Answer = input()
            if Answer == Date_MethodList[b - 1]:
                print("정-답")

            else:
                print("틀렸습니다.. 정답은 " + Date_MethodList[b- 1] + " 입니다")

elif Select == 3:
    while True:
        b = random.randrange(20)
        if b % 2 != 0:
            print(String_MethodList[b])
            Answer = input()
            if Answer == String_MethodList[b - 1]:
                print("정-답")

            else:
                print("틀렸습니다.. 정답은 " + String_MethodList[b - 1] + " 입니다")

elif Select == 4:
    while True:
        b = random.randrange(24)
        if b % 2 != 0:
            print(Math_MethodList[b])
            Answer = input()
            if Answer == Math_MethodList[b - 1]:
                print("정-답")

            else:
                print("틀렸습니다.. 정답은 " + Math_MethodList[b - 1] + " 입니다")