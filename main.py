import instaloader



def getInstaVids():
    # Get the list of videos from the instagram page
    # Return a list of videos

    Loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(Loader.context, "username")
    posts = profile.get_posts()
    videos = []
    for post in posts:
        if post.is_video:
            videos.append(post.video_url)
    return videos