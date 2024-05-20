from .models import Project, Task
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
def index(request):  # Sirve para probar el cliente
    title = "Django Course !!"
    return render(request, 'index.html', {
        'title' : title
    })

def hello(request, username):
    print("",username)
    return HttpResponse("<h1>Hola Rataaaa!!! %s <h1/>" %username)

def about(request):
    username = "Bhalu"
    return render(request, 'about.html',{
        'username' : username
    })

def helloRat(request):
    return HttpResponse("<h2> Sucia Rata <h2>")

def MilagrosSanta(request, id):
    result = id + 100 * 2
    return render(request, 'milagros.html')

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.values()
  #  return JsonResponse(projects, safe = False)
    return render(request, 'projects/project.html',{"projects":
        projects})

def tasks(request): #, id):
#    task = get_object_or_404(Task, id = id)
#    return HttpResponse("Task: %s" %task.title)
    tasks = Task.objects.all()
    return render(request, 'tasks/task.html',{
        'tasks' : tasks
    })
    
def create_task(request):
   # print(request.GET["title"])
   # print(request.GET["description
    if request.method=='GET' :
       
        return render(request, 'tasks/create_task.html', { 'form' : CreateNewTask()})
    else:
        Task.objects.create(title=request.POST['title'], description = request.POST['description'], project_id = 2)
        return redirect("tasks")
        
def create_project(request):
    if request.method == 'GET':
        return render (request, "projects/create_project.html", {
        'form': CreateNewProject()
    } )
    else:
       
        Project.objects.create(name = request.POST["name"])
        return redirect("projects")
    
def project_detail(request, id):
   # print(id)
    #project= Project.objects.get(id=id)
    project = get_object_or_404(Project, id= id)
    task = Task.objects.filter(project_id = id)
    print(project)
    return render(request, "projects/detail.html", {
        "project": project,
        "tasks":task
    })