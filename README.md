
<h1 align='center'>Blog API (TEST)</h1>
<p> In this project I had implemented a REST API for the blog comment system: </p>
<ul>
  <li>API methods for adding an article;</li>
  <li>methods API for adding a comment to an article;</li>
  <li>API method for adding a comment in response to the first level parent comment;</li>
  <li>API method for getting all comments to the article (with all levels of nesting);</li>
  <li>API method to get all nested comments for the parent comment.</li>
</ul>
<h2 align='center'>Fast start with Docker-compose</h2>
This instractions assume that you have already installed Docker and Docker Compose.
In order to get started be sure to clone this project.

## How to get up and running
Once you've cloned the project navigate to the root directory of the project. Run the following commands from this directory:

1. ` docker-compose up -d `

The docker-compose command will build the images from dockerfile and docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. After the command completes we can now view the status of our stack

2. ` docker-compose ps `

And finally run the web-server:

4. ` docker-compose run web_run `

Follow API DOCUMENTATION below.

<h2 align='center'>Installing</h2>

  <ol>
    <li> clone project; </li>
    <li> create venv, activate it and install dependencies from requirements.txt; </li>
    <li> run server "python manage.py runserver" and follow API DOCUMENTATION below. </li>
  </ol>

<h2 align='center'>API DOCUMENTATION<h2>

## Avalible API methods for blog posts:

**GET** ` /api/posts/ ` - Retrieve All Published Posts
 <br>
**GET** ` /api/posts/<id> ` - Retrieve Particular Post by it's id
<br>
**POST** ` /api/posts/create/ ` - Creating New Post
 <br>
**POST** ` /api/posts/<slug>/create_comment/ ` - Creating Comment for a Particular Post(chosen by slug), or answer on one of parents comment
<br>
  
## Avalible API methods for blog comments:

**GET** ` /api/comments/ ` - Retrieve All Comments
 <br>
**GET** ` /api/comments/<id>/ ` - Retrieve Particular Comment by it's id number
