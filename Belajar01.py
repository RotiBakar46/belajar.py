#bin#python
#module
import os,sys,time

#pembersih texs
def bersih():
    os.system("clear")
 
#tampilan
def menu():
    bersih()
    print("\033[1;35m")
    os.system("figlet Roti Bakar")
    print("\033[;34m========================================================================")
    print("\033[1;33m[1].\033[1;37m Author  : Sari Roti")
    print("\033[1;33m[2].\033[1;37m Id      : Sari Roti")
    print("\033[1;32m=======================================================================")
    print("                  DAFTAR MENU  ")
    print("             ====================================================================")
    print("\033[1;33m[1].\033[1;37m perkenalan ""    \033[1;33m[06].\033[1;37m Blm ada judul") 
    print("\033[1;33m[2].\033[1;37m Install(Update)""\033[1;33m[07].\033[1;37m Blm ada Judul")
    print("\033[1;33m[3].\033[1;37m Nethunter ""     \033[1;33m[08].\033[1;37m Blm ada Judul")
    print("\033[1;33m[4].\033[1;37m Blm Ada Judul""  \033[1;33m[09].\033[1;37m Blm ada Judul")
    print("\033[1;33m[5].\033[1;37m Blm ada judul""  \033[1;33m[10].\033[1;37m Blm ada Judul")
    print("\033[1;32m=======================================================================")
    contoh = input(" pilih 》 Loding...")
    if contoh == "1" :
       kenalan = input("        My Name Roti Bakar ")
       print("                Salam kenal Dari Roti Bakar ")
       print("==============================================================================")
    elif contoh == "2" :
       os.system(" pkg install update && upgrade -y")
       os.system(" pkg install Ruby -y")
       os.system(" pkg install nano -y")
       os.system(" pkg install python -y")
       os.system(" pkg install python2 -y")
       os.system(" pkg install python3 =y")
       os.system(" pkg install figlet -y")
       os.system(" pkg install wgit -y")
       os.system(" pkg install nethunter -y")
       print("\033[1;32m==================================================================")
    elif contoh =="3" :
         os.system(" pkg install update -y")
         os.system(" pkg install upgrade -y")
         os.system(" pkg install termux-setup-storage")
         os.system(" pkg install wget ")
         os.system(" wget -O install-nethunter-termux https://offs.cs/2MceZWr")
         os.system(" ./install-nethunter-termux")
         print("\033[1;32m===================================================================")
         
        
    
    menu()
         
    
      
        
         
    

