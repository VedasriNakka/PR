# Note: 
# You need the train.csv and test.csv in the same directory


# Run without any installation:
python3 01-KNN.py


# Install requirements in virtualenv

virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt
python3 01-KNN.py 2>&1 | tee 01-KNN.py.log
deactivate


