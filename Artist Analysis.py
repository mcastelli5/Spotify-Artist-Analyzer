# Setup Python Environment
import spotipy
import numpy as np
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

import plotly
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px

# Authenticate to Spotify API
cid = '7eead20080ce4ae5bbf680ac4eabdb37'
secret = 'a398963a75654f02bd60459ecfe409bf'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# Create input loop to collect all applicable artists that user would like to analyze
artist_list = []
while True:
    ## Get user input and validate it's applicable
    query = input("What artist would you like to analyze? To exit search and see results please input 'EXIT'.")
    if query.upper() == 'EXIT':
        break;
    else:
        result = sp.search(q=query, type='artist')
        artists = result['artists']['items']
        if len(artists) == 0:
            response = input("Search returned no results, please try again!")
            continue;
        else:
            selection = input(f"Did you mean: {artists[0]['name']}? Yes or No.")
            while selection.upper() not in ['YES', 'NO']:
                selection = input(f"Did you mean: {artists[0]['name']}? Yes or No.")

            if (selection.upper() == 'YES'):
                artist_list.append(artists[0]['name'])
            else:
                continue;

# Get results and unpack query response
def get_artist_info(artist_list):
    artist_dict = {}
    for i, artist in enumerate(artist_list, start=1):
        artist_results = sp.search(q=artist, type='artist')
        info =  artist_results['artists']['items'][0]
        case = {
            "name": info['name'],
            "followers": info['followers']['total'],
            "genres": info['genres'],
            "id": info['id'],
            "popularity": info['popularity'],
            "type": info['type']
        }
        artist_dict[f"artist_{i}"] = case

    return artist_dict


artist_dict = get_artist_info(artist_list)

# Summarize selected artists
def print_artist_info(artist_dict):
    for i, artist in enumerate(artist_dict.keys()):
        print(
            artist,
            "\nName: ", artist_dict[artist]['name'],
            "\nFollowers: ", artist_dict[artist]['followers'],
            "\nGenre(s): ", artist_dict[artist]['genres'],
            "\nID: ", artist_dict[artist]['id'],
            "\nPopularity: ", artist_dict[artist]['popularity'],
            "\nType: ", artist_dict[artist]['type'],
            "\n"
        )

print_artist_info(artist_dict)

# Get Artist's albums and tracks
def get_artist_albums(artist_dict):
    for artist in artist_dict.keys():
        albums_results = sp.artist_albums(artist_dict[artist]['id'], limit=50, country='US')
        albums = albums_results['items']
        album_list = [album['name'] for album in albums if len(sp.album_tracks(album['id'])['items']) > 1]
        album_list = [album for album in album_list if ("Explicit Deluxe" not in album) and ("Int'l Version" not in album)]
        album_list = list(dict.fromkeys(album_list))
        artist_dict[artist]['albums'] = album_list
        artist_dict[artist]['album count'] = len(album_list)
    return artist_dict

artist_dict = get_artist_albums(artist_dict)

# Get Artist's top tracks
def get_top_tracks(artist_dict):
    for artist in artist_dict.keys():
        top_tracks_response = sp.artist_top_tracks(artist_dict[artist]['id'])
        top_tracks = top_tracks_response['tracks']
        top_tracks_list = [track['name'] for track in top_tracks]
        top_tracks_id_list = [track['id'] for track in top_tracks]
        artist_dict[artist]['top tracks'] = dict(zip(top_tracks_list, top_tracks_id_list))

    return(artist_dict)

artist_dict = get_top_tracks(artist_dict)

# Create Artist df in pandas
artist_df = pd.DataFrame.from_dict(artist_dict)


# Create tracks_df for track analysis

## Flatten artist and top tracks into a base df to join on 'track id' later
def get_tracks_df(artist_df):
    artist_list = []
    track_list = []
    id_list = []
    for col in artist_df.columns:
        t_list = [track for track in artist_df[col]['top tracks'].keys()]
        track_list = track_list + t_list
        a_list = [artist_df[col]['name'] for i in artist_df[col]['top tracks'].items()]
        artist_list = artist_list + a_list
        i_list = [track for track in artist_df[col]['top tracks'].values()]
        id_list = id_list + i_list

    tracks_df = pd.DataFrame(data={"Artist": artist_list, "Tracks": track_list, "Track ID": id_list})

    return tracks_df

tracks_df = get_tracks_df(artist_df)

## Get track features for analysis
def get_track_features(tracks_df):
    track_list = list(tracks_df['Track ID'])
    danceability = []
    energy = []
    key = []
    loudness = []
    mode = []
    speechiness = []
    acousticness = []
    instrumentalness = []
    liveness = []
    valence = []
    tempo = []
    id = []

    for track in track_list:
        features = sp.audio_features(track)[0]
        danceability.append(features['danceability']),
        energy.append(features['energy']),
        key.append(features['key']),
        loudness.append(features['loudness']),
        mode.append(features['mode']),
        speechiness.append(features['speechiness']),
        acousticness.append(features['acousticness']),
        instrumentalness.append(features['instrumentalness']),
        liveness.append(features['liveness']),
        valence.append(features['valence']),
        tempo.append(features['tempo']),
        id.append(features['id'])

        feature_df = pd.DataFrame(
                        data = {
                                'danceability': danceability,
                                'energy': energy,
                                'key': key,
                                'loudness': loudness,
                                'mode': mode,
                                'speechiness': speechiness,
                                'acousticness': acousticness,
                                'instrumentalness': instrumentalness,
                                'liveness': liveness,
                                'valence': valence,
                                'tempo': tempo,
                                'id': id
                        }
        )

    return feature_df


feature_df = get_track_features(tracks_df)

# Join tracks_df and feature_df in order to analyze track features and compare artist's tracks
tracks_df = tracks_df.merge(feature_df, how='inner', left_on='Track ID', right_on='id')
tracks_df.drop(columns=['id','mode','key'], axis=1, inplace=True)

# Normalize 'tempo' and 'loudness' to be bound between [0,1] similar to the other features
def normalize_data(series):
    norm_list = []
    min = series.min()
    max = series.max()
    for i in series:
        normalized = ((i-min)/(max-min))
        norm_list.append(normalized)

    return norm_list

tracks_df['tempo'] = normalize_data(tracks_df.tempo)
tracks_df['loudness'] = normalize_data(tracks_df.loudness)

display(tracks_df)

# Create avg_tracks_df for artist average song features in top 10 songs
avg_tracks_df = tracks_df.groupby('Artist').mean()
display(avg_tracks_df)

# Plot artist radar chart
def plot_radar_chart(df):
    categories = avg_tracks_df.columns
    fig = go.Figure(
        layout=go.Layout(
            title=go.layout.Title(text='Artist Feature Comparison'),
            polar={'radialaxis': {"showticklabels": False, "showline": False}},
            showlegend=True,
            template='plotly_dark',
            width=700,
            height=575
        )
    )

    for i, artist in enumerate(avg_tracks_df.index):
        name = avg_tracks_df.index[i]
        artist_features = avg_tracks_df.iloc[i]
        fig.add_trace(go.Scatterpolar(r=artist_features, fill='toself', theta=categories, name=name))


    py.iplot(fig)

plot_radar_chart(avg_tracks_df)

# Plot artist box plot
def plot_box_plot(tracks_df):
    categories = avg_tracks_df.columns
    artist_features = tracks_df[tracks_df.Artist == 'J. Cole'].set_index('Artist')[categories]
    fig = go.Figure(
        layout=go.Layout(
            title=go.layout.Title(text='Artist Feature Comparison'),
            showlegend=True,
            template='plotly_dark',
            width=1000,
            height=700
        )
    )

    for i, feature in enumerate(categories):
        fig.add_trace(
            go.Box(
                y=artist_features[feature],
                x=[feature]*10,
                name=artist_features.index[0]
            )
        )

    #fig = px.box(tracks_df, x="day", y=, color=artist_features.index[0], notched=True)





    '''
    for artist in tracks_df.Artist.unique():
        for feature in categories:
            artist_features = tracks_df[tracks_df.Artist == artist].set_index('Artist')[categories]
            fig.add_trace(
                go.Box(
                    x=categories,
                    y=list(artist_features[feature]),
                    boxpoints='all',
                    jitter=0.5,
                    whiskerwidth=0.2,
                    marker_size=2,
                    line_width=1
                )
            )
            print(list(artist_features[feature]))
    '''

    #fig.update_layout(xaxis=dict(title='Audio Features', zeroline=False),boxmode='group')

    #fig.update_traces(orientation='h') # horizontal box plots

    py.iplot(fig)

plot_box_plot(tracks_df)


#tracks_df[tracks_df.Artist == 'J. Cole'].set_index('Artist')[categories]
