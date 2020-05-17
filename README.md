# covid-19
Some statistics regarding infection of covid-19 in Poland with some tools that extract/plot data.

NOTE: This project will not be developed anymore. I just wanted to get some basic skills in page parsing and plotting data.

## Instalation
1. Create virtual environment
```shell
python -m venv venv
```
2. Install requirements
```shell
pip install -r requirements.txt
```
3. Activate virtual env
```shell
source venv/bin/activate
```
## Usage
To compare data from two diffirent days:
```shell
python compare_data.py data/covid-19-pl20200320-101649.json data/covid-19-pl20200324-160907.json
```
