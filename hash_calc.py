import hashlib
from typing import Generator, IO

MB = 2 ** 20


def _read_in_chunks(file_object: IO[bytes], chunk_size: int = 2*MB) -> Generator[bytes, None, None]:
    while True:
        chunk = file_object.read(chunk_size)
        if chunk:
            yield chunk
        else:
            return


def compute_hashes(file_path):
    sha = hashlib.sha256()
    md5 = hashlib.md5()
    with open(file_path, mode='rb') as file_object:
        for chunk in _read_in_chunks(file_object):
            sha.update(chunk)
            md5.update(chunk)
    return sha.hexdigest(), md5.hexdigest()