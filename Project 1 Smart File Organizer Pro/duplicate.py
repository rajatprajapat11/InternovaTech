import os
import hashlib


def get_file_hash(file_path):
    """
    Generate SHA-256 hash for a file.
    """
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                sha256.update(chunk)

        return sha256.hexdigest()

    except Exception:
        return None


def find_duplicates(folder_path):
    """
    Find duplicate files using SHA-256 hashing.
    """

    hashes = {}

    duplicates = []

    duplicate_size = 0

    for root, _, files in os.walk(folder_path):

        for file in files:

            path = os.path.join(root, file)

            file_hash = get_file_hash(path)

            if file_hash is None:
                continue

            if file_hash in hashes:

                original = hashes[file_hash]
                duplicate = path

                original_name = os.path.basename(original).lower()
                duplicate_name = os.path.basename(duplicate).lower()

                # If the stored file contains "copy" but the new one doesn't,
                # swap them so the normal filename becomes the original.
                if "copy" in original_name and "copy" not in duplicate_name:
                    original, duplicate = duplicate, original

                duplicates.append((original, duplicate))

                duplicate_size += os.path.getsize(duplicate)

            else:

                hashes[file_hash] = path

    return duplicates, duplicate_size