import os


# Writing a path

filepath = os.path.join('folder1', 'folder2', 'file.png') # OS-neutral path definition
print(filepath) # output: folder1\folder2\file.png


# Getting current working folder

cwd = os.getcwd()
print(cwd)


# Changing folder

os.chdir('c:\\')
print(os.getcwd()) # output: c:\


# Absolute and relative filepaths

'c:\\fakefile.png'  # Absolute path for a file, starts with the root folder
'fakefile.png'      # Relative path (relative to the current folder)

'\\folder1\\folder2\\fakefile.png'  # Relative path, assumes there is such a path in the c:\ root


# . (current) and .. (parent) folders

# Assuming we are in C:\currentfolder:

'.\\fakefolder'     # Points to C:\currentfolder\fakefolder
'..\\fakefolder'    # Points to C:\fakefolder


# Returning the absolute path of a relative path

absol = os.path.abspath('fakefile.png')
print(absol)    # Output: c:\fakefile.png


# Checking if a path is absolute

abs_check = os.path.isabs('.\\fakefolder\\fakefile.png')   # Returns True if abs, False if not
print(abs_check)    # Output: False
abs_check = os.path.isabs('c:\\fakefolder\\fakefile.png')
print(abs_check)    # Output: True


# Get a relative path based on your cwd

rel_path = os.path.relpath('c:\\folder1\\folder2\\fakefile.png', 'c:\\folder1') # param #1 is the target path, param #2 the cwd
print(rel_path) # output: folder2\fakefile.png


# Get the folder part of a path

dir_path = os.path.dirname('c:\\folder1\\folder2\\fakefile.png')
print(dir_path) # Output: c:\folder1\folder2


# Get the part of the path after the last folder separator

base_name = os.path.basename('c:\\folder1\\folder2\\fakefile.png')
print(base_name)    # Output: fakefile.png


# Checking if a path exists

path_exists = os.path.exists('c:\\folder1\\folder2\\fakefile.png')
print(path_exists)  # Output: False


# Checking is a file exists / if the basename is a file

file_exists = os.path.isfile('c:\\folder1\\folder2\\fakefile.png')
print(file_exists)  # Output: False


# Checking if a folder exists / if the basename is a folder

dir_exists = os.path.isdir('c:\\folder1\\folder2\\')
print(dir_exists)  # Output: False


# Get the size of a file in bytes

get_size = os.path.getsize('c:\\windows\\system32\\calc.exe')
print(get_size) # Output: 27648


# Get the listing of a folder

get_listing = os.listdir('c:\\windows\\system32')
print(get_listing)


# Creating folders

os.makedirs('c:\\fakefolder\\fakechild\\fakegrandchild')
