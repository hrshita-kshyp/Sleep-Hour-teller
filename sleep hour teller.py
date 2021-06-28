
from pygame import mixer

class ScreenOne:
 def screen(self):
    print("-------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("                       WELCOME TO SLEEP HOUR TELLER     ")
    print("--------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------")
    print("                   1.Sleep Hour calculator and categorizer ")
    print("                   2.Play sleep song")

    choice_n = int(input("Enter your choice:"))
    while choice_n >0  & choice_n<3 :
     if choice_n == 1 :
      one()
      break
     elif choice_n == 2:
      two()
      break
     else:
      print("Unknown choice")
      break
      
    def changer(self,*args):
        self.manager.current = 'screen2'

def one():
        
  name = input("Enter your name:")
  print("Hi" '\t' + name + "!")
  start_time = int(input("Enter when you slept(in hours):"))
  end_time = int(input("Enter when you wake up(in hours):"))
  sleep_total = start_time - end_time
  print(f"You slept for {abs(sleep_total)}")
  if sleep_total >8:
          print("You slept more than enough for today")
  else:
          print("You need more sleep")
  print("GoodBye!")


def two():
   print("----------------------**Music List**--------------------------------")
   print("--------------------------------------------------------------------")
   print("                    1. Relaxing music 1")
   print("                    2. Relaxing music 2")
   print("                    3. Relaxing music 3")

   music_choice = int( input("Which music you want to play? Enter serial number:"))
   if music_choice == 1:
     mixer.init()
     mixer.music.load("music3.mp3")
     mixer.music.set_volume(1.2)
        # Start playing the song
     mixer.music.play()
     while True:
            
            print("Press 'p' to pause, 'r' to resume")
            print("Press 'e' to exit the program")
            query = input("  ")
            
            if query == 'p':
            
                  # Pausing the music
                  mixer.music.pause()     
            elif query == 'r':
            
                  # Resuming the music
                  mixer.music.unpause()
            elif query == 'e':
            
                  # Stop the mixer
                  mixer.music.stop()
                  print("GoodBye!")
                  break
            
 
   elif music_choice == 2:
  
            mixer.init()
            mixer.music.load("music2.mp3")
            mixer.music.set_volume(1.2)
           # Start playing the song
            mixer.music.play()
            while True:
            
             print("Press 'p' to pause, 'r' to resume")
             print("Press 'e' to exit the program")
             query = input("  ")
            
             if query == 'p':
            
                  # Pausing the music
                  mixer.music.pause()     
             elif query == 'r':
            
                  # Resuming the music
                  mixer.music.unpause()
             elif query == 'e':
            
                  # Stop the mixer
                  mixer.music.stop()
                  print("GoodBye!")
                  break
            
   elif music_choice == 3:
  
           mixer.init()
           mixer.music.load("music3.mp3")
           mixer.music.set_volume(1.2)
          # Start playing the song
           mixer.music.play()
           while True:
            
            print("Press 'p' to pause, 'r' to resume")
            print("Press 'e' to exit the program")
            query = input("  ")
            
            if query == 'p':
            
                  # Pausing the music
                  mixer.music.pause()     
            elif query == 'r':
            
                  # Resuming the music
                  mixer.music.unpause()
            elif query == 'e':
            
                  # Stop the mixer
                  mixer.music.stop()
                  print("GoodBye!")
                  break
           
   

a= ScreenOne()
a.screen()



