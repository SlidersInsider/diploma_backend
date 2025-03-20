from fastapi import FastAPI
from db.db import init_db
from routers import files, projects, roles, users, users_projects

app = FastAPI()

init_db()

app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(files.router, prefix="/files", tags=["Files"])
app.include_router(roles.router, prefix="/roles", tags=["Roles"])
app.include_router(users_projects.router, prefix="/rp", tags=["RolesProjects"])