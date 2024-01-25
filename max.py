#Nhập giá trị đầu vào 
A = float(input("nhập giát trị A = "))
B = float(input("nhập giát trị B = "))
C = float(input("nhập giát trị C = "))

#giả định gán cho A là giá trị lớn nhất
Max = A 

#TH nếu A < B
if Max < B :
    Max = B

#TH nếu B > C
if Max < C :
    Max = C 

#in ra giá trị lớn nhất    
print("max =", Max)
