# codecademy-assignment

### Language used: Python3 + Flask
### Requirements: pip, python3, docker
### Running the assignment
#### 1. Via Docker (Go to the codecademy-assignment directory & docker must be installed): 
    docker build -t codecademy-assignment .
    docker run -p 5000:5000 codecademy-assignment  
#### 2. Directly (Go to the codecademy-assignment directory)
    pip install -r requirements.txt
    python3 app.py


#### Once the application is up and running, 
#### The project will be accessible at: http://127.0.0.1:5000/health  
#### Swagger url for the APIs: http://localhost:5000/apidocs/#/  

