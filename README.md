# django-default-language

django-default-language is a Django middleware for setting a default language in bi/multilingual Django project.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install django-default-language.

```bash
pip install django-default-language
```

## Usage

### Step 1. Add DefaultLanguageMiddleware (in settings.py file)
```python
MIDDLEWARE = [
    # ...
    'language.DefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # ...
]
```
Make sure DefaultLanguageMiddleware is before LocaleMiddleware. 
Otherwise, Django will default to use the requesting browser's default language from the 'Accept-Language' request header (e.g. Accept-Language: fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5).

### Step 2. Specify default language (in settings.py file)
```python
LANGUAGE_CODE = 'zh-Hans'  # default language
```

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)
