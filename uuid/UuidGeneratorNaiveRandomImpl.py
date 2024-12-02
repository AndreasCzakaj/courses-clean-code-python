import random

class UuidGeneratorNaiveRandomImpl:
    def __init__(self):
        self.random = random.SystemRandom()  # Secure random equivalent to SecureRandom

    def create(self):
        sb = []
        for _ in range(32):
            sb.append(self.create_one())
        return ''.join(sb)

    def create_one(self):
        return hex(self.random.randint(0, 15))[2:]  # Generate a hex digit (0-15) and strip the "0x"
