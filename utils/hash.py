import hashlib

def calc_hash(filename):
    sha256_hash = hashlib.sha512()
    with open(filename,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

