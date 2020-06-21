"""
This module defines utility functions to be used for encryption, decryption, and generating keys

"""

import random
from PIL import Image
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.circuit import ControlledGate
from math import log2, floor


def logistic_sine_map(key: (float, float)):
    (k0, psi) = key

    pass


def neqr(image):
    """
    neqr(image) returns the NEQR representation of a grayscale image with number of pixels as an exponent of 2.
    
    Keyword arguments:
    
    image -- A PIL image.

    Return: (grayscale_qubits, pixel_qubits) representing the grayscale image in NEQR form.
    """

    image.convert("L")
    GRAYSCALE_SIZE = 8
    WIDTH, HEIGHT = image.size
    WIDTH_QUBITS, HEIGHT_QUBITS = floor(log2(WIDTH)), floor(log2(HEIGHT))
    data = list(image.getdata())

    data = [data[offset : offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]

    # Each pixel can be accessed as data[row][col], the value will be [0, 255]
    grayscale_qubits = QuantumRegister(GRAYSCALE_SIZE)
    pixel_qubits_height = QuantumRegister(HEIGHT_QUBITS)
    pixel_qubits_width = QuantumRegister(WIDTH_QUBITS)
    qc = QuantumCircuit(grayscale_qubits, pixel_qubits_height, pixel_qubits_width)

    for qb in pixel_qubits_height:
        qc.h(qb)

    for qb in pixel_qubits_width:
        qc.h(qb)

    run_circuit(qc)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            ancillary = QuantumRegister(1)
            grayscale_binary = format(data[i][j], "0{}b".format(GRAYSCALE_SIZE))
            pixel_height_binary = format(i, "0{}b".format(HEIGHT_QUBITS))
            pixel_width_binary = format(j, "0{}b".format(WIDTH_QUBITS))

            ControlledGate(
                name="control_pixel",
                num_qubits=1,
                num_ctrl_qubits=HEIGHT_QUBITS + WIDTH_QUBITS,
                params=[],
                ctrl_state=pixel_height_binary + pixel_width_binary,
            )

            qc.control_pixel()

            # Now we have to implement the encoding of the grayscale data in the respective qubits
            for qb, ele in zip(grayscale_qubits, grayscale_binary):
                if ele == "1":
                    qc.cx(ancillary, qb)

    return (grayscale_qubits, pixel_qubits)


def scramble(neqr_image: (QuantumRegister, QuantumRegister)):
    (grayscale_qubits, pixel_qubits) = neqr_image
    n = grayscale_qubits.size
    qc = QuantumCircuit(grayscale_qubits)

    for i in range(n - 1, -1, -1):
        if i < n / 2:
            qc.cx(grayscale_qubits[i], grayscale_qubits[n - i - 1])
        else:
            qc.cx(grayscale_qubits[i], grayscale_qubits[i - n / 2])

    run_circuit(qc)

    return (grayscale_qubits, pixel_qubits)


def cnot(
    quantum_image: (QuantumRegister, QuantumRegister), quantum_key: QuantumRegister
):
    ((image_grayscale_qubits, pixel_qubits), key_grayscale_qubits) = (
        quantum_image,
        quantum_key,
    )

    qc = QuantumCircuit(image_grayscale_qubits, key_grayscale_qubits)
    for (img_qbit, key_qbit) in zip(image_grayscale_qubits, key_grayscale_qubits):
        qc.cx(key_qbit, img_qbit)

    run_circuit(qc)

    return ((image_grayscale_qubits, pixel_qubits), key_grayscale_qubits)


def generate_key():
    psi = random.randint(0, 4)
    knot = 0
    while knot != 0:
        knot = random.random()

    return (knot, psi)


def inverse_scramble(scrambled_image: (QuantumRegister, QuantumRegister)):
    (grayscale_qubits, pixel_qubits) = scrambled_image
    n = grayscale_qubits.size
    qc = QuantumCircuit(grayscale_qubits)

    for i in range(n):
        if i < n / 2:
            qc.cx(grayscale_qubits[i], grayscale_qubits[n - i - 1])
        else:
            qc.cx(grayscale_qubits[i], grayscale_qubits[i - n / 2])

    run_circuit(qc)

    return (grayscale_qubits, pixel_qubits)


def quantum_to_pillow(quantum_image):
    pass


def run_circuit(qc: QuantumCircuit):
    pass
