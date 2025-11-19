from enum import Enum, auto

from kakao import get_kakao_plus_friend_profiles, get_kakao_plus_friend_posts


class MenuSource(Enum):
    KAKAO_PLUS_FRIEND_PROFILE_IMAGE = auto()
    KAKAO_PLUS_FRIEND_POST = auto()


def get_menu_from_kakao_profile(pf_id: str):
    profile = get_kakao_plus_friend_profiles(pf_id)
    profile_card = filter(lambda x: x.type == 'profile', profile.cards).__next__()
    menu = profile_card.profile.profile_image.url
    return menu


def get_menu_from_kakao_post(pf_id: str) -> str:
    posts = get_kakao_plus_friend_posts(pf_id)
    item = sorted(posts.items, key=lambda x: x.created_at, reverse=True)[0]
    return item.contents[0].v
