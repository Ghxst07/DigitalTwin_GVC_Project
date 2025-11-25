# Project Title: Image-Based Digital Twin Construction for VR Walkthrough
### Topic Mapping: Topic #4 / #19 (Digital Twin / Smart Classroom Walkthrough)

---

## Student Details
* **Name:** ARINDOL SARKAR
* **Roll No:** 24CD3007
* **Course:** Graphics and Visual Computing (GVC)
* **Submission Date:** November 2025

---

## 1. Objective
To construct an immersive 3D environment (Digital Twin) by computationally stitching discrete 2D images into a panoramic texture and rendering it onto a spherical manifold using perspective projection. This project demonstrates the pipeline from 2D image acquisition to 3D virtual environment visualization, adhering to the GVC modeling pipeline.

---

## 2. Methodology & Pipeline
The project follows a three-stage GVC pipeline:

### A. Data Acquisition (Input)
* Captured a sequence of overlapping frames of the target environment using a standard camera sensor.
* Maintained a fixed nodal point during capture to minimize parallax error.

### B. Image Processing (Python & OpenCV)
* **Feature Extraction:** Used ORB (Oriented FAST and Rotated BRIEF) to detect keypoints in overlapping frames.
* **Homography Estimation:** Computed the transformation matrix to align images on a common plane.
* **Warping & Blending:** Warped images into a Cylindrical/Equirectangular projection and blended seams to create a continuous panorama[cite: 1, 6].

### C. 3D Rendering & Visualization (Unity / WebGL)
* **Texture Mapping:** The stitched 2D panorama was mapped onto the interior normals of a 3D Sphere (Skybox) to simulate infinite depth.
* **Viewing Transformation:** Implemented a perspective camera with 3-DoF (Degrees of Freedom) rotational control to allow user navigation.

---

## 3. Roll Number Customization (Mandatory Requirement)
Per the project guidelines [5, 17], specific project parameters are procedurally controlled by my Roll Number.

* **Roll No:** 24CD3007
* **Control Value (Last 2 Digits):** 07
* **Parameter:** Camera Rotation Sensitivity / Speed

**Logic & Calculation:**
The sensitivity of the camera movement (or auto-rotation speed) is derived from the control value.

> **Formula:** `Sensitivity = 100 + (Last_2_Digits * 2)`
>
> **Calculation:** `100 + (07 * 2) = 114`
>
> **Result:** The system sensitivity is locked to **114**.

---

## 4. GVC Concepts Applied [cite: 4]
This project demonstrates understanding of the following course concepts:
* **Perspective Projection:** Converting the 3D spherical world coordinates to the 2D camera view plane.
* **Texture Mapping:** Mapping 2D (u,v) coordinates of the stitched image to 3D (x,y,z) coordinates of the sphere.
* **Coordinate Systems:** Transforming between World Space (The Sphere) and View Space (The Camera).
* **Modeling Pipeline:** Utilizing image-based modeling techniques instead of traditional polygonal modeling.

---

## 5. Tools & External Libraries
* **Language:** Python 3.9 (Stitching), C# / HTML5 (Rendering)
* **Libraries:**
    * **OpenCV (`cv2`):** For image feature matching and stitching.
    * **NumPy:** For matrix operations during image processing.
    * **A-Frame / Unity Engine:** For rendering the 3D scene and handling physics/input.
* **Assets:**
    * Raw video footage/images (Self-captured).
    * AI-Based Upscaling (Nano-Banana)

---

## 6. How to Run
### Step 1: Stitching (Python)
1.  Navigate to the `Python_Script` folder.
2.  Run the command: `python main.py`
3.  This generates the `final_panorama.png` from the input frames.

### Step 2: Visualization (3D Environment)
**Option A: Web/Browser (Recommended)**
1.  Navigate to the `Build` folder.
2.  Run `LAUNCH_ME.bat` (Starts a local Python HTTP server to bypass CORS security).
3.  The browser will open automatically. Use the mouse to look around.

**Option B: Standalone App**
1.  Navigate to the `Room_stitch_project\Final_model` folder.
2.  Run `Room_Project.exe`.

3.  Use the mouse to look around. Press `Alt + F4` to exit.
