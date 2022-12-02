# 텍스트 데이터 처리 01
import re
text_data = [" Interrobang. By Aishwarya Henriette",
            "Parking and going. By Kear Gua",
            "Today Is the night. By Jar par"]

# 공백 제거
strip_whitespace = [string.strip() for string in text_data] # 빈칸을 없애준다.
print("공백 제거 >>", strip_whitespace)
# ['Interrobang. By Aishwarya Henriette', 'Parking and going. By Kear Gua', 'Today Is the night. By Jar par']

# 마침표 제거
remove_periods = [string.replace(".", "") for string in strip_whitespace]  
print("마침표 제거 >>", remove_periods)

'''
공백 제거 >> ['Interrobang. By Aishwarya Henriette', 'Parking and going. By Kear Gua', 'Today Is the night. By Jar par']
마침표 제거 >> ['Interrobang By Aishwarya Henriette', 'Parking and going By Kear Gua', 'Today Is the night 
By Jar par']
'''

def capitalizer(string:str) -> str: return string.upper()

temp = [capitalizer(string) for string in remove_periods]
print(temp)
'''
['INTERROBANG BY AISHWARYA HENRIETTE', 'PARKING AND GOING BY KEAR GUA', 'TODAY IS THE NIGHT BY JAR PAR'] 
'''

def replaace_letters_with_X(string: str) -> str :
    return re.sub(r"[a-zA-Z]", "X", string)

data = [replaace_letters_with_X(string) for string in remove_periods]
print("마침표 제거 >>", data)
'''
마침표 제거 >> ['XXXXXXXXXXX XX XXXXXXXXX XXXXXXXXX', 'XXXXXXX XXX XXXXX XX XXXX XXX', 'XXXXX XX XXX XXXXX 
XX XXX XXX']
'''