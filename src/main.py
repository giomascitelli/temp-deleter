from deleter import clear_temp_directories
from logging_setup import setup_logging, upload_log_to_blob
from utils import get_user_profile, get_temp_dirs

def main():
    user_profile = get_user_profile()
    setup_logging()
    temp_dirs = get_temp_dirs(user_profile)
    deleted_files = clear_temp_directories(temp_dirs)
    upload_log_to_blob("temp-deleter.log")

    # Print results
    if not deleted_files:
        print("\nNo files were deleted.")
    else:
        print(f"\n{len(deleted_files)} files were deleted. Check the log file for more details.")

    input("\n Press Enter to exit...")

if __name__ == "__main__":
    main()

