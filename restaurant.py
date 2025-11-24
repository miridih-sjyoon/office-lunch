from enum import Enum

from menu import MenuSource, get_menu_from_instagram_feed, get_menu_from_kakao_profile, get_menu_from_kakao_post


class Restaurant(Enum):
    알찬푸드_구내식당 = (MenuSource.INSTAGRAM_FEED, 'your_table__')
    우림_더이룸푸드 = (MenuSource.INSTAGRAM_FEED, 'theirum_food')
    정원정_한식뷔페 = (MenuSource.KAKAO_PLUS_FRIEND_POST, '_Zlxgxhxj')
    한신IT타워_구내식당 = (MenuSource.KAKAO_PLUS_FRIEND_PROFILE_IMAGE, '_QRALxb')

    def __init__(self, menu_source: MenuSource, menu_source_id: str):
        self.menu_source = menu_source
        self.menu_source_id = menu_source_id

    def get_menu(self):
        if self.menu_source == MenuSource.INSTAGRAM_FEED:
            return get_menu_from_instagram_feed(self.menu_source_id)
        elif self.menu_source == MenuSource.KAKAO_PLUS_FRIEND_PROFILE_IMAGE:
            return get_menu_from_kakao_profile(self.menu_source_id)
        elif self.menu_source == MenuSource.KAKAO_PLUS_FRIEND_POST:
            return get_menu_from_kakao_post(self.menu_source_id)
        else:
            raise Exception(f'Unknown menu source {self.menu_source}')
