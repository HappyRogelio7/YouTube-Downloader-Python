
import os
import sys
import time
import yaml

from pytube import YouTube
from colorama import Fore, Back, Style

def validator_url(url):
    if "https://" not in url: # or "http://" Not recommended because it is not secure.
        return False
    else:
        return True

def valirator_youtube(url):
    yaml_file = open("config.yml", "r")
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    validators_path = yaml_data["validators"]

    if validators_path["youtube"] or validators_path["youtu"] not in url:
        return False
    else:
        return True

def verify_files_and_directories():

    # Verify the file config.yml

    if os.path.exists("config.yml"):
        pass
    else:
        print(Fore.RED + "Error: The file config.yml does not exist")
        print(Fore.RED + "Starting the download of the file config.yml...")
        os.system("powershell.exe -Command \"Invoke-WebRequest -Uri https://raw.githubusercontent.com/Happyuky7/YouTube-Downloader-PythonV1/master/config.yml -OutFile config.yml\"")
        print(Fore.GREEN + "The file config.yml has been downloaded successfully")
        print(Fore.RED + "Restarting the program...")
        exit()

    # Verify the directories videos and audios

    if os.path.exists("videos"):
        pass
    else:
        print(Fore.RED + "Error: The directory videos does not exist")
        print(Fore.RED + "Creating the directory videos...")
        os.mkdir("videos")
        print(Fore.GREEN + "The directory videos has been created successfully")
        print(Fore.RED + "Restarting the program...")
        exit()

    if os.path.exists("audios"):
        pass
    else:
        print(Fore.RED + "Error: The directory audios does not exist")
        print(Fore.RED + "Creating the directory audios...")
        os.mkdir("audios")
        print(Fore.GREEN + "The directory audios has been created successfully")
        print(Fore.RED + "Restarting the program...")
        exit()





def main():

    print(Fore.GREEN + "The main program has been loaded successfully")

    yaml_file = open("config.yml", "r")
    yaml_data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    config_version = yaml_data["config-version"]
    settings_path = yaml_data["settings"]
    lang_path = yaml_data["messages"]["languages"]
    lang_en = lang_path["en"]
    lang_es = lang_path["es"]


    # Debug mode
    if bool(settings_path["debug"]):

    #if settings_path["debug"] == True:
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Debug mode")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Config version: ")
        print(config_version)
        print(Fore.GREEN + " Settings path: ")
        print(settings_path)
        print(Fore.GREEN + " Language path: ")
        print(lang_path)
        print(Fore.GREEN + " Language en: ")
        print(lang_en)
        print(Fore.GREEN + " Language es: ")
        print(lang_es)
        print(Fore.GREEN + "============================================================")
        #time.sleep(5)
        #os.system("cls")
    else:
        pass

    # Select language of the program (English or Spanish)
    print(Fore.GREEN + "============================================================")
    print(Fore.GREEN + " Select language of the program (English or Spanish)" + Fore.WHITE + "(en/es)")
    print(Fore.GREEN + "============================================================")
    print(Fore.GREEN + " Entry language: " + Fore.WHITE)

    language = input()
    if language == "en":
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Download Video and Audio from Youtube")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Author: " + Fore.WHITE + "Happyuky7")
        print(Fore.GREEN + " Version: " + Fore.WHITE + "1.0.0")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Github: " + Fore.WHITE + "https://github.com/Happyuky7")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Language: " + Fore.WHITE + "English")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Note: " + Fore.WHITE + "The audio is downloaded in mp4 format, but it is an audio file.")
        print(Fore.WHITE + "  This problem will be addressed in the next release.")
        print(Fore.GREEN + "============================================================")

        # Get the link from the user
        link = input(Fore.GREEN + lang_en["entry-link"] + Fore.WHITE)

        # Link is not URL, return error

        #if "https://" not in link:
        #if not validators.url(link):
        if not validator_url(link):
            print(Fore.RED + lang_en["error-link"])
            return


        yt = YouTube(link)

        # Get title of the video
        title = yt.title
        print(Fore.GREEN + lang_en["title"] + Fore.WHITE + title)

        # Change the title
        print(Fore.GREEN + lang_en["change-title"] + Fore.WHITE + "(y/n)")
        change = input()

        if change == "y":
            title = input(Fore.GREEN + lang_en["entry-title"] + Fore.WHITE)
            print(Fore.GREEN + lang_en["title-changed"] + Fore.WHITE + title)
        else:
            print(Fore.GREEN + lang_en["title-not-changed"] + Fore.WHITE + title)

        # Download the video or audio
        print(Fore.GREEN + lang_en["download-video-audio"] + Fore.WHITE + "(v/a)")
        change = input()
        if change == "v":


            print(Fore.GREEN + lang_en["change-quality"] + Fore.WHITE + "(y/n)")
            change = input()
            if change == "y":
                # Get the quality of the video
                print(Fore.GREEN + lang_en["available-qualities"])
                for i in range(len(yt.streams)):
                    print(Fore.GREEN + str(i) + " " + Fore.WHITE + str(yt.streams[i].resolution) + " " + str(
                        yt.streams[i].video_codec) + " " + str(yt.streams[i].audio_codec))

                # Get the quality of the video
                quality = int(input(Fore.GREEN + lang_en["entry-quality"] + Fore.WHITE))
                yt = yt.streams[quality]
            else:
                # Get the highest resolution possible
                yt = yt.streams.get_highest_resolution()

            # Get save directory of the video
            os.chdir(os.path.dirname(sys.argv[0]) + "/videos")
            print(Fore.GREEN + lang_en["actual-save-directory"] + Fore.WHITE + os.getcwd())

            # Change save directory of the video
            print(Fore.GREEN + lang_en["change-save-directory"] + Fore.WHITE + "(y/n)")
            change = input()
            if change == "y":
                # Get the directory of the video
                directory = input(Fore.GREEN + lang_en["entry-save-directory"] + Fore.WHITE)
                os.chdir(directory)
                print(Fore.GREEN + lang_en["save-directory-changed"] + Fore.WHITE + os.getcwd())

                # Download the video
                print(Fore.GREEN + lang_en["downloading-video"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_en["downloaded-video"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_en["downloaded-video_time"] + Fore.WHITE + str(end - start) + "s")
                print(Fore.GREEN + lang_en["downloaded-video_quality"] + Fore.WHITE + str(yt.resolution))

            else:

                os.chdir(os.path.dirname(sys.argv[0]) + "/videos")

                # Download the video
                print(Fore.GREEN + lang_en["downloading-video"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_en["downloaded-video"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_en["downloaded-video_time"] + Fore.WHITE + str(end - start) + "s")
                print(Fore.GREEN + lang_en["downloaded-video_quality"] + Fore.WHITE + str(yt.resolution))

        else:

            # Get the highest resolution possible
            yt = yt.streams.get_audio_only()

            # Get save directory of the video
            os.chdir(os.path.dirname(sys.argv[0]) + "/audios")
            print(Fore.GREEN + lang_en["actual-save-directory"] + Fore.WHITE + os.getcwd())

            # Change save directory of the video
            print(Fore.GREEN + lang_en["change-save-directory"] + Fore.WHITE + "(y/n)")
            change = input()
            if change == "y":
                # Get the directory of the video
                directory = input(Fore.GREEN + lang_en["entry-save-directory"] + Fore.WHITE)
                os.chdir(directory)
                print(Fore.GREEN + lang_en["save-directory-changed"] + Fore.WHITE + os.getcwd())

                # Download the video
                print(Fore.GREEN + lang_en["downloading-audio"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_en["downloaded-audio"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_en["downloaded-audio_time"] + Fore.WHITE + str(end - start) + "s")

            else:

                os.chdir(os.path.dirname(sys.argv[0]) + "/audios")

                # Download the video
                print(Fore.GREEN + lang_en["downloading-audio"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_en["downloaded-audio"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_en["downloaded-audio_time"] + Fore.WHITE + str(end - start) + "s")


        # You don't want to download another video or audio
        print(Fore.GREEN + lang_en["download-another"] + Fore.WHITE + "(y/n)")
        change = input()
        if change == "y":
            main()
        else:
            print(Fore.GREEN + lang_en["thanks"] + Fore.WHITE)
            exit()


    # Spanish
    elif language == "es":
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Descargar Video y Audio de Youtube")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Autor: " + Fore.WHITE + "Happyuky7")
        print(Fore.GREEN + " Versión: " + Fore.WHITE + "1.0.0")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Github: " + Fore.WHITE + "https://github.com/Happyuky7")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Lenguaje: " + Fore.WHITE + "Español")
        print(Fore.GREEN + "============================================================")
        print(Fore.GREEN + " Nota: " + Fore.WHITE + "Los Audios se descargan en formato mp4, pero son audios.")
        print(Fore.WHITE + "  Este problema se intentara resolver en la próxima versión.")
        print(Fore.GREEN + "============================================================")

        # Get the link from the user
        link = input(Fore.GREEN + lang_es["entry-link"] + Fore.WHITE)

        # Link is not URL, return error
        if not validator_url(link):
            print(Fore.RED + lang_es["error-link"] + Fore.WHITE)
            return

        yt = YouTube(link)

        # Get title of the video
        title = yt.title
        print(Fore.GREEN + lang_es["title"] + Fore.WHITE + title)

        # Change the title
        print(Fore.GREEN + lang_es["change-title"] + Fore.WHITE + "(y/n)")
        change = input()

        if change == "y":
            title = input(Fore.GREEN + lang_es["entry-title"] + Fore.WHITE)
            print(Fore.GREEN + lang_es["title-changed"] + Fore.WHITE + title)
        else:
            print(Fore.GREEN + lang_es["title-not-changed"] + Fore.WHITE + title)

        # Download the video or audio
        print(Fore.GREEN + lang_es["download-video-audio"] + Fore.WHITE + "(v/a)")
        change = input()

        if change == "v":

            print(Fore.GREEN + lang_es["change-quality"] + Fore.WHITE + "(y/n)")
            change = input()
            if change == "y":
                # Get the quality of the video
                print(Fore.GREEN + lang_es["available-qualities"])
                for i in range(len(yt.streams)):
                    print(Fore.GREEN + str(i) + " " + Fore.WHITE + str(yt.streams[i].resolution) + " " + str(yt.streams[i].video_codec) + " " + str(yt.streams[i].audio_codec))

                # Get the quality of the video
                quality = str(input(Fore.GREEN + lang_es["entry-quality"] + Fore.WHITE))

                yt = yt.streams.get_by_resolution(quality)
            else:
                # Get the highest resolution possible
                yt = yt.streams.get_highest_resolution()

            # Get save directory of the video
            os.chdir(os.path.dirname(sys.argv[0]) + "/videos")
            print(Fore.GREEN + lang_es["actual-save-directory"] + Fore.WHITE + os.getcwd())

            # Change save directory of the video
            print(Fore.GREEN + lang_es["change-save-directory"] + Fore.WHITE + "(y/n)")
            change = input()
            if change == "y":
                # Get the directory of the video
                directory = input(Fore.GREEN + lang_es["entry-save-directory"] + Fore.WHITE)
                os.chdir(directory)
                print(Fore.GREEN + lang_es["save-directory-changed"] + Fore.WHITE + os.getcwd())

                # Download the video
                print(Fore.GREEN + lang_es["downloading-video"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_es["downloaded-video"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_es["downloaded-video_time"] + Fore.WHITE + str(end - start) + "s")
                print(Fore.GREEN + lang_es["downloaded-video_quality"] + Fore.WHITE + str(yt.resolution))

            else:

                os.chdir(os.path.dirname(sys.argv[0]) + "/videos")

                # Download the video
                print(Fore.GREEN + lang_es["downloading-video"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_es["downloaded-video"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_es["downloaded-video_time"] + Fore.WHITE + str(end - start) + "s")
                print(Fore.GREEN + lang_es["downloaded-video_quality"] + Fore.WHITE + str(yt.resolution))

        else:

            # Get the highest resolution possible
            yt = yt.streams.get_audio_only()

            # Get save directory of the video
            os.chdir(os.path.dirname(sys.argv[0]) + "/audios")
            print(Fore.GREEN + lang_es["actual-save-directory"] + Fore.WHITE + os.getcwd())

            # Change save directory of the video
            print(Fore.GREEN + lang_es["change-save-directory"] + Fore.WHITE + "(y/n)")
            change = input()
            if change == "y":
                # Get the directory of the video
                directory = input(Fore.GREEN + lang_es["entry-save-directory"] + Fore.WHITE)
                os.chdir(directory)
                print(Fore.GREEN + lang_es["save-directory-changed"] + Fore.WHITE + os.getcwd())

                # Download the video
                print(Fore.GREEN + lang_es["downloading-audio"] + Fore.WHITE)

                start = time.time()
                yt.download()
                end = time.time()
                print(Fore.GREEN + lang_es["downloaded-audio"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_es["downloaded-audio_time"] + Fore.WHITE + str(end - start) + "s")

            else:

                os.chdir(os.path.dirname(sys.argv[0]) + "/audios")

                # Download the video
                print(Fore.GREEN + lang_es["downloading-audio"] + Fore.WHITE)

                start = time.time()
                yt.download()

                end = time.time()
                print(Fore.GREEN + lang_es["downloaded-audio"] + Fore.WHITE + os.getcwd())
                print(Fore.GREEN + lang_es["downloaded-audio_time"] + Fore.WHITE + str(end - start) + "s")

        # You don't want to download another video or audio
        print(Fore.GREEN + lang_es["download-another"] + Fore.WHITE + "(y/n)")
        change = input()
        if change == "y":
            main()
        else:
            print(Fore.GREEN + lang_en["thanks"] + Fore.WHITE)
            exit()

    else:
        print(Fore.RED + "Error: " + Fore.WHITE + "Language not found")
        exit()








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
    print("Verifying requirements...")
    install_requirements()
    print(Fore.GREEN + "Requirements verified successfully")

    print(Fore.GREEN + "Starting the program...")

    print(Fore.GREEN + "Verifying files and directories...")
    verify_files_and_directories()
    print(Fore.GREEN + "Files and directories verified successfully")

    print(Fore.GREEN + "Loading the main program...")
    main()



