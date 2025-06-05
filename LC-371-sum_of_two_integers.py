# i/p= a= 2, b= 3
# o/p= 5

def Sum_int(self, a:int, b:int)-> int:
    MASK = 0xFFFFFFFF
    MASK_INT = 0x7FFFFFFF

    while b!=0:
        carry = (a&b)<<1
        a = (a^b)&MASK
        b = carry&MASK

    return a if a<= MASK_INT else ~(a^MASK)

