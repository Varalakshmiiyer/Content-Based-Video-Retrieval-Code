# Content-Based-Video-Retrieval-Code

## Usage

```
python app/main.py --model <model> --mode <mode> (--debug)
```

where:

* `--model` indicates the histogram model to use. Can be "all", "gray", "rgb" or "hsv". "all" will use the 3 histogram models to train/test the system.
* `--mode` indicates the mode to run in. Can be "train" or "test".
* `--debug` is an optional flag. If the flag is set, additional logs will be printed for debugging purposes.
* `--showhists` is an optional flag. If the flag is set, all of the generated histograms will be displayed.

Examples:

* To train the system: `python app/main.py --model all --mode test`
* To test the system: `python app/main.py --model all --mode train`
* To train the system with RGB only: `python app/main.py --model rgb --mode train`
* To test the system with HSV only in debug mode: `python app/main.py --model hsv --mode test --debug`

## Installation

* Clone the project
```
cd ~/Projects
git clone https://github.com/Adamouization/Content-Based-Video-Retrieval-Code
cd Content-Based-Video-Retrieval-Code
```

* Create a new virtual environment with Python 3

`virtualenv -p python3 ~/Environments/Content-Based-Video-Retrieval-Code`

* activate the virtual environment

`source ~/Environments/Content-Based-Video-Retrieval-Code/bin/activate`

* Install project dependencies

`pip install -r requirements.txt`


## TODO Project Boards

* [Project Presentation](https://github.com/Adamouization/Content-Based-Video-Retrieval-Code/projects/1) (18/02/2019)
* [Project Enhancements](https://github.com/Adamouization/Content-Based-Video-Retrieval-Code/projects/2) (07/05/2019)

## License

* see [LICENSE](https://github.com/Adamouization/Content-Based-Video-Retrieval-Code/blob/master/LICENSE) file

## Contact
* email: adam@jaamour.com
* LinkedIn: [www.linkedin.com/in/adamjaamour](https://www.linkedin.com/in/adamjaamour/)
* website: www.adam.jaamour.com
* twitter: [@Adamouization](https://twitter.com/Adamouization)
