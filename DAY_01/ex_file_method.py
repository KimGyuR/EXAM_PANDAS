# ---------------------------------------------------------------------
# 파일 데이터 접근 관련 메서드들
# ---------------------------------------------------------------------
filename='message.txt'

with open(filename, mode='r', encoding='utf8') as f:

    f.seek(6) # 한글 내용이 들어갈 경우 한글은 개당 3byte를 사용하므로
             # 3의 배수로 사용해야함 그 외 숫자 사용시 Traceback 에러 발생
    print(f.read(10))
    print(f'현재 위치 : {f.tell()}')
    print(f.name, f.closed)

    f.seek(0)
    print(f.read(5))
    print(f'현재 위치 : {f.tell()}')

print(f.name, f.closed)