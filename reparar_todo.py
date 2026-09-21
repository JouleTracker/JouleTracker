import os

fixes = {
    # Doble corrupción
    '\u00ed\u00a9': 'é',  # í© -> é
    '\u00ed\u00b1': 'ñ',  # í± -> ñ
    '\u00ed\u00a1': 'á',  # í¡ -> á
    '\u00ed\u00ad': 'í',  # í­ -> í
    '\u00ed\u00b3': 'ó',  # í³ -> ó
    '\u00ed\u00ba': 'ú',  # íº -> ú
    'el\u00ed\u00a9ctrico': 'eléctrico',
    'peque\u00ed\u00b1os': 'pequeños',
    'p\u00ed\u00a9rdidas': 'pérdidas',
    'qu\u00ed\u00a9': 'qué',
    
    # Mojibake estándar UTF-8 -> Windows-1252
    'Ã³': 'ó', 'Ã­': 'í', 'Ã¡': 'á', 'Ã©': 'é', 'Ãº': 'ú', 'Ã±': 'ñ',
    'Ã¼': 'ü', 'Ã“': 'Ó', 'Ã‰': 'É', 'Ãš': 'Ú', 'Ã‘': 'Ñ',
    'Â¿': '¿', 'Â¡': '¡', 'Â': ''
}

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.md'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                original = content
                for bad, good in fixes.items():
                    content = content.replace(bad, good)
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f" Corregido: {filepath}")
                    count += 1
            except Exception as e:
                print(f" Error en {filepath}: {e}")

print(f"\n Proceso finalizado. Se corrigieron {count} archivo(s).")
