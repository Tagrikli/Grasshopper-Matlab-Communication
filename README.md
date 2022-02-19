# Grasshopper Matlab Communicator

Custom script to allow communication between Rhino 3D Grasshopper and Matlab.

Make sure that Matlab and Rhino 3D installed.

## Preperation

1. Install Python 3.8
2. Prepare virtual environment
    ```bash
    python -m venv env
    source env/bin/activate
    pip install --upgrade pip
    ```
3. Install required dependencies

    ```bash
    pip install -R requirements.txt
    ```

4. Install matlab.engine module
    ```bash
    cd "matlabroot\extern\engines\python"
    python setup.py install
    ```
5. Place the .fis file exported from Matlab Fuzzy Logic Toolbox into the src folder.

## Compability

Tested with Python 3.8, should work with 3.7 and 3.9
