# from isOdd import isOdd
# a=int(input())
# b=int(input())
# # print(isOdd('1'))
# # print(isOdd('5'))
#
# print(isOdd(a))
# print(isOdd(b))
#
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# # Python is 👍
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# # Python is 👍
# print(emoji.demojize('Python is 👍'))
# # Python is :thumbs_up:
# print(emoji.emojize("Python is fun :red_heart:"))
# # Python is fun ❤
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# # Python is fun ❤️ #red heart, not black heart
# print(emoji.is_emoji("👍"))
# # True

from datetime import date
import datetime

current_date = date.today()
current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
print(current_time)
print(current_date)