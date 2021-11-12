# Running environment description

Thia is not a contribution file as I did all the works.

---

### Required package

**For runing this program, the following package installation is required and the latest version is suggested:**：

- librosa
- NumPy
- DateTime
- IPython
- SpeechRecognition

### About the recording files

- Please download the zip file named "sounds"
- After unzip it, your will get a folder named "sounds"
- Then put the folder under the same directory as the code file.

### Troubleshooting Note

- Jupyter notebook or Jupyter Lab is the reconmended IDE.
  - The code for speech recognition function doesn't work on google colab notebook, because google colab have trouble with reaching the local microphone.
  - The code for playing audio function doesn't work on Spyder, because Spyder doesn't support the Audio widget of IPython.
- The program can't run without internaet connection.
- The keyword "time" is needed to activate the speaking clock. So when you ask the time, please include the word "time" in your sentence.

---

### License and Data

This program and the relevant files is provided under the Apache License 2.0
The data in this repository is protected by GDPR. For further contact, please use the issues board of this repo to ask for permission.
Files in this github repository is part of the data backup plan.

### Program Description

This project is an educational exercise of me. The basic funtion of this program is to recognize your question about time, and generating the audio files which are concatenated from my recordings.
