import os
import subprocess
import re
import time


class Lab2:
    @staticmethod
    # This method shows 3 relevant data of a video
    def task1():
        print("\n")

        filename = "BBB.mp4"

        # With this command the duration of the video is shown in the console screen
        command = "ffmpeg -i " + filename + " 2>&1 | grep Duration | awk '{print $2}' | tr -d ,"
        os.system(command)

        # With this command the resolution (width and height) of a video is shown in the console screen
        command = "ffprobe -i " + filename + " -v quiet -show_entries stream=width,height -hide_banner"
        os.system(command)

        # With this command the bit rate of the video is shown in the console screen
        command = "ffprobe -v quiet -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1 " \
                  + filename
        os.system(command)

        print("\n")

    @staticmethod
    # This method creates a new container for the video
    def task2():
        filename = "BBB.mp4"

        # With this command a minute of the video is cut in order to have a shorter video to work with
        command = "ffmpeg -i " + filename + " -s 00:00:00 -t 00:01:00 -c:v copy -c:a copy cutBBB.mp4 -y"
        os.system(command)

        # With this command the audio of the video cut is exported into an mp3 audio track
        command = "ffmpeg -i cutBBB.mp4 -acodec mp3 -vcodec copy audioMP3.mp3 -y"
        os.system(command)

        # With this command the audio of the video cut is exported into an aac audio track
        command = "ffmpeg -i cutBBB.mp4 -acodec aac -vcodec copy audioAAC.aac -y"
        os.system(command)

        # With this command the video cut and both audio tracks are packaged into one single mp4 video
        command = "ffmpeg -i cutBBB.mp4 -i audioMP3.mp3 -i audioAAC.aac -map 0 -map 1 -map 2 -codec copy mixBBB.mp4 -y"
        os.system(command)

        print("\n")

        # In order to have less files saved in the folder where the videos and audios are, it is given to the user the
        # option of deleting the audio files exported before (mp3 and aac audios)
        ans = 0
        while ans != 2:
            # A question is asked to the user to know if the user wants to delete the audio tracks or not
            print("Do you want to delete the audio tracks?")
            print("1. Yes\n2. No")

            # Checking if the input is correct, asking again to write an input if it isn't
            while ans < 1 or ans > 2:
                try:
                    ans = int(input("Write an option (number 1 or 2): "))
                except ValueError:
                    pass

            # If the answer is yes, both audio tracks are deleted
            if ans == 1:
                os.system("rm audioMP3.mp3 & rm audioAAC.aac")
                print("Audio tracks removed")
                ans = 2

        print("\n")

    @staticmethod
    # This method resizes a video with any resolution given
    def task3():
        print("\n")

        filename = "cutBBB.mp4"
        execute = 0
        width = 0
        height = 0

        # A question is asked to the user to know if the user wants to resize the video, this inside a loop enables the
        # user to resize the video as many times as he wants without having to go back to the main menu
        while execute != 2:
            print("Do you want to resize the video?")
            print("1. Yes\n2. No")

            # Checking if the input is correct, asking again to write an input if it isn't
            while execute < 1 or execute > 2:
                try:
                    execute = int(input("Write an option (number 1 or 2): "))
                except ValueError:
                    pass

            # If the answer is yes, a width and height are asked to the user
            if execute == 1:
                # Checking if the inputs are correct, asking again to write them if it isn't
                while width <= 1:
                    try:
                        width = int(input("Write a width (number greater than 1): "))
                    except ValueError:
                        pass

                while height <= 1:
                    try:
                        height = int(input("Write a height (number greater than 1): "))
                    except ValueError:
                        pass

                # As the width and height can not be odd numbers, the program checks if they are odd and if so, these
                # values are converted to even ones
                if width % 2 != 0:
                    width -= 1
                    print("Width can not be odd, so width is converted to", width)

                if height % 2 != 0:
                    height -= 1
                    print("Height can not be odd, so height is converted to", height)

                # Time break to give the user time to read the message above if there is
                time.sleep(2)

                # Command to change the resolution of the video to the one given by the user
                command = "ffmpeg -i " + filename + " -vf scale=" + str(width) + ":" + str(
                    height) + " resized_cutBBB.mp4"
                os.system(command)
                width = 0
                height = 0
                execute = 0

            print("\n")

    @staticmethod
    # This methods tells the user in which broadcasting standards a video fits
    def task4():
        print("\n")

        filename = "BBB.mp4"

        # A command to show all the video information is saved in a new variable called "res" instead of being showed to
        # the user
        command = "ffmpeg -i " + filename
        res = subprocess.getoutput(command)

        # The word "Audio" is searched in the variable "res" and all the times it appears, it will be saved in "times"
        times = re.findall('Audio', res)
        all_codecs = []

        # Iterates over "times"
        for x in times:
            # Searches for "Audio" in "res" and saves this word and 11 characters more (to make sure the codec is saved)
            audio_type = res[res.find(x):res.find(x) + 11]

            # Removes blank spaces from the resulting string "audio_type"
            audio_type = audio_type.replace(" ", "")

            # Splits the word "Audio" from the codec and saves them in "aux_split"
            aux_split = audio_type.split(":")

            # Now, "Audio" is in the position 0 and the codec in the position 1 of the array "aux_split", so the program
            # saves only the codec in "all_codecs" in order to have all the codecs of the audio in the same array
            all_codecs.append(aux_split[1])

            # The first "Audio" found is deleted from "res" so in the next iteration it is not found again
            res = res.replace("Audio", "", 1)

        # Once all codecs are saved in the array "all_codecs", the program iterates over them
        for audio_track in all_codecs:
            print("The audio codec is", audio_track)

            # Checking the audio codec type and printing the corresponding broadcasting standards
            if audio_track == "aac":
                print("Broadcasting standards:\n* DVB-T\n* ISDB-T\n* DTMB\n")

            elif audio_track == "ac-3":
                print("Broadcasting standards:\n* DVB-T\n* ATSC\n* DTMB\n")

            elif audio_track == "mp3":
                print("Broadcasting standards:\n* DVB-T\n* DTMB\n")

            elif audio_track == "mp2":
                print("Broadcasting standard: DTMB\n")

            elif audio_track == "dra":
                print("Broadcasting standard: DTMB\n")


# Main function with the menu to choose the task to be executed
def main():
    option = 0
    # Showing the menu till the input given by the user is 5
    while option != 5:
        # Printing the menu with the options of the tasks to be executed and the exit option
        print("Select an option from the menu:")
        print("1. Parse the video\n2. Create a new container\n3. Resize the video\n4. Broadcasting standards\n5. Exit")

        # Checking if the input is correct, asking again if it isn't
        while option < 1 or option > 5:
            try:
                option = int(input("Write an option (number between 1 and 5): "))
            except ValueError:
                pass

        # Checking the option given by the user and calling the corresponding method to execute the selected task
        if option == 1:
            Lab2.task1()
            option = 0

        if option == 2:
            Lab2.task2()
            option = 0

        if option == 3:
            Lab2.task3()
            option = 0

        if option == 4:
            Lab2.task4()
            option = 0


# Calling main function
main()
