print("Hello World")
print("My name is Mehta Neev")
print('''Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!''')



# import pyttsx3
# engine = pyttsx3.init
# engine.say("help i am good")
# engine.runAndWait()
import os

def list_directory_contents(directory):
    try:
        Get the list of files and directories
        contents = os.listdir(directory)
        
        Print the contents
        print(f"Contents of directory '{directory}':")
        for item in contents:
            print(item)
    
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to access the directory '{directory}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    Specify the directory you want to list
    directory = input("/New floder")
    list_directory_contents(directory)
