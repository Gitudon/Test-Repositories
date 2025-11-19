import hashlib
import random
import string


class HashCalculator:
    def calculate_md5_hash(string: str) -> str:
        md5_hash = hashlib.md5()
        md5_hash.update(string.encode("utf-8"))
        return md5_hash.hexdigest()

    def calculate_sha256_hash(string: str) -> str:
        sha256_hash = hashlib.sha256()
        sha256_hash.update(string.encode("utf-8"))
        return sha256_hash.hexdigest()


class RandomStringGenerator:
    def generate_random_string(length: int) -> str:
        characters = string.ascii_letters
        return "".join(random.choice(characters) for _ in range(length))


class TestHashCalculation:
    def test_with_random_strings(test_count: int, string_length: int):
        for _ in range(test_count):
            random_string = RandomStringGenerator.generate_random_string(string_length)
            md5_hash = HashCalculator.calculate_md5_hash(random_string)
            sha256_hash = HashCalculator.calculate_sha256_hash(random_string)
            print(f"Random String: {random_string}")
            print(f"MD5 Hash     : {md5_hash}")
            print(f"SHA256 Hash  : {sha256_hash}")
            print("-" * 40)

    def test_with_fixed_string(test_count: int, fixed_string: str):
        for _ in range(test_count):
            md5_hash = HashCalculator.calculate_md5_hash(fixed_string)
            sha256_hash = HashCalculator.calculate_sha256_hash(fixed_string)
            print(f"Fixed String: {fixed_string}")
            print(f"MD5 Hash    : {md5_hash}")
            print(f"SHA256 Hash : {sha256_hash}")
            print("-" * 40)

    def test_with_certain_strings(certain_strings: list):
        for string in certain_strings:
            md5_hash = HashCalculator.calculate_md5_hash(string)
            sha256_hash = HashCalculator.calculate_sha256_hash(string)
            print(f"Certain String: {string}")
            print(f"MD5 Hash      : {md5_hash}")
            print(f"SHA256 Hash   : {sha256_hash}")
            print("-" * 40)


if __name__ == "__main__":
    TestHashCalculation.test_with_certain_strings(
        ["example1", "example2", "123456", "abcdefg"]
    )
