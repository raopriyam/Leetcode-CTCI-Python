
def acronym(str1):
    ans = ' '
    for i in str1.split():
        ans = ans + i[0].upper()
    return ans

input_string = str(input("Enter the String"))
print(acronym(input_string))
    
