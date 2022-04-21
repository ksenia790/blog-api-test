
Blog API (TEST)
=======
# Installing
1 - clone project
<br>
2 - create venv, activate it and install dependencies from requirements.txt
<br>
3 - run server "python manage.py runserver" 

API DOCUMENTATION

# Avalible API methods for blog posts:

GET - /api/posts/ - Retrieve All Published Posts
GET - /api/posts/<slug> - Retrieve Particular Post by it's slug
<br>
POST - /api/posts/create/ - Creating New Post
POST - /api/posts/<slug>/create_comment/ - Creating Comment for a Particular Post(chosen by slug)
<br>
# Avalible API methods for blog comments:

GET - /api/comments/ - Retrieve All Comments
GET - /api/comments/<id>/ - Retrieve Particular Comment by it's id number
<br>	
