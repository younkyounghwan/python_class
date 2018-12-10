"""
챕터: day7
주제: os 모듈 사용
문제:
사용자가 입력한 디렉토리(1)로 이동한 후, 사용자가 입력한 이름의 새 디렉토리를 생성하라.
사용자가 입력한 디렉토리(2) 아래에 test 디렉토리를 생성하라.
사용자가 입력한 디렉토리를 포함하여 해당 디렉토리와 (2)test 디렉토리를 삭제하라.
삭제가 끝난 후, 사용자가 입력한 디렉토리(2)의 부모 디렉토리의 파일 목록을 출력하라.
작성자: 윤경환
작성일: 2018.12.04
"""

import os

x = os.getcwd()
try:
    print(x)
    d = input("이동할 디렉토리: ")
    os.chdir(d)
    target = input("새 디렉토리 이름: ")
    print("++++1++++")
    print(os.getcwd())

    os.mkdir(target)
    print("++++2++++")
    print(os.getcwd())
    os.chdir(x +"\\"+ target)

    print("++++3++++")
    print(os.getcwd())
    os.mkdir("test")

    print("++++4++++")
    print(os.getcwd())
    os.chdir(x)

    print("++++5++++")
    print(os.getcwd())
    os.rmdir(x + "\\" + "test")

    print("++++6++++")
    print(os.getcwd())

    print("++++7e++++")
    os.rmdir(x +"\\" + target)

    print(os.getcwd())

    for i in os.listdir(x):
        print(i)
except FileNotFoundError: #입력한 디엑토리가 없는 오류가 발생한 오류
    print("입력한 디렉토리는 존재하지 않습니다.")
except Exception:
    print("알 수 없는 오류가 발생했습니다.")