# QR Code

import qrcode

qr_data = 'www.naver.com'
qr_image = qrcode.make(qr_data)

qr_image.save(qr_data + '.png')

import qrcode

with open('site_list.txt', 'rt', encoding='UTF8') as f: # with는 블록이 끝나면 종료를 해준다.
    read_lines = f.readlines()

    # 한줄씩 읽어서 출력해주는 것을 해준다.
    for line in read_lines:
        line = line.strip()  # strip은 문자 이외의 것들을 제외해준다.
        print(line)

        qr_data = line
        qr_image = qrcode.make(qr_data)
        
        qr_image.save(qr_data + '.png')
# print(read_lines)