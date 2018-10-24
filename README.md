# Loop Tools

[![GuardRails badge](https://badges.production.guardrails.io/mrstephenneal/looptools.svg)](https://www.guardrails.io)

looptools is a Python package with helper utility classes for logging output, timing processes and counting iterations.

_Almost every Python project involves some form of logging, timing and counting.  Loop Tools provides a lightweight package for handling these needs without rewriting similar snippets for multiple projects._


### How it works

Loop Tools is built entirely with Python builtins so it has no external dependencies.  The Counter class uses simply math as well as the option to add leading zeros to integers.  The LogOut class created a '_logs' folder and saves a text file with the current date as its filename to capture console output or any other text.  The Timer class records start time and returns the elapsed time in either seconds or minutes upon end method call.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Upgrade to the latest version of pip

```
pip install --upgrade pip
```

### Installing

Install the latest version of dirutility from PyPi or github

PyPi distribution

```
pip install looptools
```

GitHub distribution

```
pip install git+git://github.com/mrstephenneal/looptools.git
```
or

```
pip install git+https://github.com/mrstephenneal/looptools.git
```

## Example Usage

Outlined below are basic uses of the four main classes of the Loop Tools python package.

* Counter - Counts number of iterations in a process
* LogOutput - Save logged output to a text file
* Timer - Get time elapsed during a process

## Contributing

Please read [CONTRIBUTING.md](https://github.com/mrstephenneal/psdconvert/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/psdconvert/tags). 

## Authors

* **Stephen Neal** - *Initial work* - [StephenNeal](https://github.com/mrstephenneal)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details