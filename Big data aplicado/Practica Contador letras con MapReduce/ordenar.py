import subprocess

entrada_reducers = open("entrada_reducer_fi.txt","w")

subprocess.run(["sort", "salida_mapper_fi.txt"], stdout=entrada_reducers, check=True)

