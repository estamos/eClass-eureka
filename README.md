# eClass-eureka
eClass eureka!

## What is eureka
Eureka is a python script which uses webbot to automate and search into courses assignments files even if they are locked .

## How to use eureka
To use eureka you simply have to set your eClass credentials as well as information of the course you wanna search.

```python
COURSE_CODE = 'ABC_U_XYZ'

ECLASS_LOGIN = 'https://eclass.uth.gr'

USERNAME = 'username' # Your eClass username
PASSWORD = 'password' # Your eClass password

BASE_URL = 'https://eclass.uth.gr/modules/work/?course='
CODE = 3014 # Ξεκινήστε με έναν κωδικό πρόσφατο καθώς είναι η αρίθμηση είναι σειριακή για όλο το eClass
            # ανεξαρτήτως μαθημάτων , τμημάτων
ITER = 100  # Αριθμός επαναλήψεων
```

## Dependencies
- [webbot](https://pypi.org/project/webbot/)
Web Browser automation and testing library for python with more features and simpler api than selenium

#### Installation

```bash
pip install webbot
```

If "No distribution found error occurs" just update setuptools using 
```bash
pip install --upgrade setuptools
```
