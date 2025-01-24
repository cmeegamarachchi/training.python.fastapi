# Fast API based api

### To start
Install the dependencies  
```bash
cd api
pip install -r requirements.txt
``` 

Start api  
```bash
cd api
uvicorn api:app --reload
```

Serve api from container  
```bash
sudo docker compose up --build
```
