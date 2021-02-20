import unicodedata

# NFC - Mantém caracteres pré-compostos
nome = 'Ot\u0061\u0301vio'
normalized = unicodedata.normalize('NFC', nome)

# \u0061\u0301 is normalized to U+0076
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized])

# NFD - O contrário do NFC. Mantém caracteres separados
nome = 'Ot\u00e1vio'
normalized = unicodedata.normalize('NFD', nome)

# \u0061\u0301 is normalized to U+0076
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized])

nome = 'OM™'
normalized1 = unicodedata.normalize('NFKC', nome)
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

nome = 'OMTM'
normalized2 = unicodedata.normalize('NFKC', nome)
print(normalized2)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized2])

print(normalized1 == normalized2)

normalized1 = unicodedata.normalize('NFKC', "°")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

normalized1 = unicodedata.normalize('NFKC', "o")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

normalized1 = unicodedata.normalize('NFKC', "ᴼ")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

normalized1 = unicodedata.normalize('NFKC', "ᵒ")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

normalized1 = unicodedata.normalize('NFKC', "№")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

normalized1 = unicodedata.normalize('NFKC', "No")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

normalized1 = unicodedata.normalize('NFKC', "Nº")
print(normalized1)
print(['U+' + hex(ord(letra))[2:].zfill(4).upper() for letra in normalized1])

