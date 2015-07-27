#! python3
# Update.py - Updates Python packages


import os, pip

# Adds all of the installed packages to a set 

packs = set()
for pack in pip.get_installed_distributions():
    packs.add(pack.project_name.lower())

# Updates the packages

for pack_name in packs:
    cmd = 'python -m pip install {0} --upgrade'.format(pack_name)
    print('$ ' + cmd)
    try:
        os.system(cmd)
    except Exception:
        print('Error while updating')
    print('')




