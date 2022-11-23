from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        user_field(user, 'nickname', request.data.get('nickname', ''))
        user_field(user, 'user_profile', request.FILES.get('user_profile', ''))
        user.save()
        return user
