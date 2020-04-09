import fnmatch
import os
import win32api


def get_images():
    matches = []
    forbiden_dirs = ['Windows', 'Program Files', 'Program Files (x86)', 'AMD', 'AppData', 'Users', 'ProgramData', 'AircraftAdmin-Free']


    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)

    for drive in drives:
        for root, dirnames, filenames in os.walk(drive):
            for filename in filenames:

                if filename.endswith(('.jpg', '.jpeg', '.gif', '.png')):
                    path = os.path.join(os.getcwd(), root, filename)

                    if not any(ext in path for ext in forbiden_dirs):

                        matches.append(path)

    return matches
