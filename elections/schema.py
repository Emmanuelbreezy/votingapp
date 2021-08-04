import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from .models import Election,Candidate,Vote
from users.schema import UserType


class ElectionType(DjangoObjectType):
    class Meta:
        model = Election

class CandidateType(DjangoObjectType):
    class Meta:
        model = Candidate

class VoteType(DjangoObjectType):
    class Meta:
        model = Vote


class Query(graphene.ObjectType):
    elections = graphene.List(ElectionType)
    allcandidate = graphene.List(CandidateType)
    candidate = graphene.List(CandidateType, urlextid=graphene.String(required=True))
    vote      = graphene.List(VoteType, id=graphene.Int(required=True))

    def resolve_elections(self,info):
        return Election.objects.all()

    def resolve_allcandidate(self,info):
        return Candidate.objects.all()

    def resolve_candidate(self,info,urlextid):
        election_by = Election.objects.get(url_extid=urlextid)
        candidates = Candidate.objects.filter(election=election_by)
        return candidates

    def resolve_vote(self,info,id):
        
        candidate_obj = Candidate.objects.get(id=id)
        voteslist = Vote.objects.filter(candidate=candidate_obj)
        return voteslist


class CreateElection(graphene.Mutation):
    election = graphene.Field(ElectionType)

    class Arguments:
        election_name = graphene.String()
        cover_img = graphene.String()
        posted_by  = graphene.String()

    def mutate(self, info, election_name, cover_img, posted_by):
        election = Election(election_name=election_name, cover_img=cover_img, posted_by=posted_by)
        election.save()
        return CreateElection(election=election)

class CreateVote(graphene.Mutation):
    user = graphene.Field(UserType)
    candidate = graphene.Field(CandidateType)

    class Arguments:
        candidate_id = graphene.Int(required=True)

    def mutate(self, info, candidate_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Login to Vote')
        candidateobj_ = Candidate.objects.get(id=candidate_id)
        if not candidateobj_:
            raise Exception ('Cant find Candidate with given ID')
        vote_obj = Vote.objects.create(
            user=user,
            candidate=candidateobj_
        )
        return CreateVote(user=user, candidate=candidateobj_)

class Mutation(graphene.ObjectType):
    create_election = CreateElection.Field()
    create_vote     = CreateVote.Field()