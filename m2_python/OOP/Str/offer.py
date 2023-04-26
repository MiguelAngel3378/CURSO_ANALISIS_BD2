
# CREAR CLASE OFFER QUE REPRESENTE UNA OFERTA DE TRABAJO
# TITLE, COMPANY, SALARY, WORKMODE, EXP_YEARS



class Jobffer:
    def __init__(self, title, company, salary, workmode, exp_years):
        self.title = title
        self.company = company
        self.salary = salary
        self.workmode = workmode
        self.exp_years = exp_years

    def __str__(self):
        return 'Offer %s %s %s %s %s' % (self.title, self.company, self.salary, self.workmode, self.exp_years)
    
offer1 = Jobffer('Analista_datos', 'Adecco', 20000, 'Hibrido', 1)
offer2 = Jobffer('Database_controler', 'IBM', 25000, 'Presencial', 2)
print(offer1)
print(offer2)