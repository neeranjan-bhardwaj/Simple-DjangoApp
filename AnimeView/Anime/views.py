from django.db.models import Q
from .models import Anime
from .models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def home(request):
    # Data=User.objects.all().delete()
    return Response("Done")

@api_view(["GET","POST","DELETE"])
def anime(request):
    try:
        Data=request.data
        if(request.method=="GET"):
            Animes=Anime.objects.all().values()
            print(Animes)
            return Response({
                "Anime":Animes
            })
        if(request.method=="POST"):
            if(not Data.get("Anime") or not Data.get("Description") or not Data.get("Img")):
                raise ValueError("Can not find Name or Description or Img url")
            New_Anime=Anime(Name=Data.get("Anime"),description=Data.get("Description"),Img=Data.get("Img"))
            New_Anime.save()
            return Response({
                "Message":New_Anime.id
            })
        if(request.method=="DELETE"):
            if(not Data.get("Id") and not Data.get("Name") ):
                raise ValueError("Can not find Id or name")
            Delete=Anime.objects.filter(id=Data.get("Id")) | Anime.objects.filter(Name=Data.get("Name"))
            print(Delete.delete())
            return Response({
                "Message":"Hello"
            })
        else:
            raise ValueError("Woring Requset")
    except Exception as err:
        print(err)
        return Response ({
            "message":"An err has come",
            "err":str(err)
        })

@api_view(["POST"])
def user_login(request):
    try:
        Data=request.data
        if(not Data.get('Email') or not Data.get('Password')):
            raise ValueError(" Entry Email or Password")
        user=User.objects.filter(Email=Data.get('Email')).first()
        if(not user):
            raise ValueError(" can not find user")
        Id=user.id
        return Response({
            "Message":Id
        })
    except Exception as err:
        print(err)
        return Response({
            "Message":"An err has come",
            "Errer":str(err)
        })

@api_view(["POST"])
def user_sigin (request):
    try:
        Data=request.data
        if(not Data.get('Name') or not Data.get('Password') or not Data.get('Email')):
            raise ValueError('Can not find Name or Password or Email')
        New=User(Name=Data.get('Name'),Password=Data.get('Password'),Email=Data.get('Email'))
        New.save()
        print(User.objects.all().values())
        return Response({"message":New.id})
    except Exception as err:
        print(err)
        return Response({
            "Message":"Error has occer",
            "Exptction":str(err)
        },status=status.HTTP_404_NOT_FOUND)
