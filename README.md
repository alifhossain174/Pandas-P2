## Insall Pandas in local environment
1. cd /path/to/your/folder
2. python -m venv venv (Create Virtual ENV)
3. venv\Scripts\activate (Activate the ENV)
4. pip install pandas
5. pip install openpyxl
6. deactivate (Deactivate the ENV)

## As the venv will not be stored in the git we have to mention the libraries in requirements.txt
1. create requirements.txt
2. venv\Scripts\activate (Activate the ENV)
3. Run pip freeze > requirements.txt 

it will store the library versions inside that txt file to use later on when someone clone the repo

## After Cloning
1. git clone https://github.com/yourusername/yourproject.git
2. cd yourproject
3. python -m venv venv
4. venv\Scripts\activate
5. pip install -r requirements.txt

Now the developer will have the exact same packages and versions you had in your local setup.