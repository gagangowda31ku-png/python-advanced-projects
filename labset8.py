

# labset 8

'''Define a function that takes TWO objects representing 
complex numbers and returns a new complex number with the
 sum of two complex numbers. Define a suitable class 
 ‘Complex’ to represent the complex number.
  Develop a program to read N (N >=2) complex numbers 
  and to compute the addition of N complex numbers. '''
  
class Complex:
    def __init__(self,real , img):
        self.real = real
        self.img = img

    def  add(self,other):
        real_part = self.real + other.real
        img_part = self.img + other.img

    def display(self):
        if self.img >= 0:
            return f"{self.real} + {self.img}i"
        else:
            return f"{self.real} - {abs(self.img)}i"

def add_n_complex(numbers):
    result = numbers[0]
    for i in range(1,len(numbers)):
        result = result.add(numbers[i])
    return result

n = int(input("Enter the number of complex number: "))
complex_list = []
for i in range(n):
    print("\n Enter the complex number {i+1}: ")
    real = int(input("Enter the real part: "))
    img = int(input("Enter the imaginary part: "))
    complex_list.append(Complex(real,img))

result = add_n_complex(complex_list)
print("sum of the complex numbers: ")
print(result.display())

