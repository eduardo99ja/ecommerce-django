### How to SETup in Windows/MAC/Linux
1. Clone this Project <code>git clone https://github.com/eduardo99ja/ecommerce-django.git </code>
2. Go to Project Directory <code>cd greatKart </code>
3. Create a Virtual Environment :-
    * for Windows <code>python -m venv env </code>
    * for Linux/Mac <code>python3 -m venv env </code>
4. Activate Virtual Environment <code> .\env\Scripts\activate </code>
5. Install Requirment Packages <code>pip install -r requirements.txt</code>
6. Migrate Database :-
    * For Windows <code>python manage.py migrate</code>
    * For Linux/Mac <code>python3 manage.py migrate</code>
7. Create SuperUser :-
    * For Windows <code>python manage.py createsuperuser</code>
    * For Linux/Mac <code>python3 manage.py createsuperuser</code>
8. Finally Run the Projects :-
    * For Windows <code>python manage.py runserver</code>
    * For Linux/Mac <code>python3 manage.py runserver</code>