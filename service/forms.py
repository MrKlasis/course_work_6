from django import forms

from service.models import Mailing, Client, Massage


class MailingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # получаем пользователя и с целью избежания ошибок, удаляем
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        # фильтруем сообщения и клиентов по пользователю если он не является персоналом
        if not user.is_staff:
            # self.fields['message'].queryset = Message.objects.filter(owner=self.user)
            self.fields['clients'].queryset = Client.objects.filter(author=user)

    # def get_form_kwargs(self, *args, **kwargs):
    #     kwargs = super().get_form_kwargs

    class Meta:
        model = Mailing
        fields = ('name', 'periodic', 'massage', 'start', 'stop', 'clients')


class MassageForm(forms.ModelForm):

    class Meta:
        model = Massage
        fields = ('title', 'text')


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('email', 'name', 'comment')
