list_of_students = []

print("Enter scores: ")
for i in range(0,4):
    list_of_students.append(eval(input()))

best = max(list_of_students)

for i in range(len(list_of_students)) :
    if (list_of_students[i] >= (best - 10)) :
        print("Student ", i ," score is ", list_of_students[i] ," and grade is A")
    else :
        if (list_of_students[i] >= (best - 20)) :
            print("Student ", i ," score is ", list_of_students[i] ," and grade is B")

        else :
            if (list_of_students[i] >= (best - 30)) :
                print("Student ", i ," score is ", list_of_students[i] ," and grade is C")
            else :
                if (list_of_students[i] >= (best - 40)) :
                    print("Student ", i ," score is ", list_of_students[i] ," and grade is D")
                else :
                    print("Student ", i ," score is ", list_of_students[i] ," and grade is F")
