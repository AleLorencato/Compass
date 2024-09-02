import hashlib

texto = input("Digite algum texto: ")

hash_sha1 = hashlib.sha1(texto.encode())

print("Hash SHA-1:", hash_sha1.hexdigest())
