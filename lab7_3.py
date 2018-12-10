"""
챕터: day7
주제: os.path 모듈 사용
문제:
A. 프로그래밍이 아닌 수작업으로, c:\temp 디렉토리에 자신의 학번에 해당하는 디렉토리를 생성한 후,임의의 파일을 3개 복사한다.
학번 디렉토리 아래에 room1 디렉토리를 만들어서 임의의 파일을 3개 복사한다.
room1밑에 room2 디렉토리를 만들어서 임의의 파일 3개 복사한다. 자신의 학번아래 room3 디렉토리를 만든다.
i. 여러번 테스토하기 위해, 매번 생성하는 번거로움을 피하게 다른 디렉토리에 복사본을 만들어 놓는다.

B. 아래를 프로그래밍한다.
i. c:\temp아래의 자신의 학번 디렉토리 아래에 있는 모든 파일과 디렉토리를 삭제하라.
디렉토리인지 확인한 후, 디렉토리라면 해당 디렉토리 내에 있는 모든 파일을 삭제한 후, 해당 디렉토리를 삭제하라.
ii. 프로그램 실행 후 학번 아래에 파일과 디렉토리가 없음을 확인하라. 어떤 디렉토리 구조에서도 작동할 수 있게 프로그래밍 하라.
작성자: 윤경환
작성일: 2018.12.06
"""

import os


def remove_files(dir):
    files = os.listdir(dir)
    for i in files:
        if os.path.isfile(dir + "\\" + i) == True:
            os.remove(dir + "\\" + i)
        else:
            remove_files(dir + "\\" + i)
            os.rmdir(dir + "\\" + i)

try:
    remove_files("C:\\Temp\\201814099")
except FileNotFoundError:
    print("해당 폴더가 존재하지 않습니다.")
else:
    print("삭제 완료")