from django.shortcuts import render
from .models import Bio, BioItem

def home(request):
    bio = Bio.objects.first()

    if not bio:
        return render(request, "home.html", {"bio": None})

    items = bio.items.all()

    first_text = None
    hero_photo = None
    remaining_items = []

    for item in items:
        # Находим главное фото
        if item.item_type == 'photo' and not hero_photo:
            hero_photo = item

        # Находим первый текст
        elif item.item_type == 'text' and not first_text:
            first_text = item

        else:
            # Обработка видео (YouTube)
            if item.item_type == 'video' and item.youtube_url:
                url = item.youtube_url.strip()
                video_id = None

                # youtube.com/watch?v=
                if "watch?v=" in url:
                    video_id = url.split("watch?v=")[1].split("&")[0]

                # youtu.be/короткая ссылка
                elif "youtu.be/" in url:
                    video_id = url.split("youtu.be/")[1].split("?")[0]

                # Если видео ID найден, формируем embed
                if video_id:
                    item.youtube_embed_url = f"https://www.youtube.com/embed/{video_id}"
                else:
                    item.youtube_embed_url = None
            else:
                item.youtube_embed_url = None

            remaining_items.append(item)

    # Список достижений
    achievement_texts = [
        "1971 жана 1979-жылдары Кыргыз ССРинин Жогорку Кеңешинин “Ардак Грамотасы” менен сыйланган.",
        "1980-жылы “КЫРГЫЗ ССРинин ЭМГЕК СИҢИРГЕН ЭНЕРГЕТИГИ” наамы берилген.",
        "1987-жылы “СССРдин энергетика жана электрофикациясынын отличниги” деген наам берилген.",
        "1995-жылы Кыргыз Республикасынын “Ардак грамотасы” менен сыйланган.",
        "1995-жылы “Манас-1000” Эстелик медалы менен сыйланган.",
        "1997-жылы “Жалал-Абад шаарынын ардактуу атуулу” наамы ыйгарылган.",
        "1998-жылы Кыргыз Республикасынын “Үчүнчү даражадагы Манас” ордени менен сыйланган.",
        "2001-жылы “Сузак районунун ардактуу атуулу” наамын алган.",
        "2001-жылы ЖАМУнун “Ардактуу профессору” наамы ыйгарылган.",
        "2002-жылы “КМШнын эмгек сиңирген энергетиги” белгиси менен сыйланган.",
        "2002-жылы “Ош-3000” медалы ыйгарылган.",
        "2004-жылы II класстагы Мамлекеттик кеңешчи наамы берилген.",
        "2006-жылы КМШнын Ардак грамотасы.",
        "2007-жылы Петр I ордени.",
        "2012-жылы көмөк чордонго аты берилген.",
        "2025-жылы Жалал-Абад облусунун ардактуу атуулу."
    ]
    achievements = [{"text": a} for a in achievement_texts]

    return render(request, "home.html", {
        "bio": bio,
        "hero_photo": hero_photo,
        "first_text": first_text,
        "remaining_items": remaining_items,
        "achievements": achievements
    })
