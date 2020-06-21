from utils import (
    logistic_sine_map,
    neqr,
    scramble,
    cnot,
    inverse_scramble,
    quantum_to_pillow,
)


def generate_quantum_key(key):
    quantum_key = logistic_sine_map(key=key)
    quantum_key = neqr(quantum_key)

    return quantum_key


def generate_quantum_image(image):
    neqr_image = neqr(image)
    quantum_image = scramble(neqr_image=neqr_image)

    return quantum_image


def encrypt(image, key):
    quantum_key = generate_quantum_key(key=key)
    quantum_image = generate_quantum_image(image)

    quantum_encrypted_image = cnot(quantum_image=quantum_image, quantum_key=quantum_key)

    return quantum_encrypted_image


def decrypt(quantum_encrypted_image, key):
    quantum_key = generate_quantum_key(key)
    scrambled_image = cnot(quantum_encrypted_image, quantum_key)
    quantum_decrypted_image = inverse_scramble(scrambled_image=scrambled_image)
    decrypted_image = quantum_to_pillow(quantum_decrypted_image)

    return decrypted_image
