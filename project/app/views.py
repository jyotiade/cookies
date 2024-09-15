from django.shortcuts import render

# Create your views here.
def set(request):
    data=render(request,'set.html')
    data.set_cookie('name','jyoti',max_age=5*24*60*60,httponly=True,secure=True)  #max_age used to set maximum time for cookies data
    data.set_cookie('age','21',max_age=4*24*60*60,httponly=True,secure=True)   #httponly used to only open it with https
    data.set_cookie('city','bhopal',max_age=3*24*60*60,httponly=True,secure=True)
    return data

def get(request):
    print(request.COOKIES)
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    city=request.COOKIES['city']

    data={
        'name':name, 
        'age':age,
        'city':city
    }
    return render(request,'get.html',data)


def delete(request):
    data=render(request,'delete.html')
    data.delete_cookie('name')
    data.delete_cookie('age')
    data.delete_cookie('city')
    return data



#===========================================session==========================================================

