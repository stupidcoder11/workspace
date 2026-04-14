class Logger:
    _instance = None

    def __init__(self):
        pass
    
    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger._instance = Logger()
        return Logger._instance

    def info(self, message: str):
        print(f"INFO: {message}")
    
    def warning(self, message: str):
        print(f"WARNING: {message}")
    
    def error(self, message: str):
        print(f"ERROR: {message}")
    
if __name__ == "__main__":
    l1 = Logger.get_instance()
    l2 = Logger.get_instance()
    assert l1 is l2
    l1.info("This is a log message.")
    l2.warning("This is another log message.")