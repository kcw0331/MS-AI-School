# 구두점 삭제
# 구두점 글자의 딕셔너리를 만들어 translate() 적용
import sys
import unicodedata
text_data = ["HI!!!!!!!!!!!!! I. love. Thie. Song...!!!!",
            "12222222%% Agree?! #AA",
            "Reight!@!@"] 
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P'))    
# print(punctuation)

test = [string.translate(punctuation) for string in text_data]
print(test)
"""
문자열만 남는 것을 볼 수 있다.
['HI I love Thie Song', '12222222 Agree AA', 'Reight']
"""