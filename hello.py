# 숫자랑 문자열은 더할 수 없다!

# 변수이름은 막지으면 안된다!
# 코드 컨벤션!! 회사마다 정해진게 있다. 카멜 케이스, 스네이크 케이스 등등
# 선호하는 걸로 쭉 쓰면돼

# 자료형을 배워보자
# 리스트랑 딕셔너리를 구분하는 것이 중요하다
a_list = ['사과', '감','배']
b_list = ['영희', '철수', ['사과', '감']]

a_list.append('수박')

# 딕셔러니
a_dict = {'name':'kyungtae', 'age':30}
#추가할때는 List 처럼
a_dict['height'] = 186

# 딕셔너리 안에 List를 넣을 수도 있다.
a_dict['fruits'] = a_list
print(a_dict)
print(a_dict['fruits'][1]) # 감 출력하기
# 라스트는 숫자로 찾는다, 릭셔너리는 키 값으로 찾는다 만 기억하자

## 조건문
age = 30
if age > 30:
    print('아저씨다')
else:
    print('애기 아니면 할배')

## 반복문
# 리스트의 항목들을 순회한다.
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
for f in fruits:
    print(f)

# 딕셔너리 예제
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for p in people:
    if p['age'] >= 20:
        print(p['name'])

## 파이썬 내장함수
# 문자 쪼개기

my_email = 'rokmt1134@nate.com'
# 골뱅이를 기점으로 쪼개기
result = my_email.split('@')
print(result)

# 어느 도메인인지 알 수 있는 방법!!
result_2 = my_email.split('@')[1].split('.')
print(result_2[0])
result_3 = my_email.split('@')[1].split('.')[0]
print(result_3)

# 바꾸기!
result_4 = my_email.replace('nate', 'naver')
print(result_4)