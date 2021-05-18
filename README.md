# eClass-eureka
eClass eureka!
> Tested on Open eClass 3.10.2
> 
> You can see your Institutes eClass version on [Σχετικά](https://eclass.YOUR_INSTITUTE.gr/info/about.php).

## What is eureka
Eureka is a python script which uses webbot to automate and search into courses assignments files even if they are locked .

## Prerequisites
- [webbot](https://pypi.org/project/webbot/) | Web Browser automation and testing library for python with more features and simpler api than selenium

- Student must be **registered in course** that is searched by eureka. CODE can be retrieved through personal_calendar.


#### Installation

```bash
pip install webbot
```

If "No distribution found error occurs" just update setuptools using 
```bash
pip install --upgrade setuptools
```


## How to use eureka
To use eureka you simply have to set your eClass credentials as well as information of the course you wanna search.

```python
COURSE_CODE = 'ABC_U_XYZ'

ECLASS_LOGIN = 'https://eclass.uth.gr'

USERNAME = 'username' # Your eClass username
PASSWORD = 'password' # Your eClass password

BASE_URL = 'https://eclass.uth.gr/modules/work/?course='
CODE = 3014 # Μπορεί να βρεθεί από το ημερολόγιο τοποθετώντας τον δείκτη του ποντικιού πάνω στο στρογγυλό εικονίδιο 
            # της εργασίας. Ο κωδικός φαίνεται κάτω αριστερά στον browser.
            # Σε περίπτωση που η εργασία έχει ανέβει αλλά είναι κρυφή και δεν φαίνεται στο ημερολόγιο, ξεκινήστε με 
            # έναν κωδικό πρόσφατο καθώς είναι η αρίθμηση είναι σειριακή για όλο το eClass ανεξαρτήτως μαθημάτων, 
            # τμημάτων.
ITER = 100  # Αριθμός επαναλήψεων
```
