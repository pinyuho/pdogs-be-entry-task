# Our Blog

我們ㄉ部落格(後端小作業)

## You will learn
1. git
    - Download project
        ```
        git clone https://nas.pdogs.ntu.im:30443/pdogs/pdogs-6/our-blog.git
        ```
    - Create a new branch
        ```
        git branch my-branch-name
        ```
    - Switch to the new branch
        ```
        git checkout my-branch-name
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

3. Postman
    - Install [postman](https://www.postman.com/downloads/)

3. fastapi framework
    - Run app
        ```
        uvicorn app:app --reload
        ```
    - Call API on postman
        ```
        localhost:8000/hello-world
        ```
    - Call API with parameters
        ```
        localhost:8000/hello-people?name=pdogs
        ```
    
4. BREAD api
    - Browse: return list of objects
    - Read: return single object
    - Edit: edit single object
    - Add: create new object
    - Delete: delete single object

5. SQL
    - refs:
        - https://github.com/encode/databases
        - https://www.postgresqltutorial.com
        - https://stackoverflow.com/questions/65270624/how-to-connect-to-a-sqlite3-db-file-and-fetch-contents-in-fastapi


## Requirements
1. Browse posts
2. Read single post
3. Add post
4. Edit posts
5. Delete posts
6. Comment on posts
