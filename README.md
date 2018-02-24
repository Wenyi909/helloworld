# helloworld
## Installation
Clone the repo and use pip to install it.

	git clone https://github.com/Wenyi909/helloworld.git
	cd helloworld/
	pup install .

## CLI Usage
To use the executable helloworld command line program:

	$ helloworld -h
	usage: helloworld [-h] [--howold] [--emotion]

	optional arguments:
		-h, --help            show this help message and exit
		--howold              print random age
		--emotion             print random feeling

## API Usage
To use the helloworld Python API

	import helloworld
	helloworld.helloworld(howold = True, emotion = True)


