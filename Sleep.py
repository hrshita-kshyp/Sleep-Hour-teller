class Sleep:
     def __init__(self,name,sleep_time):
        self.name = name
        self.sleep_time = sleep_time

     @classmethod
     def cal_sleep(self):
       name = input("Enter your name:")
       print("Hi" + name + "!")
       sleep_time = int(input("Enter your sleep time:"))
       if sleep_time >8:
            print("You slept more than enough today")
       else:
              print("You need some sleep")



a = Sleep.cal_sleep()
Sleep.cal_sleep()
