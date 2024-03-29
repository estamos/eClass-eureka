# Import libraries
from webbot import Browser
import time

# -----------------------------------------------------------------------------------------
# COURSE_NAME  (COURSE_CODE)
# COURSE_INSTRUCTOR
# https://eclass.uth.gr/courses/COURSE_CODE/

# Εργασίες
# https://eclass.uth.gr/modules/work/?course=COURSE_CODE
# https://eclass.uth.gr/modules/work/index.php?course=COURSE_CODE&id=CODE
# -----------------------------------------------------------------------------------------

COURSE_NAME = 'COURSE_NAME'
COURSE_CODE = 'ABC_U_XYZ'

ECLASS_LOGIN = 'https://eclass.uth.gr'

USERNAME = 'username' # Your eClass username
PASSWORD = 'password' # Your eClass password

# URL = 'https://eclass.uth.gr/modules/work/?course=COURSE_CODE&get=CODE&file_type=1'
BASE_URL = 'https://eclass.uth.gr/modules/work/?course='
CODE = 3014 # Μπορεί να βρεθεί από το ημερολόγιο τοποθετώντας τον δείκτη του ποντικιού πάνω στο στρογγυλό εικονίδιο 
            # της εργασίας. Ο κωδικός φαίνεται κάτω αριστερά στον browser.
            # Σε περίπτωση που η εργασία έχει ανέβει αλλά είναι κρυφή και δεν φαίνεται στο ημερολόγιο, ξεκινήστε με 
            # έναν κωδικό πρόσφατο καθώς είναι η αρίθμηση είναι σειριακή για όλο το eClass ανεξαρτήτως μαθημάτων, 
            # τμημάτων.
ITER = 100  # Αριθμός επαναλήψεων
PDF = '&file_type=1'

DOWNLOAD_URL = BASE_URL + COURSE_CODE + '&get=' + str(CODE) + PDF
# -----------------------------------------------------------------------------------------

print('Εκκίνηση Google Chrome')
web = Browser()
web.go_to(ECLASS_LOGIN)
print('Σύνδεση σε ' + ECLASS_LOGIN)
web.type(USERNAME , into='username')
web.type(PASSWORD , into='password' , id='pass') # specific selection
print('-------------------------------------------------------')
print('Σύνδεση χρήστη')
print('\nΌνομα χρήστη (username):', USERNAME,'\nΣυνθηματικό (password):', PASSWORD, '\n')
print('-------------------------------------------------------')
web.click('Είσοδος' , tag='button') # you are logged in ^_^

# -----------------------------------------------------------------------------------------
print('Κατέβασμα αρχείων\n')
while CODE <= CODE + ITER:
    print(COURSE_NAME + ' | Εργασίες | ID =', CODE)
    web.go_to(DOWNLOAD_URL)
    CODE = CODE + 1

print('-------------------------------------------------------')
print('Τερματισμός Google Chrome')
web.quit()
