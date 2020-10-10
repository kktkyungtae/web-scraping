# 이메일 보내기!
# 구글링해보면 이메일 보내기도 뼈대 코드들이 다 있다
# 강사도 코드들 라인바이라인으로 다 몰라
# 빈칸만 채우면 보내지는겨

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


### 보내는 사람 정보
me = "rokmt1134@gmail.com"
my_password = "95181018kt!"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

### 받는 사람 정보
# 여러 사람에게 보낼때
emails = ['rokmt1134@naver.com', 'rokmt1134@nate.com']

for you in emails:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "이것이 제목!!"
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "내용은 없다! 뭐먹지 오늘?"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 첨부하기!! 한줄한줄 이해할 필요 없이.. // 얘도 코드스니펫!
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string()) # sendmail로 메일을 보내는 거고
    # 그를 위해서 변수들을 세팅하는 것!
s.quit()
# 스켈레톤 코드에서 정보만 기입해서 실행하면 오류가 난다! 무슨 이중인증 그런것들 때문에
# 그래서 이런놈들을 꺼줘야됨!!!
# https://myaccount.google.com/signinoptions/two-step-verification
# 2단계 인증 해제
# + 보안 수준이 낮은 앱! 이놈을 접근할 수 있게 해줘야 한다// 허용으로 바꾸면 돼
# https://myaccount.google.com/lesssecureapps




# e-mail 보내기 시작코드
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email.mime.text import MIMEText
# from email import encoders
#
#
# # 보내는 사람 정보
# me = "보내는사람@gmail.com"
# my_password = "비밀번호"
#
# # 로그인하기
# s = smtplib.SMTP_SSL('smtp.gmail.com')
# s.login(me, my_password)
#
# # 받는 사람 정보
# you = "받는사람@아무_도메인"
#
# # 메일 기본 정보 설정
# msg = MIMEMultipart('alternative')
# msg['Subject'] = "제목"
# msg['From'] = me
# msg['To'] = you
#
# # 메일 내용 쓰기
# content = "메일 내용"
# part2 = MIMEText(content, 'plain')
# msg.attach(part2)
#
# # 메일 보내고 서버 끄기
# s.sendmail(me, you, msg.as_string())
# s.quit()