# FastAPI, in a nutshell

First part of this talk should be covering why FastAPI may suit your product needs.
- Easy/quick development. Get to market faster. Spend less time messing with boilerplate code.
- It's the fastest Python API framework out there, beating Django/Flask.
- No Postman required! FastAPI is standards-based, with a built-in OpenAPI platform (localhost:8000/docs) you can test your endpoints right away.
- Great documentation (https://fastapi.tiangolo.com/)
- Fast growing community (50K+ stars - 21/Oct/22)
- Simple testing
- What can it do? Type your request payloads, GET/POST/PATCH/DELETE endpoints, Path/Query parameters, ...
- What can't it do? (https://dev.to/fuadrafid/fastapi-the-good-the-bad-and-the-ugly-20ob, https://www.netguru.com/blog/python-flask-versus-fastapi)


## What we'll be covering:
### 1) A quick crash course in: API endpoints, API parameters, Request/Responses. 
### 2) Setup: Python setup (optional), Installing FastAPI
### 3) Creating your first endpoint (GET)
### 4) Testing your first endpoint (localhost:8000/docs)
### 5) Creating an endpoint with API parameters

## A QUICK CRASH COURSE IN THE WORLD OF APIs

### API endpoints types (GET/POST/DELETE/PATCH)

#### GET
We use this endpoint to fetch data

#### POST
We use this endpoint to send complete data

#### DELETE
We use this endpoint to delete data

#### PATCH
We use this endpoint to update data

### API Parameters (Path/Query)

#### Path Parameters
You can think of these parameters as required parameters for the endpoint
e.g.

#### Query Parameters
You can think of this parameter as an optional parameter which we can use to filter payloads.
Some common query parameters are: page/size/sort.

## SETUP: FASTAPI
#### *Disclaimer - Inside this repository you will find simple endpoint examples*
(I am assuming you already have an active Python dev environment w/ at least Python 3.10.6)

- Clone this repository
- Open the cloned repository in VS Code or you preferred IDE.
- Run the setup scripts: setupVirtualEnv (optional, but preferred), setupDependenciesInVenv (or setupDependencies if you opted out from setting up a virtual env)

#### Mac: python3 script-file.py
#### Windows: python script-file.py

What got installed? FastAPI - A Web Framework for quickly creating APIs, Unicorn - a ASGI server

## CREATING YOUR FIRST ENDPOINT

* ⚠️ ATTENTION ⚠️ If you get lost at any point or would like to jump ahead you can view the Resource folder inside the cloned repository. It will have a completed copy of what we're about to in this tutorial.

From your IDE create a file called main.py.

### Running the server
Mac: python3 run.py
Windows: python run.py
## TESTING YOUR FIRST ENDPOINT

Open your web browser and navigate to: localhost:8000/docs. If you created your API correctly you will notice your hello_world_endpoint endpoint.
Now let's test it.

## CREATING AN ENDPOINT WITH API PARAMETERS


