import hashlib

text = input("Hashlenecek metni gir: ")

md5_hash = hashlib.md5(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
sha512_hash = hashlib.sha512(text.encode()).hexdigest()

print("\n[+] Hash sonuçları:\n")

print(f"MD5:    {md5_hash}")
print(f"SHA256: {sha256_hash}")
print(f"SHA512: {sha512_hash}")
