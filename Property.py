class roperties:

    def __init__(self, case_number, case_type, case_type_number, case_name, houses, is_mortgaged, owner):

        self.case_number = case_number
        self.case_type = case_type
        self.case_type_number = case_type_number
        self.case_name = case_name
        self.houses = houses
        self.is_mortgaged = is_mortgaged
        self.owner = owner

    def get_case_name(self):
        return self.case_name

    def get_full_name(self):
        return self.case_type + str(self.case_type_number) + self.case_name

    def get_houses(self):
        return self.houses

    def get_is_mortgaged(self):
        return self.is_mortgaged

    def get_owner(self):
        return self.owner

    def get_case_type(self):
        return self.case_type


