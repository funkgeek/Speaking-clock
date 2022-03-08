# Running environment description


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
- It contains recordings of number from 0 to 60, and "the current time is", "and","am","pm".

### Troubleshooting Note

- Jupyter notebook or Jupyter Lab is the reconmended IDE.
  - The code for speech recognition function doesn't work on google colab notebook, because google colab have trouble with reaching the local microphone.
  - The code for playing audio function doesn't work on Spyder, because Spyder doesn't support the Audio widget of IPython.
- The program can't run without internet connection.
- The keyword "time" is needed to activate the speaking clock. So when you ask the time, please include the word "time" in your sentence.

---

### License and Data

- This program and the relevant files is provided under the Creative Commons Zero v1.0 Universal
- The data in this repository is protected by GDPR. For further contact, please use the issues board of this repo to ask for permission.
- Files in this github repository(https://github.com/funkgeek/Speaking-clock) is part of my data backup plan.

---

### Program Description

- This project is an educational exercise of me. The basic funtion of this program is to recognize your question about time, and generating the audio files which are concatenated from my recordings.
- The used languge is English and it is a 12 hour clock with am/pm.
