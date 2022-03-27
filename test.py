Touched by ihobbang250
#조하영, 201903429, 러시아 학과
#성별과 키에 따른 표준체중 구하기
def std_weight(height, gender):
    m_weight = height*height*22*0.01*0.01
    m_weight = round(m_weight, 2)
    f_weight = height*height*21*0.01*0.01
    f_weight = round(f_weight, 2)
    if gender == "male":
        print("gender : {0}, height : {1}cm, standard weight : {2}kg" .format(
            gender, height, m_weight))
    elif gender == "female":
        print("gender : {0}, height : {1}cm, standard weight : {2}kg" .format(
            gender, height, f_weight))
    return gender, height, f_weight, m_weight

#BMI 계산
def BMICalculation(height, weight):
    height_meter = height / 100 #키 미터단위로 계산
    BMI = round(weight/(height_meter*height_meter), 1) #BMI = 몸무게/신장*신장
    if(BMI < 18.5): #BMI지수에 따른 상태출력
        Condition = '저체중'
    elif(18.5 <= BMI <= 22.9):
        Condition = '정상'
    elif(23 <= BMI <= 24.9):
        Condition = '과체중'
    elif(BMI > 25):
        Condition = '비만'
    print("BMI : {0}, Condition : {1}".format(BMI, Condition))

gender = input("Your gender? : ")
height = int(input("Your height? : "))
weight = int(input("Your weight? : "))
std_weight(height, gender)
BMICalculation(height, weight)
