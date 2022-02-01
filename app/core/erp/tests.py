from config.wsgi import *

from core.erp.models import Asesor

# Listar
query = Asesor.objects.all()
print(query)

# Insercion
# t = Asesor(names='Gianfranco').save()
