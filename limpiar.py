import os

candidates = ["report/README.md", "README.md"]
target = None
for c in candidates:
    if os.path.exists(c):
        target = c
        break

if not target:
    print("❌ No se encontró ningún README.md en report/ ni en la raíz.")
    exit()

print(f"Procesando: {target}")

with open(target, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

fixes = {
    'í©': 'é', 'í±': 'ñ', 'í¡': 'á', 'í­': 'í', 'í³': 'ó', 'íº': 'ú',
    'pí©': 'pé', 'quí©': 'qué',
    'Ã³': 'ó', 'Ã­': 'í', 'Ã¡': 'á', 'Ã©': 'é', 'Ãº': 'ú', 'Ã±': 'ñ',
    'Ã¼': 'ü', 'Ã“': 'Ó', 'Ã‰': 'É', 'Ãš': 'Ú', 'Ã‘': 'Ñ',
    'Â¿': '¿', 'Â¡': '¡', 'Â': ''
}

for bad, good in fixes.items():
    text = text.replace(bad, good)

with open(target, 'w', encoding='utf-8') as f:
    f.write(text)

print("✅ Limpieza completada con éxito en " + target)
