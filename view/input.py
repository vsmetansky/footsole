class Input:
    @staticmethod
    def get_input(help_str=''):
        if isinstance(help_str, str):
            return str(input(help_str))
        return ''
