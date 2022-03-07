RELATIVE_DIR=`dirname "$0"`

poetry run pytest $RELATIVE_DIR/../body/test_google.py --alluredir=allure-results