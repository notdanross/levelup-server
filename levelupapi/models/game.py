from django.db import models

class Game(models.Model):

    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey("Gamer", on_delete=models.DO_NOTHING)

    @property
    def event_count(self):
        return self.__event_count

    @event_count.setter
    def event_count(self, value):
        self.__event_count = value

    @property
    def user_event_count(self):
        return self.__user_event_count

    @user_event_count.setter
    def user_event_count(self, value):
        self.__user_event_count = value