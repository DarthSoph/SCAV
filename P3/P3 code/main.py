import os


# Create a HLS transport stream container
def task1():
    filename = "BBB.mp4"

    # Command to create the HLS transport stream container
    # From line 14 to line 15: Read a video and scale it to multiple resolutions
    # From line 16 to line 24: Transcode the video to multiple bit rates
    # From line 25 to line 32: Create a HLS playlist
    # Line 31: Create a master playlist
    command = 'ffmpeg -i ' + filename + ' -filter_complex "[0:v]split=3[v1][v2][v3]; \
    [v1]copy[v1out]; [v2]scale=w=1280:h=720[v2out]; [v3]scale=w=640:h=360[v3out]" \
    -map [v1out] -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M \
    -bufsize:v:0 10M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
    -map [v2out] -c:v:1 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M \
    -bufsize:v:1 3M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
    -map [v3out] -c:v:2 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M \
    -bufsize:v:2 1M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
    -map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
    -map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
    -map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
    -f hls \
    -hls_time 2 \
    -hls_playlist_type vod \
    -hls_flags independent_segments \
    -hls_segment_type mpegts \
    -hls_segment_filename stream_%v/data%02d.ts \
    -master_pl_name master.m3u8 \
    -var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" stream_%v.m3u8'

    os.system(command)


# Create a MPD video file with encryption Widevine
def task2():
    filename = "BBB.mp4"

    # Get the info of the video
    command = "mp4info " + filename
    os.system(command)

    # Get fragmented video
    command = "mp4fragment --fragment-duration 10000 " + filename + " BBBfrag.mp4"
    os.system(command)

    # Confirm the video is fragmented
    command = "mp4info " + filename
    os.system(command)

    # Packaging the video using Widevine DRM
    command = "mp4dash --widevine-header provider:widevine_test#content_id:2a --encryption-key\
    90351951686b5e1ba222439ecec1f12a:0a237b0752cbf1a827e2fecfb87479a2 BBBfrag.mp4"
    os.system(command)


# Livestream with ffmpeg
def task3():
    filename = "BBB.mp4"

    # Command to livestream the BBB.mp4 video
    command = "ffmpeg -re -i " + filename + " -vcodec libx264 -f mpegts udp://10.1.0.102:4444"

    os.system(command)


# Main menu
def main():
    option = 0
    while option != 4:
        print("Select an option from the menu:")
        print("1. Task 1\n2. Task 2\n3. Task3\n4. Exit")

        while option < 1 or option > 4:
            try:
                option = int(input("Write an option (number between 1 and 4): "))
            except ValueError:
                pass

        if option == 1:
            task1()
            option = 0

        if option == 2:
            task2()
            option = 0

        if option == 3:
            task3()
            option = 0


# Calling the main menu
main()
