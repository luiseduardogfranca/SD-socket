class Codes:
    def __init__(self):
        self.code_arr = [10, 12, 13, 14]
        self.code_dic = {
            10: "success",
            11: "not found",
            12: "method not found",
            13: "error in request",
            14: "entity not found",
        }
    
    def get_msg(self, code_input):
        return code_input, self.code_dic[code_input]