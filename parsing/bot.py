from Parser import c
from Parser_eth import c_eth
from Parser_band import c_band
from Parser_bch import c_bch
from Parser_doge import c_doge
from Parser_knc import c_knc
from Parser_link import c_link
from Parser_ltc import c_ltc
from Parser_mana import c_mana
from Parser_sushi import c_sushi
from Parser_xrp import c_xrp
from Parser_bnb import c_bnb
from Parser_sol import c_sol
from Parser_ada import c_ada
from Parser_shib import c_shib
from Parser_usdt import c_usdt
from Parser_usdc import c_usdc
from Parser_lunat import c_lunat
from Parser_avax import c_avax
from Parser_busd import c_busd
from Parser_pdotn import c_pdotn
from Parser_ust import c_ust
from Parser_matic import c_matic
from Parser_cro import c_cro
from Parser_wbtc import c_wbtc
from Parser_ton import c_ton
from stocks.america.Parser_alphabet_a import c_alphabet_a
from stocks.america.Parser_alphabet_c import c_alphabet_c
from stocks.america.Parser_amazon import c_amazon
from stocks.america.Parser_AMD import c_AMD
from stocks.america.Parser_apple import c_apple
from stocks.america.Parser_berkshire import c_berkshire
from stocks.america.Parser_block import c_block
from stocks.america.Parser_BoA import c_BoA
from stocks.america.Parser_boeing import c_boeing
from stocks.america.Parser_booking import c_booking
from stocks.america.Parser_chevron import c_chevron
from stocks.america.Parser_citi import c_citi
from stocks.america.Parser_exxon import c_exxon
from stocks.america.Parser_intel import c_intel
from stocks.america.Parser_jpm import c_jpm
from stocks.america.Parser_meta import c_meta
from stocks.america.Parser_micron import c_micron
from stocks.america.Parser_microsoft import c_microsoft
from stocks.america.Parser_netflix import c_netflix
from stocks.america.Parser_nvidia import c_nvidia
from stocks.america.Parser_occidental import c_occidental
from stocks.america.Parser_paypal import c_paypal
from stocks.america.Parser_shopify import c_shopify
from stocks.america.Parser_tesla import c_tesla
from stocks.america.Parser_visaa import c_visaa
from stocks.america.Parser_waltd import c_waltd
from stocks.america.Parser_wellf import c_wellf
from stocks.america.Parser_alibaba import c_alibaba
from stocks.russia.Parser_aeroflot import c_aeroflot
from stocks.russia.Parser_akal import c_akal
from stocks.russia.Parser_fsk import c_fsk
from stocks.russia.Parser_gaz import c_gaz
from stocks.russia.Parser_lukoil import c_lukoil
from stocks.russia.Parser_mmk import c_mmk
from stocks.russia.Parser_mosbirz import c_mosbirz
from stocks.russia.Parser_mts import c_mts
from stocks.russia.Parser_nlmk import c_nlmk
from stocks.russia.Parser_nornik import c_nornik
from stocks.russia.Parser_okr import c_okr
from stocks.russia.Parser_polus import c_polus
from stocks.russia.Parser_poly import c_poly
from stocks.russia.Parser_rosneft import c_rosneft
from stocks.russia.Parser_rostel import c_rostel
from stocks.russia.Parser_sber import c_sber
from stocks.russia.Parser_sber_priv import c_sber_priv
from stocks.russia.Parser_severstal import c_severstal
from stocks.russia.Parser_surgut import c_surgut
from stocks.russia.Parser_surgut_priv import c_surgut_priv
from stocks.russia.Parser_system import c_system
from stocks.russia.Parser_tatn import c_tatn
from stocks.russia.Parser_tatn_priv import c_tatn_priv
from stocks.russia.Parser_vtb import c_vtb
from stocks.russia.Parser_tcs import c_tcs
from stocks.russia.Parser_yandex import c_yandex
from stocks.russia.Parser_fix import c_fix
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import os
import telegram_send
from pprint import pprint
import config

global all



bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)




@dp.message_handler(commands='start')
async def start(message: types.Message):
        start_buttons = ['Крипто','Акции','Сырьевые товары','Индексы']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*start_buttons)

        await message.answer('Выберете категорию', reply_markup=keyboard)

@dp.message_handler(content_types = ["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact"])
async def get_audio(message):
    await dp.bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)

@dp.message_handler(Text(equals='Крипто'))
async def get_c(message: types.Message):
        all = c + '\n' + c_eth + '\n' + c_ton + '\n' + c_cro + '\n' + c_band + '\n' + c_ada + '\n' + c_avax + '\n' + c_bch + '\n' + c_bnb + '\n' + c_busd + '\n' + c_doge + '\n' + c_knc  + '\n' + c_link + '\n' + c_ltc + '\n' + c_lunat + '\n' + c_mana + '\n' + c_shib + '\n' + c_sol + '\n' + c_sushi + '\n' + c_matic + '\n' + c_ust + '\n' + c_usdc + '\n' + c_usdt + '\n' + c_wbtc + '\n' + c_xrp + '\n' + c_pdotn
        await message.answer(all)

@dp.message_handler(Text(equals='Акции'))
async def get_a(message: types.Message):
        get_a_buttons = ['↖','Россия','Америка','Китай','Англия','Германия']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*get_a_buttons)

        await message.answer('Выберете страну', reply_markup=keyboard)

@dp.message_handler(Text(equals='↖'))
async def get_exit(message: types.Message):
        get_exit_buttons = ['Крипто','Акции','Сырьевые товары','Индексы']
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*get_exit_buttons)

        await message.answer('Вы снова в главном меню', reply_markup=keyboard)

@dp.message_handler(Text(equals='Америка'))
async def get_america(message: types.Message):
        all = c_alibaba + '\n' + c_alphabet_a + '\n' + c_alphabet_c + '\n' + c_amazon + '\n' + c_AMD + '\n' + c_apple + '\n' + c_berkshire + '\n' + c_block + '\n' + c_BoA + '\n' + c_boeing + '\n' + c_booking + '\n' + c_chevron + '\n' + c_citi + '\n' + c_exxon + '\n' + c_intel + '\n' + c_jpm + '\n' + c_meta + '\n' + c_micron + '\n' + c_microsoft + '\n' + c_netflix + '\n' + c_nvidia + '\n' + c_occidental + '\n' + c_paypal + '\n' + c_shopify + '\n' + c_tesla + '\n' + c_visaa + '\n' + c_waltd + '\n' + c_wellf
        await message.answer(all)

@dp.message_handler(Text(equals='Россия'))
async def get_america(message: types.Message):
        all = c_aeroflot + '\n' + c_akal + '\n' + c_fsk + '\n' + c_gaz + '\n' + c_lukoil + '\n' + c_mmk + '\n' + c_mosbirz + '\n' + c_mts + '\n' + c_nlmk + '\n' + c_nornik + '\n' + c_okr + '\n' + c_polus + '\n' + c_poly + '\n' + c_rosneft + '\n' + c_rostel + '\n' + c_sber + '\n' + c_sber_priv + '\n' + c_severstal + '\n' + c_surgut + '\n' + c_surgut_priv + '\n' + c_system + '\n' + c_tatn + '\n' + c_tatn_priv + '\n' + c_vtb + '\n' + c_yandex + '\n' + c_tcs + '\n' + c_fix
        await message.answer(all)

def main():
        executor.start_polling(dp)

if __name__ == '__main__':
        main()


