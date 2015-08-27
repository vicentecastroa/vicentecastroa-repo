# coding=utf-8

# Recuerda borrar los 'pass'. Pudes borrar si quieres los comentarios.


class Commit:
    commit_id = 1
    def __init__(self, message, changes=None):
        self.id = commit_id
        commit_id+=1
        self.message = message
        self.changes=[]
        if changes != None:
            self.changes.append(changes)

        self.padre=None


class Branch:
    def __init__(self,nombre):
        self.nombre=nombre
        self.last_commit=None

    def new_commit(self, commit):
        commit.padre=self.last_commit
        self.last_commit=commit

    def pull(self):
        files = []
        for i in self.last_commit.id:
            self.last_commit.pull()
                for l in commit.changes:
                    if commit.changes[l][0]=='DELETE':
                        files.remove(commit.changes[l][1])
                    if commit.changes[l][0]=='CREATE':
                        files.append(commit.changes[l][1])

        return files


class Repository:

    def __init__(self, name):
        self.name = name
        self.branch = 'master'
        self.branch..new_commit(Commit(
        message="creado master",
        changes=[("CREATE", ".jit")]
        ))


    def create_branch(self, new_branch_name, from_branch_name):
        #############
        # COMPLETAR:
        # Crear branch a partir del último estado de la 'from_branch_name'.
        #############
        pass

    def branch(self, branch_name):
        #############
        # COMPLETAR:
        # Retornar la branch con el nombre 'branch_name'.
        #############
        return None

    def checkout(self, commit_id):
        files = []
        #############
        # COMPLETAR:
        # Buscar el commit con cierta id y retornar el estado del repositorio
        # hasta ese commit. Puede estar en cualquier branch.
        #############
        return files


if __name__ == '__main__':
    # Ejemplo de uso
    # Puedes modificarlo para probar esto pero al momento de la corrección
    # el ayudante borrará cualquier cambio y restaurará las siguientes lineas
    # a su estado original (como se muestran aquí).

    repo = Repository("syllabus 2.0")

    repo.branch("master").new_commit(Commit(
        message="agregado readme",
        changes=[("CREATE", "README.md")]
    ))

    repo.branch("master").new_commit(Commit(
        message="archivos base",
        changes=[("CREATE", "main.py"), ("CREATE", "clases.py")]
    ))

    # Creamos una rama del estado actual de 'master'
    repo.create_branch("desarrollo-de-vistas", 'master')
    repo.branch("desarrollo-de-vistas").new_commit(Commit(
        message="imagenes",
        changes=[("CREATE", "main.jpg"), ("CREATE", "user.png")]
    ))

    repo.branch("desarrollo-de-vistas").new_commit(Commit(
        message="cambiar instrucciones",
        changes=[("DELETE", "README.md"), ("CREATE", "instrucciones.html")]
    ))

    repo.branch("master").new_commit(Commit(
        message="datos recolectados",
        changes=[("CREATE", "data.csv")]
    ))

    print(repo.branch("master").pull())
    # Esperamos que el repo esté así:
    # ['.jit', 'README.md', 'main.py', 'clases.py', 'data.csv']

    print(repo.branch("desarrollo-de-vistas").pull())
    # Esperamos que el repo esté así:
    # ['.jit', 'main.py', 'clases.py',
    #  'main.jpg', 'user.png', 'instrucciones.html']

    print(repo.checkout(4))
    # Esperamos que el repo esté así:
    # ['.jit', 'README.md', 'main.py', 'clases.py', 'main.jpg', 'user.png']

    print(repo.checkout(1))
    # Esperamos que el repo esté así:
    # ['.jit']
