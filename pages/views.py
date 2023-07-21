from django.shortcuts import render, HttpResponse

def index(request):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'pages/index.html')

def aboutus(request):
    # name = "John"
    student = {1: "John", 2: "Jane", 3: "Sam", 4: "Harry"}
    results = {1: {"name": "John", "cgpa": [9.2,9.3,9.4,9.5]},
               2: {"name": "Sara", "cgpa": [8.2,9.3,8.4,8.5]},
               3: {"name": "Jane", "cgpa": [9.2,8.9,9.5,9.5]},
               4: {"name": "Chris", "cgpa": [9.1,9.4,9.3,9.5]},
               5: {"name": "Amy", "cgpa": [7.1,8.4,8.3,9.5]},
               }
    context = {
        "name" : "Swati",
        "age" : 20,
        "num1" : 12,
        "num2" : 10,
        "nums" : [1,2,3,4,5,10,20,30],
        "students" : student,
        "result": results
    }
    return render(request, 'pages/about.html', context)
    
