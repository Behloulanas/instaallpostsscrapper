from instaloader import Instaloader, Profile

compress_json=False
download_video_thumbnails=False
L = Instaloader()
PROFILE = "teknikgol"
profile = Profile.from_username(L.context, PROFILE)

posts_sorted_by_likes = profile.get_posts()


for post in posts_sorted_by_likes:
    compress_json=False
    if post.is_video:
        download_video_thumbnails=False
        L.download_post(post, PROFILE)
