<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/avict18/car-insurance-id">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Car Insurance ID Checker</h3>

  <p align="center">
    A system to check car insurance status by uploading CSV files of plate numbers and verifying through a government API.
    <br />
    <a href="https://github.com/avict18/car-insurance-id"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/avict18/car-insurance-id">View Demo</a>
    ·
    <a href="https://github.com/avict18/car-insurance-id/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/avict18/car-insurance-id/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

This project allows users to check the registration status of car insurance by uploading a CSV file containing car plate numbers. The system sends the data to a government API and retrieves the verification result.


### Built With

* [![Python][Python-shield]][Python-url]
* [![Pandas][Pandas-shield]][Pandas-url]
* [![Requests][Requests-shield]][Requests-url]


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

You will need the following installed:
* Python 3.x
* Pandas library
  ```sh
  pip install pandas
Installation
Clone the repo
sh
Copy code
git clone https://github.com/avict18/car-insurance-id.git
Install Python packages
sh
Copy code
pip install -r requirements.txt
<!-- USAGE EXAMPLES -->
Usage
Place your MV_Insurance.csv file in the project directory.
Run the Python script to check registration status:
sh
Copy code
python check_registration.py
The results will be saved in a registration_results.csv file.
<!-- ROADMAP -->
Roadmap
 Feature 1: Add support for more data formats.
 Feature 2: Automate CSV upload through UI.
 Feature 3: Improve error handling for API requests.
<!-- CONTRIBUTING -->
Contributing
Contributions are what make the open source community such an amazing place to learn and create. Any contributions you make are greatly appreciated.

> Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
<!-- LICENSE -->
License
Distributed under the MIT License. See LICENSE.txt for more information.

Project Link: <a href="https://github.com/avict18/car-insurance-id">https://github.com/avict18/car-insurance-id</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p> 

[Python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Pandas-shield]: https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white
[Pandas-url]: https://pandas.pydata.org/
[Requests-shield]: https://img.shields.io/badge/Requests-FF4F00?style=for-the-badge&logo=requests&logoColor=white
[Requests-url]: https://requests.readthedocs.io/
