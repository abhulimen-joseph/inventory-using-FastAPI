from fastapi import FastAPI

api = FastAPI()

all_todos = [
    {"todo_id":1, "todo_name": "sports", "todo_description": "Go to gym"},
    {"todo_id":2, "todo_name": "Read", "todo_description": "Read 10 pages"},
    {"todo_id":3, "todo_name": "shop", "todo_description": "Go shopping"},
    {"todo_id":4, "todo_name": "Study", "todo_description": "Study for exam"},
    {"todo_id":5, "todo_name": "Meditate", "todo_description": "Meditate for 10 mins"},

]
# the end points
@api.get("/")
def index():
    return {"message": "Hello world !"}

# for all todo's
@api.get("/todos")
def get_todos(first_n: int = None): 
    if first_n:
        return all_todos[:first_n]
    else:
        return all_todos
    
# specify the todo
@api.get("/todos/{todo_id}")
def get_todo(todo_id: int): 
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return {"result": todo}

# create a new todo
@api.post("/todos")
def create_todo(todo : dict):
    new_todo = max(todo["todo_id"] for todo in all_todos) + 1  
    new_todo_list = {
        "todo_id": new_todo,
        "todo_name": todo["todo_name"],
        "todo_description": todo["todo_description"]
 
    }
    all_todos.append(new_todo_list)
    return all_todos

# update an already existing todo
@api.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_task : dict):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            todo["todo_name"] = updated_task["todo_name"]
            todo["todo_description"] = updated_task["todo_description"]
            return todo
    return "Error, task not found"

@api.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo["todo_id"] == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo
    return "Error, todo not found"
    

# i waont to use pydynatic in this code 

