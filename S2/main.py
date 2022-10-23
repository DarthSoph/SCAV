import os


# Globals
path = os.path.dirname(__file__)


# Cut N seconds of a video
def task1():
    # Ask the user a number to be the seconds of the video to be cut
    # For this I do a while and a try/except in order to check the variable to be introduced is correct and ask for
    # another one if it isn't
    n = -1
    while n < 1 or n > 600:
        try:
            n = int(input("Introduce the time in seconds you want the video to last (between 1 and 600): "))
        except ValueError:
            pass

    # Converting seconds to time in format hours:minutes:seconds
    time = ""
    s = n % 60
    m = n // 60
    h = m // 60
    m = m % 60
    time = '{:02d}:{:02d}:{:02d}'.format(h, m, s)

    # Writing the command to cut the video from the beginning to the time computed before
    filename = "BBB.mp4"
    command = "ffmpeg -i " + filename + " -s 00:00:00 -t " + time + " -c:v copy -c:a copy BBB_cut.mp4"
    os.system(command)


# Create the YUV histogram from the previous cut and then putting it next to the video
def task2():
    # Writing the command to create the histogram
    filename = "BBB_cut.mp4"
    command = "ffmpeg -i " + filename + " -vf histogram histogram.mp4"
    os.system(command)

    # Writing the command to put together the video with the histogram
    command = "ffmpeg -i " + filename + " -i histogram.mp4 -filter_complex '[0:v]pad=iw*2:ih[int];[int][" \
                                        "1:v]overlay=W/2:0[vid]' -map '[vid]' -c:v libx264 -crf 23 -preset veryfast " \
                                        "BBB_histogram.mp4"
    os.system(command)

    # Removing the histogram in order to only have the mix video saved
    os.system("rm histogram.mp4")


# Resize the video
def task3():
    filename = "BBB.mp4"

    # Showing the different options to resize the video and checking the input is correct
    # There is an option to exit the task
    s = 0
    while s != 5:
        command = ""
        print("Select the new size of the video:")
        print("1. 720p\n2. 480p\n3. 360x240\n4. 160x120\n5. Exit")

        while s < 1 or s > 5:
            try:
                s = int(input("Write an option (number between 1 and 5): "))
            except ValueError:
                pass

        # Now the program checks the option and resizes the video to the corresponding size according to the menu
        if s == 1:
            # The original video is already at this size
            command = "ffmpeg -i " + filename + " -vf scale=1280:720 BBB_720p.mp4"
            s = 0

        if s == 2:
            command = "ffmpeg -i " + filename + " -vf scale=854:480 BBB_480p.mp4"
            s = 0

        if s == 3:
            command = "ffmpeg -i " + filename + " -vf scale=360:240 BBB_360x240.mp4"
            s = 0

        if s == 4:
            command = "ffmpeg -i " + filename + " -vf scale=160:120 BBB_160x120.mp4"
            s = 0

        os.system(command)


# Changing the audio from stereo to mono and from mono to stereo
def task4():
    # Showing a little menu with the options and checking the option introduced by the user is correct, if not, the
    # program asks again
    # There is also an option to exit the task
    audio = 0
    while audio != 3:
        command = ""
        print("Select the type of audio:")
        print("1. Change audio to mono\n2. Change audio to stereo\n3. Exit")

        while audio < 1 or audio > 3:
            try:
                audio = int(input("Write an option (number between 1 and 3): "))
            except ValueError:
                pass

        # The program checks the option and changes audio from mono to stereo or from stereo to mono depending on
        # what the user chooses
        if audio == 1:
            command = "ffmpeg -i BBB.mp4 -ac 1 mono.mp4"
            audio = 0

        if audio == 2:
            command = "ffmpeg -i monoBBB.mp4 -ac 2 stereo.mp4"
            audio = 0

        os.system(command)


# Main function that calls each task
def main():
    # The program shows a menu with different options to choose
    option = 0
    # If the option is 5, the program finishes
    while option != 5:
        print("Select an option from the menu:")
        print("1. Cut the video\n2. YUV histogram\n3. Resize the video\n4. Change audio type\n5. Exit")

        # Here the program checks if the introduced option is one of the correct ones
        while option < 1 or option > 5:
            try:
                option = int(input("Write an option (number between 1 and 5): "))
            except ValueError:
                pass

        # If the option is one of the correct ones, the program calls the corresponding function to execute the task
        if option == 1:
            task1()
            option = 0

        elif option == 2:
            task2()
            option = 0

        elif option == 3:
            task3()
            option = 0

        elif option == 4:
            task4()
            option = 0


# Calling the main function to execute the program
main()
