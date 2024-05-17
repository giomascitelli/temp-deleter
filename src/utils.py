import os

# Get user profile directory
def get_user_profile():
    return os.getenv('USERPROFILE')

# Windows temp directories
def get_temp_dirs(user_profile):
    return [
        r"C:\Windows\Temp",
        os.path.join(user_profile, r"AppData\Local\Temp"),
        r"C:\Windows\Panther",
        r"C:\Windows\SoftwareDistribution\Download",
        os.path.join(user_profile, r"AppData\Local\Microsoft\Windows\Explorer")
    ]

