
import os

def install_requirements():

    if os.path.exists("requirements.txt"):
        os.system("pip install -r requirements.txt")
        pass
    else:
        print("Error: requirements.txt not found or no permissions to read it or no exist.")
        print("Please download the requirements.txt file and put it in the same directory as the program.")
        print("Github Download file: https://github.com/Happyuky7/YouTube-Downloader-PythonV1/blob/master/requirements.txt")
        print("If it doesn't work, download the requirements.txt file again install the requirements manually.")
        exit()


if __name__ == "__main__":
    # Install the requirements
    print("Installing the requirements...")
    install_requirements()
    print("Requirements installed successfully")

    if os.path.exists("YouTubeDownloaderPY.py"):
        os.system("python YouTubeDownloaderPY.py")
        print(" ")
        print("Run the program with the command in the terminal: python YouTubeDownloaderPY.py")
        print("The current version does not support the PowerShell terminal or PyCharm terminal.")
        print(" ")
        print("If you are in Windows, run command in cmd: 'python YouTubeDownloaderPY.py' Or execute 'run.bat' file.")
        print("If you are in Linux, run command in terminal: python3 YouTubeDownloaderPY.py")
        print("If you are in Mac, run command in terminal: python3 YouTubeDownloaderPY.py")
        print("If you are in Android Termux, run command in terminal: python3 YouTubeDownloaderPY.py")
        print(" ")
        print("or you can simply run in GIT Bash: python YouTubeDownloaderPY.py")
        print(" ")
        exit()
    else:
        print("Error: YouTubeDownloaderPY.py not found or no permissions to read it or no exist.")
        print("Github Download file: https://github.com/Happyuky7/YouTube-Downloader-PythonV1/")
        exit()


