import os

# this function creates a directory for each result if not already created
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# this functions writes the file on the path with data
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
