# Blog Backend

## Getting started

1. Download project
   ```
   git clone https://nas.pdogs.ntu.im:30443/pdogs/pdogs-6/backend-entry-task/entry-task-polly.git
   ```
   
2. Conda env
   
   (Open a terminal and run the command lines below.)
   
    - Move to the project directory
      ```
      cd entry-task-polly
      ```
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
3. Run database service
   
   - Install [Docker](https://docs.docker.com/get-docker/) 
   - Run command line below in the same terminal at 2. to start database system
   
   ```
   docker-compose up 
   ```
      
4. Fastapi framework

   (Open another new terminal, and run command line below)
    - Move to the project directory
      ```
      cd entry-task-polly
      ```
    - Activate environment again
      ```
      conda activate my-blog
      ```
    - Run app
        ```
        uvicorn main:app --reload
        ```
    - Now we can call API in browser
        ```
        http://127.0.0.1:8000/docs
        ```
## Descriptions

### Database schema

There are 2 tables in the schema, which is named  `post` and `comment` separately.

| post          | -         |
| ------------- | --------- |
| id            | int       |
| author        | varchar   |
| title         | varchar   |
| content       | text      |
| time          | timestamp |


| comment  | -         |
| -------- | --------- |
| id       | int       |
| post_id  | int       |
| username | varchar   |
| content  | text      |
| time     | timestamp |


## APIs

### Input class
1. class `PostInput`
```
author : string
title  : string
content: string
```

2. class `CommentInput`
```
username: string
content : string
```

### Output Class
1. class `PostOutput`
```
id     : integer
author : string
title  : string
content: string
time_  : datetime
```

2. class `CommentOutput`
```
id      : integer
post_id : integer
username: string
content : string
time_   : datetime
```


### API Functions
1. Browse Post

    - URL: `/post`
    - Method: `GET`
    - Input: None
    - Output: a sequence of output class `PostOutput`
    - Success Response: `HTTP_200_OK`
    - Error Response: None

2. Read Post

    - URL: `/post/{post_id}`
    - Method: `GET`
    - Input: an integer `post_id`
    - Output: an output class `PostOutput`
    - Success Response: `HTTP_200_OK`
    - Error Response: 
        - `HTTP_404_NOT_FOUND` 
        - a message`"Post {post_id} not found"`

3. Add Post

    - URL: `/post`
    - Method: `POST`
    - Input: an input class `PostInput`
    - Output: a message `"Post {post_id} added"`
    - Success Response: `HTTP_201_CREATED`
    - Error Response: None

4. Edit Post

    - URL: `/post/{post_id}`
    - Method: `PATCH`
    - Input: 
        - an integer `post_id` 
        - an input class `PostInput`
    - Output: a message `"Post {post_id} updated"`
    - Success Response: `HTTP_200_OK`
    - Error Response: 
        - `HTTP_404_NOT_FOUND`
        - a message`"Post {post_id} not found"`
    
5. Delete Post

    - URL: `/post/{post_id}`
    - Method: `DELETE`
    - Input: an integer `post_id`
    - Output: a message `"Post {post_id} deleted"`
    - Success Response: `HTTP_204_NO_CONTENT`
    - Error Response: 
        - `HTTP_404_NOT_FOUND`
        - a message`"Post {post_id} not found"`
    
    
6. Add Comment

    - URL: `/post/{post_id}/comment`
    - Method: `POST`
    - Input: 
        - an integer `post_id`
        - an input class `CommentInput`
    - Output: a message `"Comment {comment_id} added"`
    - Success Response: `HTTP_201_CREATED`
    - Error Response: 
        - `HTTP_404_NOT_FOUND`
        - a message`"Post {post_id} not found"`

7. Browse Comment

    - URL: `/post/{post_id}/comment`
    - Method: `GET`
    - Input: an integer `post_id`
    - Output: a sequence of output class `CommentOutput`
    - Success Response: `HTTP_200_OK`
    - Error Response: 
        - `HTTP_404_NOT_FOUND`
        - a message`"Post {post_id} not found"`



