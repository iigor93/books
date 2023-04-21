
from rest_framework import viewsets, generics

from user_profile.models import Profile
from user_profile.serializers import ProfileSerializer


class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    model = Profile
    serializer_class = ProfileSerializer

    def get_object(self):
        user_profile, _ = Profile.objects.get_or_create(pk=1)

        return user_profile
