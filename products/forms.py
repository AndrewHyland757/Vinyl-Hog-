from django import forms
from .models import Album, Artist, Genre


class ProductForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        artists = Artist.objects.all()
        genres = Genre.objects.all()
        artist_names = [(artist.id, artist.name) for artist in artists]
        genre_names = [(genre.id, genre.name) for genre in genres]

        self.fields["artist"].choices = artist_names
        self.fields["genres"].choices = genre_names

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "checkout-input"


class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "checkout-input"


class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "checkout-input"
