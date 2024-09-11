from django.shortcuts import render

# # Create your views here.
# def set(request):
#     data=render(request,'set.html')
#     data.set_cookie('name','jyoti',max_age=5*24*60*60,httponly=True,secure=True)  #max_age used to set maximum time for cookies data
#     data.set_cookie('age','21',max_age=4*24*60*60,httponly=True,secure=True)   #httponly used to only open it with https
#     data.set_cookie('city','bhopal',max_age=3*24*60*60,httponly=True,secure=True)
#     return data

# def get(request):
#     print(request.COOKIES)
#     name=request.COOKIES['name']
#     age=request.COOKIES['age']
#     city=request.COOKIES['city']

#     data={
#         'name':name, 
#         'age':age,
#         'city':city
#     }
#     return render(request,'get.html',data)


# def delete(request):
#     data=render(request,'delete.html')
#     data.delete_cookie('name')
#     data.delete_cookie('age')
#     data.delete_cookie('city')
#     return data



#===========================================session==========================================================

def set(request):
    my_list1={'id':1,'name':'jyoti','city':'bhopal'}
    my_list2={'id':2,'name':'viti','city':'bhopal'}
    my_list=[my_list1,my_list2]
    request.session['data']=my_list

    return render(request,'set.html')

#minimum time for cookies are closing till browser,and for session is 14 days

def get(request):
    data1=request.session.get('data','Guest')
    return render (request,'get.html',{"name":data1})