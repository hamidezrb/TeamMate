from .models import Participants

class team:
    def get_teams(request,teams):
        list_team = []
        for team in teams:
            viewMore = False
            if  team.participants_set.count() > 3 :
                viewMore = True
                
            participants = team.participants_set.all()[:3]
            
            participantsNO = Participants.objects.filter(team = team).count()
            remains = team.participantsNO - participantsNO
            list_team.append({ 'participants':participants ,'team_id' : team.id, 'title' : team.title ,'content' :team.content , 'startdate' : team.startdate,
                            'finishdate' : team.finishdate , 'image' :team.image.url , 'createuser_image' : team.user.image.url, 'user_id' : team.user.id,
                            'createdate' : team.createdate.time(), 'participantsNO' : team.participantsNO , 'remains' : remains , 'viewMore' : viewMore, 'owner' : True if request.user.id == team.user.id else False })
        return list_team