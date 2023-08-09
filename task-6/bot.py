import telebot
import requests
import csv

# creating csv file
with open('movies.csv', 'w') as csvfile:
    fieldnames = ['Title', 'Year', 'Genre', 'IMDB', 'Plot']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
csvfile.close()

# TODO: 1.1 Get your environment variables
bot_id = '6612300877:AAEjf2lpxphEEZHrM7fH7ZyDUEjLaWOEPYY'

bot = telebot.TeleBot(bot_id)


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')


@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')


@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    bot.reply_to(message,
                 '1.0 You can use \"/movie MOVIE_NAME\" command to get the details of a particular movie. For eg: \"/movie Barbie\"\n\n2.0. You can use \"/export\" command to export all the movie data in CSV format.\n\n3.0. You can use \"/stop\" or the command \"/bye\" to stop the bot.')


@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    bot.reply_to(message, 'Getting movie info...')
    # TODO: 1.2 Get movie information from the API
    x = message.text.split()[1:]
    search = "+".join(x)
    your_key = "http://www.omdbapi.com/?t=" + search + "&apikey=4f96c8c4"
    api = requests.get(your_key)
    data = api.json()
    if api.json()['Response'] == 'True':
        title = data['Title']
        year = data['Year']
        genre = data['Genre']
        plot = data['Plot']
        imdb = data['imdbRating']
        photo = data['Poster']

        # TODO: 1.3 Show the movie information in the chat window
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, f"Movie name: {title}\nYear: {year}\nGenre: {genre}\nIMDB Ratings: {imdb}\nPlot: {plot}")

        # TODO: 2.1 Create a CSV file and dump the movie information in it
        with open('movies.csv', 'a', newline="") as file:
            writer2 = csv.DictWriter(file, fieldnames=fieldnames)
            writer2.writerow({'Title': title, 'Year': year, 'Genre': genre, 'IMDB': imdb, 'Plot': plot})
        file.close()
    else:
        bot.send_message(message.chat.id, "Sorry, Couldn't find any movie with that title")


@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    bot.reply_to(message, 'Generating file...')
    # TODO: 2.2 Send downloadable CSV file to telegram chat
    with open('movies.csv', 'rb') as file:
        bot.send_document(message.chat.id, file)
    file.close()


@bot.message_handler(func=lambda message: botRunning)
def default(message):
    bot.reply_to(message, 'I did not understand ' + '\N{confused face}')


bot.infinity_polling()
