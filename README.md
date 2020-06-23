<!-- Source https://github.com/othneildrew/Best-README-Template/ -->
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPLv3 License][license-shield]][license-url]


*The project is currently under development so all features have not yet been developed.*

# Quantum Image Encryption

An implementation of the 2017 paper on quantum image encryption based on NEQR, 2-D logistic sine map, bit-planes, and gray codes.

[Request Feature](https://github.com/harshitgarg22/quantum_image_encryption/issues)



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Quantum Image Encryption](#quantum-image-encryption)
  - [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
    - [Built With](#built-with)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)
  - [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project


This is part of the work that I am doing for Practice School-1 internship at UST Global. This project aims to implement Quantum Image Encryption as specified in [this paper](https://ieeexplore.ieee.org/document/8119911) (IEEE link). It uses NEQR, bit-planes, gray codes, and 2-D logistic sine map to achieve this.


### Built With

* [qiskit](https://qiskit.org/)
* [Pillow](https://github.com/python-pillow/Pillow/)



<!-- GETTING STARTED -->
## Getting Started

This short tutorial will guide you to set-up the python environment, generate a random image and run the a demo of the program.

### Prerequisites

1. Clone the repo
```sh
git clone https://github.com/harshitgarg22/quantum_image_encryption.git
```
2. Install packages (**Create a virtual environment first!**)
```sh
python3 -m pip install -r requirements.txt
```
3. (Optional) Generate random 4x4 grayscale pixel image (stored as random.png).
```sh
python3 image.py
```


<!-- USAGE EXAMPLES -->
## Usage

Start demo from `main.py`
```sh
python3 main.py
```
This will take up the image `random.png` and output the encrypted image.



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/harshitgarg22/quantum_image_encryption/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Harshit Garg - hg1229@gmail.com

Project Link: [github.com/harshitgarg22/quantum_image_encryption/](https://github.com/harshitgarg22/quantum_image_encryption)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[forks-shield]: https://img.shields.io/github/forks/harshitgarg22/quantum_image_encryption
[forks-url]: https://github.com/harshitgarg22/quantum_image_encryption/network/members
[stars-shield]: https://img.shields.io/github/stars/harshitgarg22/quantum_image_encryption
[stars-url]: https://github.com/harshitgarg22/quantum_image_encryption/stargazers
[issues-shield]: https://img.shields.io/github/issues/harshitgarg22/quantum_image_encryption
[issues-url]: https://github.com/harshitgarg22/quantum_image_encryption/issues
[license-shield]: https://img.shields.io/github/license/harshitgarg22/quantum_image_encryption
[license-url]: https://github.com/harshitgarg22/quantum_image_encryption/blob/master/LICENSE

