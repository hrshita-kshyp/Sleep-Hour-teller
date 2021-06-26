print("******************************************************************************")
print("WELCOME TO SLEEP HOUR TELLER")
print("*******************************************************************************")



class Sleep:
     @classmethod   
     def sleep_time(self):
        name = input("Enter your name:")
        print("Hi" '\t' + name + "!")
        start_time = int(input("Enter when you slept(in hours):"))
        end_time = int(input("Enter when you wake up(in hours):"))
        sleep_total = start_time - end_time
        print(f"You slept for {sleep_total}")
        if sleep_total > 8:
          print("You slept more than enough today")
        elif sleep_total == 8:
          print("You slept enough")
        else:
          print("You need more sleep")
    
             
Sleep.sleep_time()



