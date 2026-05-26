class LoggableMixin:
    def log_info(self):
        class_name = self.__class__.__name__
        return class_name