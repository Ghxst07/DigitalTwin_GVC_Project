"""
Exported from image-stitching.ipynb
"""

import os
import cv2
import matplotlib.pyplot as plt

VIDEO_PATH = "video_1.mp4"
MAX_FRAMES_TO_STITCH = 100
SKIP_INTERVAL = 5


def extract_frames(video_path, skip_interval, max_frames):
    print(f"Processing video: {video_path}")
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        if count % skip_interval == 0:

            height, width = frame.shape[:2]
            if width > 1000:
                scale = 1000 / width
                frame = cv2.resize(frame, (0,0), fx=scale, fy=scale)

            frames.append(frame)

            if len(frames) >= max_frames:
                print(f"Reached {max_frames} frames. Stopping extraction to save RAM.")
                break

        count += 1

    cap.release()
    return frames


def stitch_frames(frames):
    if len(frames) < 2:
        print("Error: Could not extract enough frames.")
        return None

    print(f"Stitching {len(frames)} frames with good overlap...")


    stitcher = None
    try:
        stitcher = cv2.Stitcher_create(cv2.Stitcher_SCANS)
    except Exception:
        try:
            stitcher = cv2.Stitcher_create()
        except Exception:
            stitcher = None

    if stitcher is None:
        print("Could not create OpenCV Stitcher. Check your OpenCV build.")
        return None

    status, panorama = stitcher.stitch(frames)

    if status == cv2.Stitcher_OK:
        print("Success! Panorama generated.")
        cv2.imwrite("final_panorama.png", panorama)

        plt.figure(figsize=(20, 10))
        plt.imshow(cv2.cvtColor(panorama, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
        return panorama
    else:
        print(f"Still failed. Error Code: {status}")
        print("Try changing SKIP_INTERVAL to 10 (more overlap) or 30 (less overlap).")
        return None


def main():
    frames = extract_frames(VIDEO_PATH, SKIP_INTERVAL, MAX_FRAMES_TO_STITCH)
    stitch_frames(frames)


if __name__ == "__main__":
    main()
