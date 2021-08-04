import graphene
from graphene_django import DjangoObjectType
from .models import User, Profile

class UserType(DjangoObjectType):
    class Meta:
        model = User

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile


class Query(graphene.ObjectType):
    usertoken = graphene.Field(ProfileType, token=graphene.String(required=True))
    allstaff  = graphene.List(UserType)
    me = graphene.Field(UserType)

    def resolve_usertoken(self,info,token):
        if not token:
            raise Exception('Input all field')
        resToken = Profile.objects.filter(token=token)[0]
        print(resToken)
        return resToken
        
    def resolve_allstaff(self, info):
        return User.objects.filter(staff=True)

    def resolve_me(self, info):
        user = info.context.user
        print(user)
        if user.is_anonymous:
            raise Exception('Not Login')

        return user



class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    user_profile = graphene.Field(ProfileType)

    class Arguments:
        email   = graphene.String(required=True)
        password = graphene.String(required=True)
        surname = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname  = graphene.String()
        dob       = graphene.String()
        localgovernment = graphene.String()
        fingerprintID   = graphene.String()
        photo           = graphene.String()

    
    def mutate(self, info,email,password,surname,firstname,lastname,dob,localgovernment,fingerprintID,photo):
        
        user = User(
            email=email
        )
        user.set_password(password)
        user.save()
        user_item = User.objects.get(id=user.id)
        if not user_item:
            raise GraphQLError('')

        user_profile = Profile.objects.create(
            user=user_item,
            surname=surname,
            firstname=firstname,
            lastname=lastname,
            dob=dob,
            localgovernment=localgovernment,
            fingerprintID=fingerprintID,
            photo=photo
        )
        return CreateUser(user=user,user_profile=user_profile)


# class CreateStaffUser(graphene.Mutation):
#     user = graphene.Field(UserType)
    
#     class Arguments:
#         email   = graphene.String(required=True)
#         password = graphene.String(required=True)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


