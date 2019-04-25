class LexicalAnalyzer:
    def __init__(self,min_dfa):
        self.token_class =[]
        self.attribute_value = {}

    def read_input_code(self , input_file):
        '''
        function reads input java code
        :param input_file:
        :return:
        '''
        # TODO
        print()