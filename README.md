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

For the initial view of each artist's musical profile, a Plotly radar chart (Fig. 4) was used to depict the comparison between profiles because this visual allows for multivariate data to be plotted relative to the same starting point. One benefit includes the ability to compare each artist's profile holistically or by each separate variable. The chart creates a web-like visual for each artist that can be used to discover similar patterns between each or multiple profiles that might not be as obvious in other forms of visualization.

|![artist_comp_box](https://user-images.githubusercontent.com/94403609/147486013-60cf6d47-9abc-4f3e-8bb5-dc40416c2d79.png)|
|:--:|
|Fig. 5 - Artist Audio Feature Box Plots</b>|

Since it is important to get a few different views of the dataset, the same information used in the Radar chart is now displayed in a small multiples series of box plots (Fig. 5). While the first visual (Fig. 4) is great at consolidating the variables into one concise chart, the box plots split by each feature helps to expand the data to analyze more specific data points. Each subplot has a box plot per artist for the given feature which includes min, max, median, quartiles and any outliers if applicable. In addition, the small multiple layout enables a quick analysis of all artists and features since each subplot is exactly the same (axes, categories, etc...) except for the underlying data.

### Use Case Insights

|![LB_Marshmello_Comp](https://user-images.githubusercontent.com/94403609/147496948-a7ea551e-3134-4a09-81ad-d553168bbfc0.png)|
|:--:|
|Fig. 6 - Luke Bryan & Marshmello Radar Comparison</b>|

When taking a look at this scenario, it was interesting to find that two of the four artists that were chosen are very similar to each other (Luke Bryan and Marshmello), even though their genres do not overlap and are considered entirely different in the music industry. Luke Bryan is known as a top Country artist and Marshmello produces music primarily for EDM & House listeners. However, their musical profile (Fig. 6) is more closely related than expected and shows that within the track features of their Top 10 songs, they both follow the same pattern for creating popular music within their respective domains. 

|## Lessons Learned![LB_Marshmello_Comp_box](https://user-images.githubusercontent.com/94403609/147499337-a2706390-b2ae-40e0-bee9-cf098654dc42.png)|
|:--:|
|Fig. 7 - Luke Bryan & Marshmello Box Comparison</b>|

This finding is further exemplified through the box plots (Fig. 7) as the two artists produce similar medians and quartile ranges in almost every category. Medians are used in this scenario to combat the outliers that exist in a few of the features.

Based on the visualizations, these two artists can be analyzed by their average features for their Top 10 songs as such:

Measurable Values (Mean Value for that Track)

- **Danceability**: Marshmello tends to produce more danceable songs than luke Bryan. This follows closely to each artist's specific genres, Country being less "dancy" than EDM & House music.

- **Energy**: Both artists produce music with high energy, but Luke Bryan tends to be higher in energy which was shocking when compared to Marshmello.

- **Loudness**: Both artists produce music that is considered "loud", which is measured in decibels (dB).
 
- **Valence**: The largest difference between these two artists is this feature. Luke Bryan tends to produce a lot happier and euphoric music than Marshmello.
 
- **Tempo**: Both artists scored closely to each other; which was shocking but not unrealistic since the box plots provided more value in this feature by showing that Luke Bryan also has a wider range of tempos than Marshmello. Therefore, Marshmello is more consistent in tempo than Luke Bryan even though his average is higher.

Predictive Values (Spotify guessing if something exists in the track or not)

- **Speechiness**: Both artists scored below .33, meaning that there is a high probability that their tracks don't ONLY include words, but also can be primarily "non-speech-like" tracks. Marshmello fits well into the category of "non-speech-like" given his genre, but Luke Byan scored lower than expected.

- **Acousticness**: Both artists scored very low, meaning that Spotify is confident that their tracks are not mainly acoustic. After looking at the top songs analyzed, this seems to be accurate.

- **Instrumentalness**: Both artists scored very low, meaning that Spotify is confident that their tracks contain at least some vocals. After looking at the top songs analyzed, this seems to be accurate.

- **Liveness**: Both artists scored very low, meaning that Spotify is confident that their tracks are not performed live (like a recording from a live concert). After looking at the top songs analyzed, this seems to be accurate.

### Libraries Used
- Spotipy
- Numpy
- Pandas
- Spotipy.oauth2
- Plotly
- Plotly.offline
- Plotly.graph_objs
- Plotly.subplots
