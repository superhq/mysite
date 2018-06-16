import os
from photo_collector.digest import CalDigest
from photo_collector.models import Files

class FileDigest:
    def walk_dir(self, path):
        try:
            for name in os.listdir(path):
                file_path = os.path.join(path, name)
                if os.path.isdir(file_path):
                    self.walk_dir(file_path)
                else:
                    print(file_path)
                    digest = CalDigest.get_md5(file_path)
                    self.file_digest_to_db(file_path, digest)

        except Exception as e:
            print(e)

    def file_digest_to_db(self,path,digest):
        file = Files(path=path, digest=digest)
        file.save()
