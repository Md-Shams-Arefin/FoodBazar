# FoodBazar

* Python 3.9.2

**First clone the repo :**

```shell
 git clone https://github.com/Md-Shams-Arefin/FoodBazar.git
```

---
**Create virtual environment based on your operating system**
 * **For ubuntu**
 ```shell
python -m venv env
  ```

  ###### Activate the virtual environment
 ```shell
source env/bin/activate
  ```
 * **For windows**
 ```shell
python -m venv venv
  ```

  ###### Activate the virtual environment
 ```shell
venv\Scripts\activate
  ```
---

**Install the requirements.txt file**
 ```shell
pip install -r requirements.txt
  ```
  * If needed then upgrade pip version. (Optional)
    ```shell
    pip install --upgrade pip
    ```
---


**Copy .env.example file to .env :**

  * For linux
    ```shell
    cp .env.example .env
    ```
  * For windows
    ```shell
    copy .env.example .env
    ```
  ###### Create Mysql database and set up in .env and fill up other necessary fields with proper credentials.

---

**Migrate all the fields**
 ```shell
python manage.py migrate
  ```

**Create superuser**
 ```shell
python manage.py createsuperuser
  ```

**Run the server**
 ```shell
python manage.py runserver
  ```

---

### Connect postgresql server

* Install postgresql and make sure postgresql server is running.
* To install postgresql you can check the docx [https://www.postgresql.org/download/]


**Restart postgresql server :**
 ```shell
sudo systemctl restart postgresql
  ```
  ###### OR
  ```
  sudo systemctl start postgresql    --start postgresql server
  sudo systemctl stop postgresql     --stop postgresql server
  ```


**Testing Postgresql :**
 ```shell
sudo systemctl status postgresql
  ```


**Run the qcluster server**
 ```shell
python manage.py qcluster
  ```
  ###### Then stop the server and run again the localhost of django

  ```shell
python manage.py runserver
  ```
  ---

