# problem_28.py
# Count Pass/Fail Students

def pass_fail_Checker(scores, passing_Score):
    passCount = sum(1 for score in scores if score >= passing_Score)
    failCount = len(scores) - passCount
    return passCount, failCount



scores = []
passing_score = 50
NumOfStudent = int(input("enter number of student:  "))

for i in range(NumOfStudent):
    student_score= int(input(f"Enter The Score of Student {i + 1}: "))
    scores.append(student_score)

pass_student, fail_student = pass_fail_Checker(scores, passing_score)

print(f"total pass: {pass_student}")
print(f"total fail: {fail_student}")