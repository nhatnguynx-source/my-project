#Phase 1
class User:
     
        def __init__(self, username, password):
            self.username = username
            self.password = password
            self.attempts = 0                   # Đếm số lần thử
        
class Room:
        def __init__(self, room_number, type_room, view):
            self.room_number = room_number
            self.type_room = type_room
            self.view = view
            self.is_booked = False              # False nghĩa là phòng chưa đặt

        def book(self):
            if  self.is_booked:                 # Phòng đã được đặt 
                print("Sorry, this room is already booked. Please select another room")
            else:
                self.is_booked = True              # Phòng chưa được đặt 
                print("Congratulations on your successful booking!")

    
        def __repr__(self):                                # diện mạo của self.is_booked
             if self.is_booked:                            #phòng đã đặt = true => Booked
                  status = "Booked"
             else:
                  status = "Available"                    # phòng chưa đặt = false => Available
             return "Room " + self.room_number + " - " + self.type_room +  " - " + status         # Return số phòng + loại phòng + trạng thái
               
Hotel_list = [
     Room("201", "Master", "Moutain and Beach"),
     Room("202", "Double", "Beach"),
     Room("203", "Master", "Beach"),
     Room("204", "Double", "Beach"),
     Room("205", "Double", "Beach"),
     Room("301", "Master", "Moutain and Beach"),
     Room("302", "Double", "Beach"),
     Room("303", "Master", "Beach"),
     Room("304", "Double", "Beach"),
     Room("305", "Double", "Beach"),
     Room("401", "Master", "Moutain and Beach"),
     Room("402", "Double", "Beach"),
     Room("403", "Master", "Beach"),
     Room("404", "Double", "Beach"),
     Room("405", "Double", "Beach"),
     Room("501", "Master", "Moutain and Beach"),
     Room("502", "Double", "Beach"),
     Room("503", "Master", "Beach"),
     Room("504", "Double", "Beach"),
     Room("505", "Double", "Beach")
]

#Phase 2
import time                          # Để dùng lệnh time.sleep

print("WELCOME TO THE SMART HOTEL SYSTEM")
print("To begin making a reservation, please register an account.")

login_user = input("Please select your username: ")


while True:
 req_pass = input("Create a password (min 6 characters): ")
 if len(req_pass) < 6:
      print("Your password is too short. Please create again!")
 else:
      break


Customer = User(login_user, req_pass)

print("Registration successful!")
print("Now, please log in to verify your access.")

while True:                            #  Chạy liên tục chương trình
     if Customer.attempts == 3:        # == là so sánh, = là gán cái str = int đó 
          print("\n!!! SECURITY ALERT: Too many failed attempts.")  
          print("The system will be temporarily locked for 1 minute.")
          time.sleep(60)              # tạm thời lock sever trong 60s
          Customer.attempts = 0       # Chưa thử 1 lần nào 
          print("You can try again now!")
     login_user = input("Please enter your username: ")
     login_pass = input("Please enter your password: ")

     if login_user == Customer.username and login_pass == Customer.password:           # vì customer = user (login_user, login_pass)
          print("Login successful! Welcome back, " + Customer.username)              # dấu "." được coi là toán tử để chỉ chính xác function đó trong đoạn code VD username nhìn self.username ở class user
          break
     else:
          Customer.attempts += 1                          # Phải tăng số lần sai lên (nếu sai)
          print("Incorrect! Please try again. ")           # Số lần sai >= 3 bị khóa

 

     
     
     

