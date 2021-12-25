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

## Example Use Case

Artists (user input at the start of analyzer): J. Cole, John Mayer, Luke Bryan, Marshmello

![artist_comp_overview](https://user-images.githubusercontent.com/94403609/147392354-8bc1f466-0ea6-4d79-aa18-9231bec73f1b.png)



## Lessons Learned


