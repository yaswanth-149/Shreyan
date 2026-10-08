from django.shortcuts import render

# Create your views here.

def student_data(request):
    students= [
        {
            'name': 'rahul',
            'age': 19,
            'course': 'python',
            'email': 'rahul@example.com'
        },
        {
            'name': 'vinay',
            'age': 23,
            'course': 'machine learning',
            'email': 'vinay@example.com'
        },
        {
            'name': 'priya',
            'age': 21,
            'course': 'web development',
            'email': 'priya@example.com'
        },
    ]

    return render(request, 'students/student_list.html', {
        'students': students
    })
