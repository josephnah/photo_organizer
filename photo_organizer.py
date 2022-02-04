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
            print(file)

            # get date time of file
            file_date = datetime.datetime.fromtimestamp(os.path.getctime(file))

            # Get date into desirable folder format
            creation_date = file_date.strftime("%Y") + '/' + file_date.strftime("%m") + '-' + file_date.strftime("%d") + '/'

            # Designate destination folder
            destination_folder = data_omega_dir + str.upper(file_ext) + '/' + creation_date

            # create folder if it does not exist
            os.makedirs(destination_folder, exist_ok=True)

            # Check if file already exists in location
            check_file_destination = Path(destination_folder+file_name)

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

move_photos(file_ext='jpg', camera_type='fuji')





