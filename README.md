sample admin login details:
username: admin
password: admin123

Routes Description:
authentication:
  http://localhost:8000/api_auth/login/ for Login 
  http://localhost:8000/api_auth/logout/ for Logout

client routes:
  http://localhost:8000/api/clients/  Post-create client
  http://localhost:8000/api/clients/  Get all clients
  http://localhost:8000/api/clients/:id  Get client by id
  http://localhost:8000/api/clients/:id  Delete client by id
  http://localhost:8000/api/clients/:id  Update client details
  
project routes:
  http://localhost:8000/api/projects/  post create project
  http://localhost:8000/api/projects/  Get all projects
  http://localhost:8000/api/projects/:id  Get project by id
  http://localhost:8000/api/projects/:id  Delete project by id
  http://localhost:8000/api/user/projects/ Get User assigned projects


for all routes we need authentication

for authentication, I used JWT authentication 

Headers:
for authorization:-
  key: Authorization
  value: Bearer <access_Token>
  

