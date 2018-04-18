from apps.usuarios.forms import LoginForm
from apps.inmueble.forms import ImagenesForm
def add_variable_context(request):
    return{
        'login':LoginForm,
        'imagenesForm':ImagenesForm
    }
