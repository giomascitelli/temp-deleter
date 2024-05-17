import logging

# Setting up logging configuration to write to a file and overwrite it every time the script runs
def setup_logging():
    logging.basicConfig(filename='temp_deleter.log', filemode='w', level=logging.INFO)

