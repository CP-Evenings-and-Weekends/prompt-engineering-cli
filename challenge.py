KEYPAD = { 
'A': '2', 'B': '2', 'C': '2', 
'D': '3', 'E': '3', 'F': '3', 
'G': '4', 'H': '4', 'I': '4', 
'J': '5', 'K': '5', 'L': '5', 
'M': '6', 'N': '6', 'O': '6', 
'P': '7', 'Q': '7', 'R': '7', 'S': '7', 
'T': '8', 'U': '8', 'V': '8', 'W': '9', 
'X': '9', 'Y': '9', 'Z': '9', 
} 

def to_phone_number(s): 
    return ''.join(KEYPAD.get(c.upper(), c) for c in s) 
    # print(to_phone_number("877-CASH-NOW")) # 877-227-4669
    s = input("Enter string:")
    print(to_phone_number(s))


def reverse_integer(number):
    sign = -1 if number < 0 else 1
    digits_reversed = str(abs(number))[::-1]
    reversed_number = int(digits_reversed)
    return sign * reversed_number