# covid-19
Some statistics regarding infection of covid-19 in Poland with some tools that extract/plot data

## Instalation
1. Create virtual environment

python -m venv venv

2. Install requirements

pip install -r requirements.txt

3. Activate virtual env

source venv/bin/activate

## Usage
To compare data from two diffirent days:

python compare_data.py data/covid-19-pl20200320-101649.json data/covid-19-pl20200324-160907.json
