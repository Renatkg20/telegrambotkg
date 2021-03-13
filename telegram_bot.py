from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import socket
import requests
from config import TOKEN
import os
import re

from bs4 import BeautifulSoup


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def get_url():
  url = "http://bpetroleum.kg"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'class': 'petrol-prices'})
  result  = soup.get_text()
  total = [value for value in result.split('\n') if value != ""]
  total1 = [value.strip() for value in total]
  return f"Bishkek Petrolium\n\n{total1[0]}\n\n{total1[1]} | {total1[2]}\n\n{total1[3]} | {total1[4]}\n\n{total1[5]} | {total1[6]}\n\n {total1[7]} | {total1[8]}\n\n{total1[9]} | {total1[10]} "

res = get_url()

def get_url_rosneft():
  url = "http://www.knp.kg/"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  # soup = soup.find('div', {'class': 'mb50'}).find_all('ul', {'class': 'retailPrice'})
  soup = soup.find('aside', {'class': 'informer'})
  result  = soup.get_text()
  total = result.split("\n")

  return f"РосНефть Кыргызстан, Розничная стоимость ГСМ\n\nДата: {total[1]}\n\nВид  | Стоимость (сом.л) \n\nАИ92 | {total[4]}\n\nАИ95 | {total[5]}\n\n  ДТ | {total[6]}"

res_ros = get_url_rosneft()

def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
       s.connect((ip, int(port)))
       s.shutdown(2)
       return f"Port {port} is open"
   except:
       return f"Port {port} is close"


port1 = isOpen("92.62.72.167", "10012")

def aki():
  resp = requests.get("http://www.akipress.kg")
  data = resp.text
  soup = BeautifulSoup(data, "html.parser")
  resl = soup.find('div', attrs = {"id": "covid-block"})
  resl2 = soup.find('div', attrs = {"class": "nowr_all_textbig"})
  resl1 = soup.find('div', attrs = {'class': "nowr_all_cnt"})
  return f"{resl2.text} {resl1.text} \n {resl.text.strip()}"

akipress = aki()

def get_url_oc():
  url = "https://oc.kg/"
  res = requests.get(url)
  html_doc = res.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  soup = soup.find('div', {'id': 'online_movies_list'})
  result = soup.get_text()
  res1 = (str(result)).strip()

  return res1

ockg = get_url_oc()

def shutdown(shut_comand):
	pass
	if shut_comand == "/9":
	    return os.system("shutdown -h +5")

def reboot1(reboot_comand1):
	pass
	if reboot_comand1 == "/11":
	    return os.system("reboot")

def reboot1(reboot_comand):
	pass
	if cancel_comand == "/99":
	    return os.system("shutdown -c")

def temp_cpu():
	return os.system("sensors > temp_cpu.txt")

t = temp_cpu()

with open("temp_cpu.txt") as file:
	data = file.read()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"Welcom Ranger! How can I assist you?")

@dp.message_handler(commands=['1'])
async def process_help_command(message: types.Message):
    await message.reply(res)

@dp.message_handler(commands=['2'])
async def process_help_command(message: types.Message):
    await message.reply((res_ros))

@dp.message_handler(commands=['3'])
async def process_help_command(message: types.Message):
    await message.reply((ockg))

@dp.message_handler(commands=['5'])
async def process_help_command(message: types.Message):
    await message.reply((port1))

@dp.message_handler(commands=['6'])
async def process_help_command(message: types.Message):
    await message.reply((akipress))

@dp.message_handler(commands=['9'])
async def process_help_command(message: types.Message):
    await message.reply((shutdown("".join(re.findall("/9", str(message))))))

@dp.message_handler(commands=['11'])
async def process_help_command(message: types.Message):
    await message.reply((reboot1("".join(re.findall("/11", str(message))))))

@dp.message_handler(commands=['99'])
async def process_help_command(message: types.Message):
    await message.reply((cancel_comand("".join(re.findall("/99", str(message))))))


@dp.message_handler(text=['CPU'])
async def text_in_handler(message: types.Message):
    await message.answer(data)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
