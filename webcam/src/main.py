import subprocess
import datetime
import os


def record_webcam(
    output_dir="videos", segment_time=300, resolution="1280x720", framerate=30
):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate output filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_template = os.path.join(output_dir, f"output_{timestamp}_%03d.mp4")

    # FFmpeg command to capture from the webcam and split into segments
    ffmpeg_command = [
        "ffmpeg",
        "-f",
        "avfoundation",  # For macOS webcam capture
        "-framerate",
        str(framerate),  # Set the framerate
        "-video_size",
        resolution,  # Set the resolution
        "-i",
        "0",  # Input device (webcam)
        "-vf",
        f"fps={framerate}",  # Set frame rate for video filter
        "-f",
        "segment",  # Split the video into segments
        "-segment_time",
        str(segment_time),  # Duration of each segment
        "-reset_timestamps",
        "1",  # Reset timestamps for each segment
        output_template,  # Output file pattern
    ]

    try:
        # Start the FFmpeg process
        print(f"Recording started. Saving files to {output_dir}/")
        subprocess.run(ffmpeg_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while recording: {e}")
    except KeyboardInterrupt:
        print("Recording stopped by user.")
    finally:
        print("Recording finished.")


if __name__ == "__main__":
    # You can customize these values
    segment_duration = 5  # Segment length in seconds (5 minutes)
    video_resolution = "1280x720"  # Resolution (HD)
    frame_rate = 30  # Frames per second

    # Start recording webcam
    record_webcam(
        segment_time=segment_duration, resolution=video_resolution, framerate=frame_rate
    )
