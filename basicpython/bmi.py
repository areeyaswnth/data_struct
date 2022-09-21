x= list(map(float, input("Enter your High and Weight : ").split()))


height=x[0];
weight=x[1];
Bmi=weight/(height*height)
if(Bmi<18.5):
    print('Less Weight')
elif(Bmi<23.0 and Bmi>=18.5):
    print('Normal Weight')
elif(Bmi<25.0 and Bmi>=23.0):
    print('More than Normal Weight')
elif(Bmi<30.0 and Bmi>=25.0):
    print('Getting Fat') 
elif(Bmi>=30.0):
    print('Fat')   
#BMI < 18.50 แสดงผล Less Weight
#18.50 <= BMI  < 23 แสดงผล Normal Weight
# #23 <= BMI  < 25 แสดงผล Morethan Normal Weight
#5 <= BMI  < 30 แสดงผล Getting Fat
# #BMI  >= 30 แสดงผล Fat