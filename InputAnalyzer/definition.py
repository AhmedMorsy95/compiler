class Definition:
    def __init__(self, line):
        equal_position = line.find('=')
        self.name = line[0:equal_position].strip()
        self.value = line[equal_position + 1:].strip()
        # self.process_value_string()

    # def process_value_string(self):
