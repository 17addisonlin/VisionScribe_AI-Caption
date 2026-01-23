<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System">
    <img src="image/caption.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">AI-Powered-Image-Captioning-System</h3>

  <p align="center">
    Upload an image and get an AI-generated caption or a social-ready caption with tone, emojis, and hashtags.
    <br />
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System">View Demo</a>
    &middot;
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running-locally">Running Locally</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#troubleshooting">Troubleshooting</a></li>
    <li><a href="#security--privacy-notes">Security & Privacy Notes</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/17addisonlin/AI-Powered-Image-Captioning-System)

This project is a lightweight web app that generates AI captions from uploaded images. It supports a standard caption mode and a social caption mode with tone, emojis, and hashtags.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![FastAPI][FastAPI-badge]][FastAPI-url]
* [![PyTorch][PyTorch-badge]][PyTorch-url]
* [![Transformers][Transformers-badge]][Transformers-url]
* [![HTML5][HTML5-badge]][HTML5-url]
* [![CSS3][CSS3-badge]][CSS3-url]
* [![JavaScript][JavaScript-badge]][JavaScript-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Features

- Upload images and generate AI captions
- Social caption mode with tone, emojis, and hashtags
- Clean UI with preview and drag-and-drop upload
- FastAPI backend with vision-language models

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisites

- Python 3.11 (recommended)
- Conda or venv

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/17addisonlin/AI-Powered-Image-Captioning-System.git
   cd AI-Powered-Image-Captioning-System
   ```
2. Create and activate an environment
   ```sh
   conda create -n captioning python=3.11 -y
   conda activate captioning
   ```
3. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```

### Running Locally

1. Start the server
   ```sh
   uvicorn backend.main:app --reload
   ```
2. Open `http://127.0.0.1:8000`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

1. Upload an image in Caption mode to get a short description.
2. Switch to Social mode to generate a social-ready caption.
3. Choose tone and toggle emojis/hashtags if desired.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Troubleshooting

- **Slow startup:** models download on first run; allow extra time.
- **Dependency errors:** verify you are using the `captioning` environment.
- **Blank caption:** try a different image or reduce image size.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Security & Privacy Notes

- Images are processed locally by your server; nothing is uploaded unless you deploy it.
- If you deploy publicly, add authentication and rate limiting.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [ ] Enhance UI
- [ ] Add features
- [ ] Add dark/white toggle background

See the [open issues](https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are welcome. If you have improvements or bug fixes, please open an issue or submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Addison Lin - [LinkedIn](https://www.linkedin.com/in/addison-lin-227)

Project Link: [https://github.com/17addisonlin/AI-Powered-Image-Captioning-System](https://github.com/17addisonlin/AI-Powered-Image-Captioning-System)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
* [PyTorch](https://pytorch.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[contributors-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[forks-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/network/members
[stars-shield]: https://img.shields.io/github/stars/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[stars-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/stargazers
[issues-shield]: https://img.shields.io/github/issues/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[issues-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/issues
[license-shield]: https://img.shields.io/github/license/17addisonlin/AI-Powered-Image-Captioning-System.svg?style=for-the-badge
[license-url]: https://github.com/17addisonlin/AI-Powered-Image-Captioning-System/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/addison-lin-227
[product-screenshot]: image/caption demo.jpg
[FastAPI-badge]: https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/
[PyTorch-badge]: https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white
[PyTorch-url]: https://pytorch.org/
[Transformers-badge]: https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000
[Transformers-url]: https://huggingface.co/docs/transformers/index
[HTML5-badge]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/HTML
[CSS3-badge]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[JavaScript-badge]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=000
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
