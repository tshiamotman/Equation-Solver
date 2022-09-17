import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'equationsolver.settings')
django.setup()

from equationsolverapp.dispatcher import run_polling

print("django")
if __name__ == "__main__":
    run_polling()