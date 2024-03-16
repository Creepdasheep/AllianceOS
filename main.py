import sys
import subprocess
import os
import time
from AudioDecoder import AudioDemodulator
import keyboard
import pyaudio
from Recording import AudioRecorder

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def execute_command(command, input_stuff):
    input_stuff = input_stuff
    command = command.lower()
    if command == "exit" or command == "shutdown":
        print(bcolors.FAIL + "Shutting down")
    elif command == "audio":
        print(bcolors.HEADER + "Press any key to start recording audio")
        print(bcolors.FAIL + "Press any key to stop")

        recording = AudioRecorder(output_filename="my_recording.wav")
        recording.record()
        print(bcolors.HEADER + "Stoped Recording")
        demodulator = AudioDemodulator("my_recording.wav")
        demodulator.load_audio()
        recovered_text = demodulator.process_audio()
        print(recovered_text)
        # exec(recovered_text)

    elif command == "math":
       answer = eval(input_stuff or 0)
       print(bcolors.OKBLUE + str(answer))
       return str(answer)
    elif command == "clear":
       clear()
    else:
        print(bcolors.FAIL + "Unknown Command: " + command)

def main():
    clear()
    print(bcolors.OKGREEN + """

     _    _     _     ___    _    _   _  ____ _____ 
    / \  | |   | |   |_ _|  / \  | \ | |/ ___| ____|
   / _ \ | |   | |    | |  / _ \ |  \| | |   |  _|  
  / ___ \| |___| |___ | | / ___ \| |\  | |___| |___ 
 /_/   \_|_____|_____|___/_/   \_|_| \_|\____|_____|
                                                    
                                                                                                                                                        
""")
    print(bcolors.ENDC + "Version 0.0.1")
    while True:
        user_input = input(bcolors.OKCYAN + "$ | ")
        command, *input_stuff = user_input.split(maxsplit=1)
        execute_command(command, input_stuff[0] if input_stuff else "0")

if __name__ == '__main__':
    main()