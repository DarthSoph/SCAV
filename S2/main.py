import os


# Globals
path = os.path.dirname(__file__)


def task1():
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

    filename = "BBB.mp4"
    command = "ffmpeg -i " + filename + " -s 00:00:00 -t " + time + " -c:v copy -c:a copy BBB_cut.mp4"
    os.system(command)


def task2():
    filename = "BBB_cut.mp4"
    command = "ffmpeg -i " + filename + " -vf histogram histogram.mp4"
    os.system(command)
    command = "ffmpeg -i " + filename + " -i histogram.mp4 -filter_complex '[0:v]pad=iw*2:ih[int];[int][" \
                                        "1:v]overlay=W/2:0[vid]' -map '[vid]' -c:v libx264 -crf 23 -preset veryfast " \
                                        "BBB_histogram.mp4"
    os.system(command)
    os.system("rm histogram.mp4")


def task3():
    filename = "BBB.mp4"
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

        if s == 1:
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


def task4():
    audio = 0
    while audio != 3:
        command = ""
        print("Select the type of audio:")
        print("1. Change audio to mono\n2. Change audio to stereo\n3. Exit")

        while audio < 1 or audio > 3:
            try:
                audio = int(input("Write an option (number between 1 and 3):"))
            except ValueError:
                pass

            if audio == 1:
                command = "ffmpeg -i BBB.mp4 -ac 1 mono.mp4"
                audio = 0

            if audio == 2:
                command = "ffmpeg -i monoBBB.mp4 -ac 2 stereo.mp4"
                audio = 0

            os.system(command)


def main():
    option = 0
    while option != 5:
        print("Select an option from the menu:")
        print("1. Cut the video\n2. YUV histogram\n3. Resize the video\n4. Change audio type\n5. Exit")

        while option < 1 or option > 5:
            try:
                option = int(input("Write an option (number between 1 and 5): "))
            except ValueError:
                pass

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


main()
