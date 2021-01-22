#public
#protected
#private

class college:
    col_fee=60000 #public by default
    _col_fee=60000    #protected access
    __col_fee1=12223131

class student(college):
    income=50000           #public by default
    __income1=9000000         # pravate



vp=college()
stud1=student()

print(vp.col_fee)
print(vp._college__col_fee1)
print(stud1.income)
print(stud1._student__income1)


