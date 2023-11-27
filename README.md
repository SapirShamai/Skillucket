# Skillucket

### Overwiew
Skillucket (skill+bucket) is a web application that allows users to gain new skills through exchange, it's kind of a social midea based on learning.
Every user can list their skills that they are willing to teach and 
a bucket list of skills that they wish to learn. After the registration and filling out both lists: skills that you have and skills that you wish to learn, users can be matched 
together and learn from each other, no money involved. 

### Installation instruction
Skillucket is a Python Django project. It requires Python, pip and postgres to be installed.

After forking and cloning the project, preferably in VSCode or Pycharm, run the terminal command while being in the skillucket_v2 directory:

```
pip install -r requirements.txt
```

The next necessary step is to create a database using postgreql. For that run the commands:

```postgres
psql -U postgres -h localhost
```
And once in the postgres:
```sql
CREATE DATABASE your_database_name;
\q
```
Next create a file named .env to which copy and fill in the template: 

(or simply copy and configure .env.sample file from the project)

```
export SECRET_KEY='your_secret_key'
export DB_NAME='your_database_name'
export DB_USER='postgres'
export DB_PASSWORD='your_password'
export DB_HOST='localhost'
export DB_PORT='5432'
```
Run in the terminal:
```commandline
source .env
```
Create and run migrations to fill out the database:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Run the server to check if everything is working correctly: 
```
python3 manage.py runserver
```

### Features

- **Register** - a new user can register to our platform with email, password, username and optionally profile picture and real name.
- **Login** - user is able to login to access full functionality of our platform.
- **Profile** - a new profile is created automatically after the user been created, users can edit or delete items from their profile.
- **User Skills** - user can make a list of their skills, stating category and name of the skill, proficiency level and experience.
- **Bucket Skills** - user can make a list of skills they wish to learn. They state notes, category and name of the skill.
- **Matches** - after creating a bucket list, user can see automatically users that have the skills that he wish to learn and are willing to teach it.
- **Search Matches** - every user authenticated user can search for a skill in the search bar and see users how matches the search.

### Contributions

Skillucket began as a school group project. The contributors include Sapir Shamai, Barak Shalom, Michael-Gage Runge, Mariana Dragomir, and Róża Wadowska.

I was responsible for creating the APIs, testing them with DRF, Swagger, and Postgres, and then providing detailed documentation. This can be reviewed in the Skillucket API's directory. We deployed the project to AWS, and I crafted a comprehensive guide on this deployment process, available in the base directory. I'm deeply passionate about this project and continue to develop it independently, adding more features.

In the skillucketApp directory, I've designed views and templates that operate independently from the APIs, offering modularity and ensuring each directory is self-contained.

### Future plans

- Improve Frontend: Although I primarily focus on backend development, I plan to delve into and enhance the frontend for a more engaging user experience.
- Message to Admin: the way that the database build is that the admin creating the pull of skills and categories that users get to choose from, it will make no sance if any user will be able to add to the system any skill he wants, I want to add a feature that users can leave request to add a specific skill if he was not able to find it on the platform.
- Currency System: To maintain fairness, one should teach to learn. Imagine teaching someone Python but not gaining knowledge in return. In such scenarios, users could earn a point for their teaching efforts and redeem it with another user for desired lessons.
- Direct Messaging: Introduce a DM feature, enabling users to communicate directly upon finding a match.
- Rating System: Implement an option for users to rate their peers after a lesson, enhancing credibility.
- Advanced Filtering: Enhance the search logic by adding filters, such as searching for users with expertise in specific fields, for example only experts user in Python or those with a particular rating.

### Feedback Welcome!
If you have suggestions on how to enhance the platform, or ideas for new features that could benefit Skillucket, I'd love to hear from you. Your feedback is invaluable in shaping the future direction of the project, ensuring it remains relevant and user-centric.
My Linkedin profile: https://www.linkedin.com/in/sapir-shamai-75b45125b/
