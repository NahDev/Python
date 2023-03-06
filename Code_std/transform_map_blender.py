import bpy

# Abre o arquivo com o mapa
with open("mapa.txt", "r") as f:
    mapa = f.readlines()

# Obtém as dimensões do mapa
linhas = len(mapa)
colunas = len(mapa[0]) - 1

# Cria uma matriz para armazenar os valores do mapa
matriz = [[0 for x in range(colunas)] for y in range(linhas)]

# Preenche a matriz com os valores do mapa
for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = mapa[i][j]

# Cria uma malha 3D para representar o mapa
mesh = bpy.data.meshes.new("Mapa")
object = bpy.data.objects.new("Mapa", mesh)
bpy.context.collection.objects.link(object)

# Adiciona vértices à malha
vertices = []
for i in range(linhas):
    for j in range(colunas):
        x = j
        y = i
        z = matriz[i][j]
        vertices.append((x, y, z))

# Adiciona faces à malha
faces = []
for i in range(linhas - 1):
    for j in range(colunas - 1):
        a = j + i * colunas
        b = a + 1
        c = a + colunas
        d = c + 1
        faces.append((a, b, c, d))

# Atribui os vértices e as faces à malha
mesh.from_pydata(vertices, [], faces)
mesh.update()

