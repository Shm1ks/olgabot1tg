from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start = InlineKeyboardMarkup(row_width=4,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='ДАВАЙ РАССКАЗЫВАЙ!!!', callback_data='Prestart'),
                                              ]
                                          ])

start2 = InlineKeyboardMarkup(row_width=4,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='РАССКАЖИ ПОДРОБНЕЕ', callback_data='gaid'),
                                              ]
                                          ])

money = InlineKeyboardMarkup(row_width=4,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='1️⃣    20000', callback_data='True')
                                              ],
                                              [
                                                  InlineKeyboardButton(text='2️⃣    35000', callback_data='True'),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='3️⃣    54000', callback_data='True'),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='4️⃣    90000', callback_data='True'),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='  5️⃣    200000', callback_data='True'),
                                              ]
                                          ])

posmoney = InlineKeyboardMarkup(row_width=4,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='Не уверена, что у меня получится', callback_data='posmoney'),
                                              ]
                                          ])

gooda = InlineKeyboardMarkup(row_width=10,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='Ну хорошо, а что будет дальше?', callback_data='gooda'),
                                              ]
                                          ])

vaprosorzapis = InlineKeyboardMarkup(row_width=4,
                                          inline_keyboard=[
                                              [
                                                  InlineKeyboardButton(text='Остались Вопросы', url="https://wa.me/%2B79236533921?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5%21%20%D0%A3%20%D0%BC%D0%B5%D0%BD%D1%8F%20%D0%B5%D1%81%D1%82%D1%8C%20%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B%20%D0%BF%D0%BE%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8E."),
                                              ],
                                              [
                                                  InlineKeyboardButton(text='Записаться на бесплатный урок', url="https://wa.me/%2B79236533921?text=%D0%94%D0%BE%D0%B1%D1%80%D1%8B%D0%B9%20%D0%B4%D0%B5%D0%BD%D1%8C.%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C%D1%81%D1%8F%20%D0%BD%D0%B0%20%D0%BF%D1%80%D0%BE%D0%B1%D0%BD%D1%8B%D0%B9%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D1%8B%D0%B9%20%D1%83%D1%80%D0%BE%D0%BA.")
                                              ]
                                          ])