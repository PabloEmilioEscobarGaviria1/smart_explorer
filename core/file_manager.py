import os

class FileManager:

    def list_files(self, path):

        files = []

        try:
            for f in os.listdir(path):
                files.append(os.path.join(path, f))
        except:
            pass

        return files

    def is_folder(self, path):

        return os.path.isdir(path)