data = [10, "Python", "", 25, "Loop", 40]
print(data)
number_list=[0]*len(data)
string_list=[""]*len(data)
count_numbers = 0
count_strings = 0
n_index = 0
s_index = 0
for i in data:
    if type(i)==int:
        number_list[n_index]=i
        count_numbers=count_numbers+1
        n_index=n_index+1
    elif type(i)==str and i != "":
        string_list[s_index]=i
        count_strings=count_strings+1
        s_index=s_index+1
reg=int(input("enter the last num of ur reg no:"))

number_list = number_list[:n_index]
string_list = string_list[:s_index]

if reg%2==0:
    number_list=number_list[::-1]
else:
    string_list = string_list[::-1]

print("Numbers List:", number_list)
print("Strings List:", string_list)
print("Total Numbers:", count_numbers)
print("Total Strings:", count_strings)



