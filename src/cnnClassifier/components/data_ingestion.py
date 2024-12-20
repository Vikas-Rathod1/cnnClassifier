import os
from urllib import request
from zipfile import ZipFile, BadZipFile, is_zipfile
from cnnClassifier.entity import (DataIngestionConfig)
from pathlib import Path

import tqdm
from cnnClassifier import logger
from cnnClassifier.utils import get_size # to check the file size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Check if the local zip file already exists
        if not os.path.exists(self.config.local_data_file):
            print(f"Downloading file from {self.config.source_URL}...")
            try:
                # Download the zip file from the GitHub raw URL
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                print(f"File downloaded to {self.config.local_data_file}")
            except Exception as e:
                print(f"Error downloading file: {e}")

    def _get_updated_list_of_files(self, list_of_files):
        # Filter files based on your criteria (e.g., .jpg files with "men" or "women" in the name)
        return [f for f in list_of_files if f.endswith(".jpg") and ("men" in f or "women" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        # Define the target file path
        target_filepath = os.path.join(working_dir, f)
        
        # Extract the file if it doesn't exist already
        if not os.path.exists(target_filepath):
            try:
                print(f"Extracting {f}...")
                zf.extract(f, working_dir)
            except Exception as e:
                print(f"Error extracting file {f}: {e}")
                return
        
        # Remove empty files
        if os.path.getsize(target_filepath) == 0:
            print(f"Removing empty file {target_filepath}...")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        # Check if the local zip file exists
        if not os.path.exists(self.config.local_data_file):
            print(f"Local zip file not found at {self.config.local_data_file}")
            return
        
        # Check if the file is a valid zip file
        if not is_zipfile(self.config.local_data_file):
            print(f"Error: The file {self.config.local_data_file} is not a valid zip file.")
            return
        
        try:
            # Open the zip file
            with ZipFile(file=self.config.local_data_file, mode="r") as zf:
                list_of_files = zf.namelist()
                updated_list_of_files = self._get_updated_list_of_files(list_of_files)
                
                # Preprocess each file in the updated list
                for f in updated_list_of_files:
                    self._preprocess(zf, f, self.config.unzip_dir)  # type: ignore
                print("Unzipping and cleaning completed.")
        except BadZipFile:
            print(f"Error: The file {self.config.local_data_file} is not a valid zip file.")
        except Exception as e:
            print(f"Error during unzip and clean process: {e}")


# class DataIngestion:
#     def __init__(self, config: DataIngestionConfig):
#         self.config = config

#     def download_file(self):
#         logger.info("Trying to download file...")
#         if not os.path.exists(self.config.local_data_file):
#             logger.info("Download started...")
#             filename, headers = request.urlretrieve(
#                 url=self.config.source_URL,
#                 filename=self.config.local_data_file
#             )
#             logger.info(f"{filename} download! with following info: \n{headers}")
#         else:
#             logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")        

#     def _get_updated_list_of_files(self, list_of_files):
#         return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]

#     def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
#         target_filepath = os.path.join(working_dir, f)
#         if not os.path.exists(target_filepath):
#             zf.extract(f, working_dir)
        
#         if os.path.getsize(target_filepath) == 0:
#             logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
#             os.remove(target_filepath)

#     def unzip_and_clean(self):
#         logger.info(f"unzipping file and removing unawanted files")
#         with ZipFile(file=self.config.local_data_file, mode="r") as zf:
#             list_of_files = zf.namelist()
#             updated_list_of_files = self._get_updated_list_of_files(list_of_files)
#             for f in tqdm(updated_list_of_files): # type: ignore
#                 self._preprocess(zf, f, self.config.unzip_dir) # type: ignore