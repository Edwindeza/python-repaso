class Language:
    def __init__(self, nombre, año):
        self.nombre= nombre
        self.año = año
    def description(self):
        print('%s fue creado en %s' % (self.nombre, self.año))

javascript = Language('Javascript', 1995)
javascript.description()