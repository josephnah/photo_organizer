import os
import glob
import datetime
from pathlib import Path
import shutil
import time
import personal_paths


def move_photos(file_ext, camera_type):
    x = time.time()
    # define file extension that you want to move
    if file_ext == 'raw' and camera_type == 'fuji':
        file_ext_type = 'raf'
    elif file_ext == 'raw' and camera_type == 'sony':
        file_ext_type = 'arw'
    elif file_ext == 'raw' and camera_type == 'canon':
        file_ext_type = 'cr2'
    elif file_ext == 'raw' and camera_type == 'nikon':
        file_ext_type = 'nef'
    else:
        file_ext_type = file_ext

    bulk_file_ext = '*' + str.upper(file_ext_type)

    # directories and file extensions
    data_alpha_dir = personal_paths.data_alpha_dir
    data_omega_dir = personal_paths.data_omega_dir

    print('Begin photo import!')

    # Get total # of files
    import_list_file = glob.glob(data_alpha_dir + bulk_file_ext)

    print(f'A total of {len(import_list_file)} photos, {str.lower(file_ext)}s to be specific\n')

    if len(import_list_file) > 0:
        print(f'Copying {file_ext}s...')

        for file in import_list_file:

            # Get basename of file
            file_name = os.path.basename(file)

            # get date time of file, compare access, create, and modified time to  get earliest timestamp
            file_date_access = os.path.getatime(file)
            file_date_create = os.path.getctime(file)
            file_date_modified = os.path.getmtime(file)

            file_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(min(file_date_access, file_date_create, file_date_modified)))

            # Get date into desirable folder format
            creation_date = str(file_date[0:4]) + '/' + str(file_date[5:7]) + '-' + str(file_date[8:10])

            # Designate destination folder
            destination_folder = data_omega_dir + str.upper(file_ext) + '/' + creation_date

            # create folder if it does not exist
            os.makedirs(destination_folder, exist_ok=True)

            # Check if file already exists in location
            check_file_destination = Path(destination_folder + file_name)

            # Copy file to directory only if it doesn't exist already
            if check_file_destination.is_file():
                print('Already exists, moving on')
            else:
                # Copy file to destination, preserving timestamp
                shutil.copy2(file, destination_folder)
                # print(destination_folder)

    else:
        print('Nothing to move today! Go grab a coffee or a beer or both...')

    time_elapsed = time.time() - x
    print(f'\nDone! All photos copied in {(round(time_elapsed, 5))} seconds')


move_photos(file_ext='raw', camera_type='fuji')
