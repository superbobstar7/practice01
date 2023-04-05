def convert_score(grade):
    match grade:
        case 'A+':
            score = 4.5
        case 'A':
            score = 4.0
        case 'B+':
            score = 3.5
        case 'B':
            score = 3.0
        case 'C+':
            score = 2.5
        case 'C':
            score = 2.0
        case 'D+':
            score = 1.5
        case 'D':
            score = 1.0
        case 'F':
            score = 0.0
    return score


submit_credit, archive_credit = 0, 0
submit_gpa, archive_Gpa = 0.0, 0.0

while True:
    print("작업을 선택하세요")
    print("   1. 입력")
    print("   2. 계산")
    user_value = input()
    value = int(user_value)

    match value:
        case 1:
            print("학점을 입력하세요. ")
            user_value = input()
            credit = int(user_value)

            print("평점을 입력하세요. ")
            user_value = input()
            gpa = convert_score(user_value)

            if gpa > 0:
                submit_credit += credit
                submit_gpa += gpa * credit
            archive_credit += credit
            archive_gpa += gpa * credit

        case 2:
            submit_gpa /= submit_credit
            archive_gpa /= archive_credit

            print('제출용: ' + str(submit_credit) + '(GPA: ' + str(submit_gpa) + ')')
            print('열람용: ' + str(archive_credit) + '(GPA: ' + str(submit_gpa) + ')')

            break




# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.


def print_hi(name):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
    print(f'Hi, {name}')  # 중단점을 전환하려면 Ctrl+F8을(를) 누릅니다.


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    print_hi('PyCharm')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
