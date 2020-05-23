from classes.databse_file_handlers.serial_file_handler import SerialFileHandler


class FileHandlerFactory():
    def __init__(self):
        super().__init__()

    def return_file_handler(self, database_type, path, metapath):
        if database_type == "sequental":
            pass
        elif database_type == "serial":
            return SerialFileHandler(path, metapath)
        else:
            return "Database type not supported."
            
