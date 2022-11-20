from functools import partial
from tkinter import *
import os


# Function to execute a command
def execute_command(cmd: StringVar):
    os.system(cmd.get())


# Function to select the video file with the selected resolution
def select_video(n, file):
    # Checking the chosen resolution by the associated number (n) and setting the corresponding video to the variable
    # "file"
    if n == 1:
        file.set("BBB.mp4")

    elif n == 2:
        file.set("BBB_480p.mp4")

    elif n == 3:
        file.set("BBB_360x240.mp4")

    elif n == 4:
        file.set("BBB_160x120.mp4")


# Function to select the command to convert the video into the selected codec
def select_command(n, file: StringVar, cm):
    # Auxiliary variable to save the corresponding command
    cmnd = ""

    # Checking the chosen codec by the associated number (n) and saving the corresponding command in "cmnd"
    if n == 1:
        cmnd = "ffmpeg.exe -i " + file.get() + " -c:v libvpx -b:v 1M -c:a libvorbis BBB_VP8.webm -y"

    elif n == 2:
        cmnd = "ffmpeg.exe -i " + file.get() + " -c:v libvpx-vp9 -b:v 2M BBB_VP9.webm -y"

    elif n == 3:
        cmnd = "ffmpeg.exe -i " + file.get() + " -c:v libx265 -c:a copy -x265-params crf=25 BBB_h265.mov -y"

    elif n == 4:
        cmnd = "ffmpeg.exe -i " + file.get() + " -c:v libaom-av1 -crf 30 -b:v 0 BBB_AV1.mkv -y"

    # Now the command "cmnd" is set into the variable "cm"
    cm.set(cmnd)


# Function to mix 4 videos in 1
def mix_4videos(cm):
    # Auxiliary variable to save the corresponding command
    cmnd = ""

    # First, we check if 4 videos with different codecs exist, which means the user has chosen 4 different codecs to do
    # the conversion
    if os.path.exists("BBB_VP8.webm") and os.path.exists("BBB_VP9.webm") and os.path.exists(
            "BBB_h265.mov") and os.path.exists("BBB_AV1.mkv"):
        # If so, a command to execute the order of joining the 4 videos in 1 is saved in the variable "cmnd"
        cmnd = 'ffmpeg.exe -i BBB_VP8.webm -i BBB_VP9.webm -i BBB_h265.mov -i BBB_AV1.mkv -filter_complex "[0:v][' \
                  '1:v]hstack[t];[2:v][3:v]hstack[b];[t][b]vstack[v]; [0:a][1:a][2:a][3:a]amerge=inputs=4[a]" -map ' \
                  '"[v]" -map "[a]" -ac 2 -shortest mixBBB.mp4 -y'
        # Sets in "cm" the command saved in "cmnd"
        cm.set(cmnd)
        # The function "execute_command" is called to execute the command saved in "cm"
        execute_command(cm)

    # If there are not 4 videos with different codecs, the user is told to create one video with each codec
    else:
        print("4 videos are needed to execute this order, please create 1 video with every codec.")

    # As an additional comment, if the 4 videos do not have the same resolution, the conversion will fail


# Executing the main program that will show the interface
if __name__ == "__main__":
    # Creating the instance of the interface window
    window = Tk()

    # Creating the variables needed in this program with StringVar(), that is how Tkinter works with variables
    filename = StringVar()
    command = StringVar()

    # Specifying the size of the window
    canvas = Canvas(window, height=700, width=800)
    canvas.pack()

    # Creating a black screen inside the window where the buttons of the interface will be
    frame = Frame(window, background="black")
    frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

    # SELECTING THE VIDEO TO BE CONVERTED
    label1 = Label(frame, text="Select the video you want to convert:", background="black", foreground="white",
                   font=("Arial", 10))
    label1.place(relx=0, rely=0.1, relwidth=0.4, relheight=0.1)

    # Creating the corresponding buttons to choose the video to be converted

    # If this button is clicked, the order to be executed calls "select_video" with the number associated to this button
    # and the variable "filename" where the corresponding video file will be saved (same for all buttons)
    order = partial(select_video, 1, filename)
    button1 = Button(frame, text="720p", background="purple2", font=("Arial", 12), command=order)
    button1.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)

    order = partial(select_video, 2, filename)
    button2 = Button(frame, text="480p", background="purple2", font=("Arial", 12), command=order)
    button2.place(relx=0.1, rely=0.4, relwidth=0.2, relheight=0.1)

    order = partial(select_video, 3, filename)
    button3 = Button(frame, text="360x240", background="purple2", font=("Arial", 12), command=order)
    button3.place(relx=0.1, rely=0.6, relwidth=0.2, relheight=0.1)

    order = partial(select_video, 4, filename)
    button4 = Button(frame, text="160x120", background="purple2", font=("Arial", 12), command=order)
    button4.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1)

    # SELECTING THE CONVERSION
    label2 = Label(frame, text="Select the conversion you want to do:", background="black", foreground="white",
                   font=("Arial", 10))
    label2.place(relx=0.4, rely=0.1, relwidth=0.4, relheight=0.1)

    # Creating the corresponding buttons to select the command to convert the corresponding video to the chosen codec

    # If this button is clicked, the order to be executed calls "select_command" with the number associated to this
    # button, the video file previously chosen and the variable "command" where the corresponding command will be saved
    # (same for all buttons)
    order = partial(select_command, 1, filename, command)
    button5 = Button(frame, text="VP8", background="DeepSkyBlue3", font=("Arial", 12), command=order)
    button5.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.1)

    order = partial(select_command, 2, filename, command)
    button6 = Button(frame, text="VP9", background="DeepSkyBlue3", font=("Arial", 12), command=order)
    button6.place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.1)

    order = partial(select_command, 3, filename, command)
    button7 = Button(frame, text="h265", background="DeepSkyBlue3", font=("Arial", 12), command=order)
    button7.place(relx=0.5, rely=0.6, relwidth=0.2, relheight=0.1)

    order = partial(select_command, 4, filename, command)
    button8 = Button(frame, text="AV1", background="DeepSkyBlue3", font=("Arial", 12), command=order)
    button8.place(relx=0.5, rely=0.8, relwidth=0.2, relheight=0.1)

    # Creating the button to execute the chosen command with the chosen video file
    # If the button is clicked, "execute_command" is called with the command previously saved to execute that command
    order = partial(execute_command, command)
    button9 = Button(frame, text="Convert", background="SeaGreen1", font=("Arial", 11), command=order)
    button9.place(relx=0.8, rely=0.5, relwidth=0.1, relheight=0.1)

    # Creating the button to mix 4 videos in 1
    # If this button is clicked, the order calls "mix_4videos"
    order = partial(mix_4videos, command)
    button10 = Button(frame, text="Join 4 videos", background="MediumVioletRed", font=("Arial", 12), command=order)
    button10.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)

    # Calling the main
    window.mainloop()
