import os


# Globals
path = os.path.dirname(__file__)


# This function checks the option the user has introduced and selects the corresponding video
def select_video(n):
    file = ""

    # The chosen file corresponds to the resolution chosen by the user in the menu
    # The function saves the corresponding video in a new variable called "file"
    if n == 1:
        file = "BBB.mp4"

    elif n == 2:
        file = "BBB_480p.mp4"

    elif n == 3:
        file = "BBB_360x240.mp4"

    elif n == 4:
        file = "BBB_160x120.mp4"

    # At the end, the function returns the chosen file
    return file


# This function checks the option the user has introduced and selects the corresponding command
def select_command(n, file):
    cm = ""

    # The chosen command corresponds to the codec chosen by the user in the menu
    # The function saves the corresponding command in the new variable "cm", depending on the chosen codec and with the
    # file chosen previously
    if n == 1:
        cm = "ffmpeg -i " + file + " -c:v libvpx -b:v 1M -c:a libvorbis BBB_VP8.webm "

    elif n == 2:
        cm = "ffmpeg -i " + file + " -c:v libvpx-vp9 -b:v 2M BBB_VP9.webm"

    elif n == 3:
        cm = "ffmpeg -i " + file + " -c:v libx265 -c:a copy -x265-params crf=25 BBB_h265.mov"

    elif n == 4:
        cm = "ffmpeg -i " + file + " -c:v libaom-av1 -crf 30 -b:v 0 BBB_AV1.mkv"

    # The function returns the variable cm where the command is saved
    return cm


# This function mixes 4 converted videos in 1
def mix_4videos():
    # First, we check if 4 videos with different codecs exist, which means the user has chosen 4 different codecs to do
    # the conversion
    if os.path.exists("BBB_VP8.webm") and os.path.exists("BBB_VP9.webm") and os.path.exists(
            "BBB_h265.mov") and os.path.exists("BBB_AV1.mkv"):
        # If so, a command to execute the order of joining the 4 videos in 1 is executed
        command = 'ffmpeg -i BBB_VP8.webm -i BBB_VP9.webm -i BBB_h265.mov -i BBB_AV1.mkv -filter_complex "[0:v][' \
                  '1:v]hstack[t];[2:v][3:v]hstack[b];[t][b]vstack[v]; [0:a][1:a][2:a][3:a]amerge=inputs=4[a]" -map ' \
                  '"[v]" -map "[a]" -ac 2 -shortest mixBBB.mp4'
        os.system(command)

    # If there are not 4 videos with different codecs, the user is told to execute again the program to create one video
    # with each codec
    else:
        print("4 videos are needed to execute this order, please execute the code again and create 1 video with "
              "every codec.")

    # As an additional comment, if the 4 videos do not have the same resolution, the conversion will fail


# Main menu
def main():
    # The program asks the user if he wants to convert the video
    # After each conversion, it will ask again in order to be able to convert any of the available videos the times the
    # user wants
    option = 0
    while option != 2:
        print("Do you want to convert the video?")
        print("1. Yes\n2. No")

        # The user introduces an answer and the program checks if it is a correct option, if not it asks again
        while option < 1 or option > 2:
            try:
                option = int(input("Write an option (number 1 or 2): "))
            except ValueError:
                pass

        # If the answer was "Yes" (option 1), the program shows the 4 options of resolution to choose
        if option == 1:
            video = 0
            print("\n")
            print("Select the video you want to use:")
            print("1. 720p\n2. 480p\n3. 360x240\n4. 160x120")

            # The user introduces an option and the program checks if it is a correct one
            while video < 1 or video > 4:
                try:
                    video = int(input("Write an option (number between 1 and 4): "))
                except ValueError:
                    pass

            # Now the program calls the function select_video with the chosen option by the user and saves the chosen
            # file in a new variable "filename"
            filename = select_video(video)

            # Now, the program shows the user the 4 options of codecs to convert the video to that it has
            conversion = 0
            print("\n")
            print("Select the conversion you want to do:")
            print("1. VP8\n2. VP9\n3. h265\n4. AV1")

            # The user introduces an option and the program checks if it is correct
            while conversion < 1 or conversion > 4:
                try:
                    conversion = int(input("Write an option (number between 1 and 4): "))
                except ValueError:
                    pass

            # The program calls select_command with the option chosen of the codec and with the filename returned by the
            # function select_video
            command = select_command(conversion, filename)

            # Finally, the command is executed in order to convert the chosen video to a new video with the chosen codec
            os.system(command)
            print("\n")
            option = 0

    # When the user finally decides to stop converting videos, the program will ask a last question to know if the user
    # wants to join 4 videos in 1
    answer = 0
    print("\n")
    print("Do you want to join 4 videos in 1?")
    print("1. Yes\n2. No")

    # The user introduces an answer and the program checks if it is a correct option
    while answer < 1 or answer > 2:
        try:
            answer = int(input("Write an option (number 1 or 2): "))
        except ValueError:
            pass

    # If the answer was "Yes", the the program calls the corresponding function, mix_4videos()
    if answer == 1:
        mix_4videos()


# Here the main menu is called
main()
