# temp-deleter v1.2
A script whose sole purpose is to delete temporary files from your operating system (currently **Windows** and **Linux**).

The changes made in version 1.1 **(currently only on Windows)** are that instead of flooding the user's terminal when they run the script, temp-deleter generates a log file that records the status of which files were successfully deleted and which ones could not be removed.

In addition to that, to prevent the log file from becoming excessively large over time, each script execution refreshes it. Each time the script runs, the log file is updated and overwritten with the most recent information.

Currently, on **Windows**, this script deletes the contents of the following folders:

```
'C:\Windows\Temp',    # System temporary files
'%USERPROFILE%\AppData\Local\Temp',    # User temporary files
'C:\Windows\Panther',    # Windows setup logs
'C:\Windows\SoftwareDistribution\Download',    # Windows update downloads
'%USERPROFILE%\AppData\Local\Microsoft\Windows\Explorer'    # File Explorer settings and cache
```


Currently, on **Linux (Ubuntu)**, this script deletes the contents of the following folders:

```
'/tmp',    # Temporary files
'/var/tmp',    # Persistent temporary files
'/.cache',    # General cache
'var/cache',    # System cache
'var/cache/apt/archives',    # Apt package cache
'/.config',    # User configuration
'/var/log'    # System logs
```

# Why would I want to use this script anyway?
temp-deleter offers a convenient way to manage temporary files on your operating system. But why would I want to do that?

1. <b>Optimization:</b> Temporary files accumulate over time, slow down your computer's performance, and occupy disk space unnecessarily.
   
2. <b>Privacy and Security:</b> Temporary files may also contain sensitive information, such as cached data or logs. Deleting these files regularly with temp-deleter helps safeguard your privacy by reducing the risk of unauthorized access to such data.

# How to use temp-deleter on Windows
![temp-deleter1 2printscreen](https://github.com/giomascitelli/temp-deleter/assets/47045018/37e2b7e0-5660-4e03-8390-d904b32576fe)

Open the executable as <b>admin</b> and see the results.

# For advanced users (Optional):

To store log files in your Azure cloud, add your container's SAS URL to `logging_setup.py` to enable this feature.

## Steps to enable Azure Cloud Logging on temp-deleter:

1. Clone this repository using GitHub or the following command:
   ```
   git clone <repository_url>
   ```

3. Make sure you have Python 3 installed by typing in your terminal the following command:
   ```
   python --version
   ```

5. Open `src\logging_setup.py` and update the line
   ```
   sas_url = ''
   ```
   to:
   ```
   sas_url = 'your_containers_sas_url'
   ```

### Setting Up an Azure Container:

1. <b>Create an Azure Account:</b>
- Sign up for a free or paid subscription on the <a href="https://azure.microsoft.com/en-us/free/" target="_blank">Microsoft Azure website</a>.


2. <b>Create a Storage Account:</b>
- Go to "Storage Accounts" and follow the prompts to create your storage account.


3. <b>Create a Container</b>
- Go to "Data Storage".
- Create a new container.


4. <b>Generate a Shared Access Signature (SAS):</b>
- Go to your container and click on "Shared Access Tokens".
- Ensure "Read", "Add", "Create" and "Write" permissions are checked.
- Set the start and expiry dates and times.
- Generate the SAS URL and copy it to your clipboard.
