
'''
# Tìm max trong 3 số

a,b,c = map(float,input().split())
print('Số lớn nhất trong 3 số là: ',max(a,b,c))



# kiểm tra dữ liệu là string hay number, viết chương trình chỉ cho phép nhập số

while True:
    a = input("Nhập một số bất kì: ")
    try:
        a1 = int(a) # ép kiểu int
        print("Number")
        break
    except ValueError:
        try:
            a2 = float(a) # ép kiểu float
            print('Number')
            break
        except ValueError:
            print('String')



# Tính tổng S(n) = 1+2+3+4+5+...+n

def NhapSo():
    while True:
        a = input("Nhập một số bất kì: ")
        try:
            a1 = int(a) # ép kiểu int
            return a1
        except ValueError:
            print('Nhập số')

if __name__ == "__main__":
    print('Tính S(n) = 1+2+3+...+n')
    while True:
        n = NhapSo()
        if n>0:
            break
        else:
            print('Nhap so nguyen duong')
    S=0
    for i in range(0,n+1):
        S+=i
    print('S(n)='+str(S))


# Tính tổng S(n) = 1^2 + 2^2 + 3^2 + 4^2 + ... + n^2

def NhapSo():
    while True:
        a = input("Nhập một số bất kì: ")
        try:
            a1 = int(a) # ép kiểu int
            return a1
        except ValueError:
            print('Nhập số')

if __name__ == "__main__":
    print('Tính S(n) = 1^2 + 2^2 + 3^2 + 4^2 + ... + n^2')
    while True:
        n = NhapSo()
        if n>0:
            break
        else:
            print('Nhap so nguyen duong')
    S=0
    for i in range(1,n+1):
        S+=(i**2)
    print('S(n)='+str(S))



# Tính S(n) = 1 + 1/2 + 1/3 + ... + 1/n

if __name__ == "__main__":
    print ("S(n) = 1 + 1/2 + 1/3 + ... + 1/n")
    global n
    while True:
        n = input("n = ")
        try:
            n = int(n)
            if(n>0):
                break
        except ValueError:
            print('Nhập số nguyên dương')
    s=0
    for i in range(1,n+1):
        s+= (1/i)
    print ("kết quả: ",s)

# Dùng đệ quy
def tinh(n):
    if n==1: return 1
    else:
        return n+tinh(n-1)

if __name__=="__main__":
    n = int(input("Nhập n"))
    print(tinh(n))


# Tính S(n) = 1/2 + 1/4 + ... + 1/2n

if __name__ == "__main__":
    print ("S(n) = 1/2 + 1/4 + ... + 1/2n")
    global n
    while True:
        n = input("n = ")
        try:
            n = int(n)
            if(n>0):
                break
        except ValueError:
            print('Nhập số nguyên dương')
    s=0
    for i in range(1,n+1):
        s+= 1/(2*i)
    print ("kết quả: ",s)


# Tính tổng S(n) = 1/3 + 1/5 + 1/7 + ... + 1/(2n+1)
if __name__ == "__main__":
    print ("S(n) = 1/3 + 1/5 + 1/7 + ... + 1/(2n+1)")
    global n
    while True:
        n = input("n = ")
        try:
            n = int(n)
            if(n>0):
                break
        except ValueError:
            print('Nhập số nguyên dương')
    s=0
    for i in range(1,n+1):
        s+= 1/(2*i+1)
    print ("kết quả: ",s)



# Bài toán về ước số
    
if __name__ == "__main__":
    global n
    dem=0
    tong=0 # Tính tổng tất cả các ước số
    uocle =1 # Tìm ước số LẺ LỚN NHẤT
    uoc = []
    # Nhập n nguyên dương
    while True:
        n = input("Nhập n = ")
        try:
            n = int(n)
            if(n>0):
                break
        except ValueError:
            print('Nhập số nguyên dương')
    # Tìm ước số
    for i in range(1,n+1):
        if n%i==0:
            dem+=1
            uoc.append(i)
            tong+=i
            if i%2!=0 and i>uocle:
                uocle = i

    # in kết quả
    print("Số lượng ước số của " +str(n)+ " là: " + str(dem) )
    print("Liệt kê:", end="")
    print(*uoc, sep= ',')
    print("Tổng tất cả các ước số là: " + str(tong))
    print("Ước số lẻ lớn nhất: ",uocle)
    print("Đây là số hoàn hảo không?", (tong-n)==n)



# Số chính phương

from math import sqrt
if __name__ == "__main__":
    n = int(input("Nhập số:"))
    a = (sqrt(n))
    print("Đây là số chính phương?",a*a==n)



# kiểm tra số nguyên tố
if __name__ == "__main__":
    n = int(input("Nhập số: "))
    ketqua = True
    for i in range(2,n):
        if n%i==0:
            ketqua = False
            break
    print('Đây là số nguyên tố không?', ketqua==True)


# Đảo ngược số

if __name__ == "__main__":
    n = int(input())
    a = 0
    while n!=0:
        a = a*10 + (n%10)
        n = n//10
    print(a)


# Giải phương trình bậc 2

from math import sqrt


if __name__=="__main__":
    a,b,c = map(int, input().split())
    if(a==0):
        if(b==0):
            print('PT vô nghiệm' if c!=0 else 'PT vô số nghiệm')
        else:
            print('PT có nghiệm:',-c/b)
    else:
        d = b*b-4*a*c
        if(d<0):
            print('PT vô nghiệm')
        elif d==0:
            print('PT có nghiệm kép: ', -b/2/a)
        else:
            print('x1 = ', (-b+sqrt(d))/2/a)
            print('x2 = ', (-b-sqrt(d))/2/a)
  

# Tính điểm trung bình, xếp loại: 5 môn
def DiemTB(d1,d2,d3,d4,d5):
    TB = (d1+d2+d3+d4+d5)/5
    if(TB<5):
        return TB,'học lực yếu'
    elif 5<=TB<6.9:
        return TB,'học lưc trung bình'
    elif 7<=TB<8.9:
        return TB,'học lưc khá'
    else:
        return TB,'giỏi'

if __name__ == "__main__": 
    d1,d2,d3,d4,d5 = map(float,input("Nhập điểm: ").split())
    DTB, XepLoai = DiemTB(d1,d2,d3,d4,d5)
    print(DTB)
    print(XepLoai)
  

 # Tính tổng 1000 số nguyên tố đầu tiên
 import math
def checkSNT(a):
    if a==2: return True
    elif a<2 or a%2==0: return False
    else:
        for x in range(3,math.ceil(sqrt(a)),2):
            if a%x==0:
                return False
        return True

if __name__=="__main__":
    dem=0
    tong =0
    a = []
    for i in range(1,10005):
        if dem==1000: break
        if checkSNT(i):
            tong+=i
            dem+=1
            a.append(i)
    print(tong)
    print(*a,sep='    ')


# Lambda in ra thông tin sinh viên
def sinhvien(name):
    return lambda infor: name + ' ' + infor
name_ = input('Nhập tên: ')
sv = sinhvien(name_)
print(sv(input('Nhập tuổi: ')))
print(sv(input('Nhập giới tính: ')))
print(sv(input('Nhập quốc tịch: ')))

# Thêm phần tử đến khi nhập 'exit' thì dừng, sau đó in ra các số chẵn

if __name__=="__main__":
    input_ = ""
    a = []
    while input_ != 'exit':
        input_ = input("Nhập số (hoặc nhập 'exit' để dừng lại): ")
        try:
            input_ = (int)(input_)
            a.append(input_)
        except ValueError:
            print('Hãy nhập đúng yêu cầu!')
    for x in a:
        if x%2==0: print(x,end=" ")

# Nhập danh sách tên sinh viên, tìm tên 1 sinh viên
def nhap():
    global sv
    # nhập đến khi nhập 'stop' thì dừng nhập
    input_ = ''
    while input_ != 'stop':
        input_ = input("Nhập sinh viên (hoặc 'stop' để dừng nhập): ")
        if check(sv,input_)==False: sv.append(input_)
    # xóa phần tử 'stop'
    sv.pop(-1)
def check(list_,str_):
    for x in list_:
        if x == str_: return True
    return False
if __name__ == "__main__":
    sv = []
    nhap()
    print(*sv,sep="  **  ")
    print("Kết quả: ",check(sv,input("Nhập sinh viên cần tìm: ")))

# sắp xếp mảng tăng dần, giảm dần
a = [1,3,5,6,4,2,8,9,7] 
print("Ban đầu:",*a)
# tăng dần
a.sort()
print("Tăng dần:",*a)
# giảm dần
a.sort(reverse = True)
print("Giảm dần:",*a)

# quản lý sinh viên python dùng list - dictionary
def menu():
    luachon=-1
    print("1: Thêm sinh viên")
    print("2: Xóa sinh viên")
    print("3: Sửa sinh viên")
    print("4: Xem danh sách sinh viên")
    print("0: Thoát")
    while luachon not in [0,1,2,3,4]:
        try:
            luachon = (int)(input("Nhập lựa chọn của bạn: "))
        except:
            print('Bạn phải nhập đúng chức năng !')
    return luachon
# Tìm sinh viên theo mã sinh viên
def find(list_, id_):
    for i in range(0,len(list_)):
        if id_ == list_[i]["msv"]: return i
    return -1
# Thêm sinh viên
def add():
    global list_sv
    sv = {"msv":'', "ten":""}
    msv = input("Nhập id:")
    while find(list_sv,msv)!=-1:
        msv = input("id đã tồn tại. Hãy nhập id khác: ")
    # add
    sv['msv'] = msv 
    sv['ten'] = input("Nhập tên sinh viên: ")
    list_sv.append(sv)
    print("Thêm thành công id:",sv['msv']," *** tên:",sv["ten"])
# Xóa sinh viên
def remove():
    global list_sv
    msv = input("Nhập id sinh viên cần xóa: ")
    index_ = find(list_sv,msv)
    if index_ == -1: print("id không tồn tại")
    else:
        list_sv.pop(index_)
        print('Đã xóa thành công')
# Sửa sinh viên
def edit():
    global list_sv
    msv = input("Nhập id sinh viên cần sửa: ")
    index_ = find(list_sv,msv)
    if index_ == -1: print("id không tồn tại")
    else:
        list_sv[index_]['ten'] = input("Nhập tên mới: ")
        print("Đã sửa thành công")
def display():
    for sv in list_sv:
        print("Mã sinh viên:",sv['msv'],"|| Tên sinh viên:",sv["ten"])
if __name__ == "__main__":
    
    list_sv = []
    func = 1
    while func>=0 or func<4:
        func=menu()
        if func==0: break
        elif func==1: add()
        elif  func==2: remove()
        elif func==3: edit()
        else: display()
'''




































