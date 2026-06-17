import actions.actions

class Student():
    
    def __init__(self, name, section, spanish, english, social, science):
        self.name = name
        self.section = section
        self.grades = { "Spanish" : spanish,
                       "English" : english,
                       "Social" : social,
                       "Science" : science                       
                       }