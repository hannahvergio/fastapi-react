FRONTEND github link: https://github.com/hannahvergio/react-fastapi
BACKEND github link: https://github.com/hannahvergio/fastapi-react

FRONTEND live link: https://hannahvergio.github.io/react-fastapi/
BACKEND live link: https://fastapi-react-69wq.onrender.com/ https://fastapi-react-69wq.onrender.com/tasks/

SETUP INSTRUCTIONS:

1. Created a virtual environment: python -m venv venv & activate: source venv/bin/activate
2. Install the dependencies: pip install -r requirements.txt.
3. Deploy on Render (FastAPI) and input the uvicorn & database_url from PostgreSQL.
4. To integrate with React, I changed the fetch to the render live link of fastapi, changed the base in vite.config.js, and etc. 
5. Redeployed it in the github pages.

api endpoints:
[{"text":"kuan","completed":false,"id":2},
{"text":"test-edited","completed":true,"id":1},
{"text":"hahay","completed":false,"id":3}]

GET request/response:
    - request
        "kuan" added task
        "test-edited"
        "hahay"

     - response

                [
        {
            "text": "kuan",
            "completed": false,
            "id": 2
        },
        {
            "text": "test-edited",
            "completed": true,
            "id": 1
        },
        {
            "text": "hahay",
            "completed": false,
            "id": 3
        }
        ]


POST request/response: 
    - request  

        {
        "text": "string",
        "completed": false
        }  

    - response

        {   
        "text": "string",
        "completed": false,
        "id": 4
        }

PUT request/response: 
    - request    
        {
        "text": "1",
        "completed": false
        }

    - response:
    {
    "text": "string",
    "completed": false,
    "id": 1
    }


DELETE request/response:

    -requested: 
        deleted '1'

   - response:
        {
        "message": "Task deleted"
        }

