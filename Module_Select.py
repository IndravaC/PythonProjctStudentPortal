import pandas as pd

print("1.Creating a student database.")
print("2.View Batch database.")
print("3.View Course database.")
print("4.View Departments database.")
a = int(input("Enter the module number you want to open: "))
if a==1:
    import Python_Project_Indrava
    exec('Python_Project_Indrava.py')
elif a==2:
    df = pd.read_csv('Batch.csv')

    print(df)
elif a==3:
    df = pd.read_csv('Course.csv')

    print(df)
elif a==4:
    df = pd.read_csv('Department.csv')

    print(df)
