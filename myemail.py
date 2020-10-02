# 이메일 보내기!
# 구글링해보면 이메일 보내기도 뼈대 코드들이 다 있다
# 강사도 코드들 라인바이라인으로 다 몰라
# 빈칸만 채우면 보내지는겨

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


# 보내는 사람 정보
me = "rokmt1134@gmail.com"
my_password = "95181018kt!"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
you = "rokmt1134@nate.com"

# 메일 기본 정보 설정
msg = MIMEMultipart('alternative')
msg['Subject'] = "이것이 제목!!"
msg['From'] = me
msg['To'] = you

# 메일 내용 쓰기
content = "내용은 없다! 뭐먹지 오늘?"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

# 메일 보내고 서버 끄기
s.sendmail(me, you, msg.as_string()) # sendmail로 메일을 보내는 거고
# 그를 위해서 변수들을 세팅하는 것!
s.quit()
# 스켈레톤 코드에서 정보만 기입해서 실행하면 오류가 난다! 무슨 이중인증 그런것들 때문에
# 그래서 이런놈들을 꺼줘야됨!!!
# https://myaccount.google.com/signinoptions/two-step-verification
# + 보안 수준이 낮은 앱! 이놈을 접근할 수 있게 해줘야 한다
# https://myaccount.google.com/lesssecureapps