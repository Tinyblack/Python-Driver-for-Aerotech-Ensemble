class FileInfo():
    _FileInfoNET=None
    def __init__(self,FileInfoNET=AerotechEnsembleFileSystemNET.FileInfo):
        self._FileInfoNET=FileInfoNET