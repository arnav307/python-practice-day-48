def list_of_digit(input_string):
    digits=[]
    for i in input_string:
        if i.isdigit():
            digits.append(int(i))
    return digits
        
input_string="Hello123World456384848457"
print(list_of_digit(input_string))