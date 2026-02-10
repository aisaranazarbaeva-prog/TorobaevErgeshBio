from django.shortcuts import render
from .models import Bio

def home(request):
    bio = Bio.objects.first()

    if not bio:
        return render(request, "home.html", {"bio": None})

    items = bio.items.all()

    texts = []
    photos = []
    videos = []

    for item in items:
        if item.item_type == "text":
            texts.append(item)

        elif item.item_type == "photo":
            photos.append(item)

        elif item.item_type == "video" and item.youtube_url:
            url = item.youtube_url.strip()
            video_id = None

            if "watch?v=" in url:
                video_id = url.split("watch?v=")[1].split("&")[0]
            elif "youtu.be/" in url:
                video_id = url.split("youtu.be/")[1].split("?")[0]

            if video_id:
                item.youtube_embed_url = f"https://www.youtube.com/embed/{video_id}"
                videos.append(item)

    # HERO PHOTO (биринчи сүрөт)
    hero_photo = photos[0] if photos else None

    # Тексттер: 1,2,3
    text1 = texts[0] if len(texts) > 0 else None
    text2 = texts[1] if len(texts) > 1 else None
    text3 = texts[2] if len(texts) > 2 else None

    achievement_texts = [
        "1971 жана 1979-жылдары Кыргыз ССРинин Жогорку Кеңешинин Ардак Грамотасы менен сыйланган.",
        "1980-жылы Кыргыз ССРинин эмгек сиңирген энергетиги наамы берилген.",
        "1987-жылы СССРдин энергетикасынын отличниги.",
        "1995-жылы Кыргыз Республикасынын Ардак грамотасы.",
        "1995-жылы Манас-1000 эстелик медалы.",
        "1997-жылы Жалал-Абад шаарынын ардактуу атуулу.",
        "1998-жылы Манас ордени (III даража).",
        "2001-жылы Сузак районунун ардактуу атуулу.",
        "2001-жылы ЖАМУнун ардактуу профессору.",
        "2002-жылы КМШнын эмгек сиңирген энергетиги.",
        "2002-жылы Ош-3000 медалы.",
        "2004-жылы II класстагы мамлекеттик кеңешчи.",
        "2006-жылы КМШнын Ардак грамотасы.",
        "2007-жылы Петр I ордени.",
        "2012-жылы көмөк чордонго аты берилген.",
        "2025-жылы Жалал-Абад облусунун ардактуу атуулу."
    ]

    achievements = [{"text": a} for a in achievement_texts]

    return render(request, "home.html", {
        "bio": bio,
        "hero_photo": hero_photo,
        "texts": [text1, text2, text3],
        "photos": photos,
        "videos": videos,
        "achievements": achievements
    })
