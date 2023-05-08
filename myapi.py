from fastapi import FastAPI

app = FastAPI()

assignment={
    '1':{'course': 'wads','condition':"done"},
    "2":{'course': 'indonesian','condition': "undone"},
    "3":{'course': 'ethical hacking','condition': "done"},
    }

@app.get("/")
def index():
    return {'FastAPI Assignment':'Welcome to Todo App'}

@app.get("/assignment")
def print_assignment():
    return {'assignemnt list':assignment}

@app.get("/status")
def status(condition:str):
    courses = []
    if not condition == "done" and not condition == "undone":
        return "error: fill this using done or undone"
    for data in assignment.values():
        if data['condition'] == condition:
            courses.append(data['course'])
    return {"this the course": courses}
   
@app.post("/new data")
def new_data(course: str, condition: str):
    new_id = str(len(list)+1)
    list[new_id] = {'course': course, 'condition': condition}
    return {"the data already done added"}
 
@app.put("/rename")
def rename(course:str, new_course: str):
    for x in list:
        if list[x]["course"] == course:
            list[x]["course"] = new_course
            return {'assignment list':assignment}
        
@app.delete("/delete")
def delete():
    global list
    list = {}