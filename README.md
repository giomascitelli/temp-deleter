# temp-deleter
A script whose sole purpose is to delete temporary files from your operating system (currently **Windows** and **Linux**).

Currently on **Windows**, this script deletes the contents of the following folders:

```
'C:\Windows\Temp',
'%USERPROFILE%\AppData\Local\Temp',
'C:\Windows\Panther',
'C:\Windows\SoftwareDistribution\Download',
'%USERPROFILE%\AppData\Local\Microsoft\Windows\Explorer'
```


Currently on **Linux (Ubuntu)**, this script deletes the contents of the following folders:

```
'/tmp',
'/var/tmp',
'/.cache',
'var/cache',
'var/cache/apt/archives',
'/.config',
'/var/log'
```

# Why would I want to use this script anyway?
temp-deleter offers a convenient way to manage temporary files on your operating system. But why would I want to do that?

1. <b>Optimization:</b> Temporary files accumulate over time, slow down your computer's performance, and occupy disk space unnecessarily.
   
2. <b>Privacy and Security:</b> Temporary files may also contain sensitive information, such as cached data or logs. Deleting these files regularly with temp-deleter helps safeguard your privacy by reducing the risk of unauthorized access to such data.

# How to use temp-deleter
![image](https://github.com/giomascitelli/temp-deleter/assets/47045018/ace098e6-029d-463d-a81a-e88647069f55)

Open the executable as <b>admin</b> and see the results.

# How to run the .py file

1. Make sure you have Python 3 installed.

2. Open the Windows Terminal as an administrator

3. Type "cd" and the path to the folder where you placed "temp-deleter.py":

```
   cd C:\Users\Username\Desktop
```

5. Run the script:

```
   python temp-deleter.py
```
