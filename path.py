import os


def file_path(file_name, path):
    for r, d, f in os.walk(path):
        for file in f:
            filepath = os.path.join(r, file)
            if file_name in file:
                return os.path.join(r, file)


