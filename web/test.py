import environ
env = environ.Env()
environ.Env.read_env()

print(str(env('SECRET_KEY')))
