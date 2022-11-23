from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_field

class CustomAccountAdapter(DefaultAccountAdapter):

    # def save_user(self, request, user, form, commit=False):
    #     user = super().save_user(request, user, form, commit)
    #     data = form.cleaned_data
    #     user.nickname = data.get('nickname')
    #     user.profile = data.get('profile')

    #     user.save()
    #     return user

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, False)
        # user_field(user, 'nickname', request.data.get('nickname', ''))
        # user_field(user, 'user_profile', request.data.get('user_profile', ''))
        user.save()
        return user
