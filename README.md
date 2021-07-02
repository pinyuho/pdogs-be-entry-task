# Blog Backend


## Features
1. Browse posts
2. Read single post
3. Add post
4. Edit posts
5. Delete posts
6. Comment on posts
7. Browse comments of a post

## Getting started

1. download project
   ```
   git clone https://nas.pdogs.ntu.im:30443/pdogs/pdogs-6/backend-entry-task/entry-task-polly.git
   ```
   
2. conda env
    - Create a new environment
        ```
        conda create --name my-blog python=3.8
        ```
    - Activate environment
        ```
        conda activate my-blog
        ```
    - Install dependencies
        ```
        pip install -r requirements.txt
        ```
3. run database service
   
   (to run this service, you'll need to have [Docker](https://docs.docker.com/get-docker/) installed.)
   ```
   docker-compose up 
   ```
      
4. fastapi framework
    - run app
        ```
        uvicorn main:app --reload
        ```
    - call API 
        ```
        http://127.0.0.1:8000/docs
        ```






