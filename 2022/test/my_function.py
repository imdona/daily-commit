def my_divide():
    try:
        x = input('분자의 숫자를 입력하세요 ~ ')
        y = input('분모의 숫자를 입력하세요 ~ ')
        return int(x) / int(y)
    except:
        return '나누기를 할 수 없습니다'

writer = 'Lion'