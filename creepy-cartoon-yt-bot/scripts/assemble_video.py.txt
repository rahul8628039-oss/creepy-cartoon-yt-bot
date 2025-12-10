from moviepy.editor import ImageSequenceClip
import os

def make_video():
    frames = [f"outputs/frames/frame_{i}.png" for i in range(12)]
    clip = ImageSequenceClip(frames, fps=12)
    clip.write_videofile("outputs/video.mp4", codec="libx264")

if __name__ == "__main__":
    make_video()
