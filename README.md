# Spotify-Artist-Analyzer

The objective of this project was to build a flexible, exploratory tool for users to explore any musical artists within the Spotify database. In addition the tool allows for user input to determine the specific artists to analyze. The analysis focuses on a few general aspects of each artist (albums, followers, popularity, etc...), and then dives into the specific type of music the artist produces. To determine the specifics, each artist's Top 10 tracks and the associated track features (listed below) are collected and then aggreagated for visual analysis.

## Track Feature Definitions

The description for each feature from the [Spotify Web API Guidance](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features) can be found below:

**Danceability**: describes the suitability of a track for dancing. This is based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

**Energy**: a measure from 0.0 to 1.0, and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.

**Loudness**: the overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing the relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.

**Speechiness**: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent instrumental music and other non-speech-like tracks.

**Acousticness**: a confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence that the track is acoustic.

**Instrumentalness**: predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.

**Liveness**: detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.

**Valence**: a measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (for example happy, cheerful, euphoric), while tracks with low valence sound more negative (for example sad, depressed, angry).

**Tempo**: the overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece, and derives directly from the average beat duration.

## Use Case

Artists (user input at the start of analyzer): J. Cole, John Mayer, Luke Bryan, Marshmello

|![artist_comp_overview](https://user-images.githubusercontent.com/94403609/147392354-8bc1f466-0ea6-4d79-aa18-9231bec73f1b.png)|
|:--:|
|Fig. 1 - Artist Overview</b>|

Once the user selects the artist's that they would like to analyze, the artist information is collected, organized, cleaned, and displayed in a concise dataframe layout (Fig. 1). This dataframe is a very general overview of each artist juxtaposed with each other to quickly compare and contrast. Several rows hold more than just a value, such as a dictionary (tracks with track id) or a list (albums), which are used for more in-depth analysis in the following steps.

|![artist_track_features](https://user-images.githubusercontent.com/94403609/147415592-ff7051d8-59f1-4a72-afd0-7c3aca3777a5.png)|
|:--:|
|Fig. 2 - Artist Track Level Audio Features</b>|

The next section of analysis focuses on each artist's musical profile, based on Spotify audio features from their Top 10 songs. Every track in the Spotify database includes audio features that describe the track traits, allowing for more precise and granular analytics to be performed. The image above (Fig. 2) depicts the first five rows in the dataframe that is used to determine each artist's musical profile and to easily assess each track in their top 10, on an individual observation level. When collecting the audio features, most feeatues were bound between 0 and 1, except two: Tempo and Loudness. To correctly analyze all the important features and get the entire holistic view, these features were normalized between 0 and 1 by apllying ((x-min)/(max-min)) to each observation.

|![agg_artist_track_features](https://user-images.githubusercontent.com/94403609/147417506-2c2cadff-2fc9-474d-9da4-8bffdb28ac26.png)|
|:--:|
|Fig. 3 - Aggregated Artist Audio Features</b>|

To visualize each artist's musical profile, the Top 10 track's and their features were aggreagated into one average score (Fig. 3). This dataframe layout allows for more efficient visualizations to be created. For this project, the Plotly library was used to display a colorful radar chart and small multiple box plots. Plotly allows users to render highly customizable and interactive visuals with minimal complexity in code when compared to other visualization libraries such as MatplotLib and Seaborn (also great options!).

|![artist_analyzer_rdrchart](https://user-images.githubusercontent.com/94403609/147418003-186ff743-450e-4e4a-81fe-aa3b2c1315ea.png)|
|:--:|
|Fig. 4 - Artist Audio Features Radar Chart</b>|



## Lessons Learned


