# Có bốn hướng mà một con rùa có thể di chuyển:

# Forward – phía trước
# Backward – phía sau
# Left – bên trái
# Right – bên phải
# Con rùa move.forward() hoặc move.backward() theo hướng mà nó đang đối mặt. Bạn có thể thay đổi hướng này bằng cách xoay nó .left () hoặc .right () ở một mức độ nhất định. Bạn có thể thử từng lệnh sau như sau:

t.right(90)

t.forward(100)

t.left(90)

t.backward(100)

# rút gọn
t.rt() 
t.fd() 
t.lt() 
t.bk() 

# Để đưa rùa về vị trí cũ, bạn gõ như sau: 

>>> t.home()

# vẽ hình tròn
t.circle(60)

# Theo cách tương tự, bạn cũng có thể vẽ một dấu chấm, 
# không là gì khác ngoài một vòng tròn được điền đầy.
t.dot(20)

# thay đổi background 
turtle.bgcolor(“blue”)

# Đôi khi, bạn có thể cần tăng hoặc giảm độ dày của bút. Bạn có thể thực hiện việc này bằng lệnh sau:

t.pensize(5)

t.forward(100)

# thay đổi màu trỏ chuột và kích thước
t.shapesize(3,3,3)
t.fillcolor(“red”)

# Để thay đổi màu đường viền của trỏ chuôtj

t.pencolor(“green”)

# Con rùa thường di chuyển với tốc độ vừa phải. 
# Nếu bạn muốn giảm hoặc tăng tốc độ để rùa di chuyển chậm hơn 
# hoặc nhanh hơn, thì bạn có thể thực hiện bằng cách nhập như sau: 

>>> t.speed(1)

>>> t.forward(100)

>>> t.speed(10)

>>> t.forward(100)

# Mã này đầu tiên sẽ giảm tốc độ và di chuyển con rùa về phía trước, 
# sau đó tăng tốc độ và di chuyển con rùa về phía trước một lần nữa, 

# Màn hình được chia thành bốn góc phần tư. 
# Điểm mà con rùa được định vị ban đầu ở đầu chương trình của bạn là (0,0).
# Để di chuyển con rùa đến bất kỳ khu vực nào khác trên màn hình, 
# .goto() và nhập các tọa độ:

>>> t.goto(100,100)