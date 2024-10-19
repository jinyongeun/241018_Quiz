# 평균 점수를 계산하여 60점 이상이면 합격하는 클래스
class Student:
    # 학생의 정보를 받는 함수
    def __init__(self, name, grade, major):
        self.name = name
        self.grade = grade
        self.major = major

    # 학생의 과목별 성적을 받는 함수
    def input_score(self, korean, english, math):
        self.korean = korean
        self.english = english
        self.math = math
        score = f"국어: {self.korean}, 영어: {self.english}, 수학: {self.math}"
        return score

    # 입력 받은 성적을 평균내는 함수
    def score_average(self):
        average = ((self.korean + self.english + self.math) / 3)
        return average

    # 학생의 정보와 합격여부를 알려주는 함수
    def student_info(self):
        input_score = self.input_score(korean, english, math)
        score_average = self.score_average()
        student_info = f"이름: {self.name}, 학년: {self.grade}, 학과: {self.major}\n{input_score}\n평균 성적: {score_average}"
        if score_average >= 60:
            print("축하합니다, 합격입니다.")
        else:
            print("불합격입니다.")
        return student_info

# 이름, 학년, 학과 입력
name = input("이름을 입력하세요: ")
grade = input("학년을 입력하세요: ")
major = input("학과를 입력하세요: ")

# 학생 객체 생성
student = Student(name, grade, major)

# 성적 입력
korean = int(input("국어 점수를 입력하세요: "))
english = int(input("영어 점수를 입력하세요: "))
math = int(input("수학 점수를 입력하세요: "))

# 학생 정보 확인
print(student.student_info())