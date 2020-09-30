from django import forms
import requests

class SearchCharacterForm(forms.Form):
    char_name = forms.CharField(max_length=100, required=True)

    def search(self):
        result = {}
        char_name = self.cleaned_data['char_name']

        endpoint = 'https://gateway.marvel.com:443/v1/public/characters?apikey=9c034c15eff31760f9f9b9a34d7bf3e3&hash=2a139a7bce9a6d813ac34a0107beff33&ts=1601415510&nameStartsWith={char_name}'        
        url = endpoint.format(char_name=char_name)

        response = requests.get(url)
        if response.status_code == 200:  # SUCCESS
            result = response.json()
            if result['data']['total'] > 0:
                result['success'] = True
            else:
                result['success'] = False
                result['message'] = f'No entry found for {char_name}'

        else:
            result['success'] = False
            if response.status_code == 404:  # NOT FOUND
                result['message'] = f'No entry found for {char_name}'
            else:
                result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        return result