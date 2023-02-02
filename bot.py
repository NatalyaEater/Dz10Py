from telegram import *
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler,ConversationHandler,filters
import pimondrian

async def hello (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello  {update.effective_user.first_name} запусти бота через команду /print')

async def question_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привет!Этот модуль, задуманный для создания картин в стиле Пита Мондриана из числовых последовательностей. Укажите кол-во последовательностей от 1 до 10 ")
    return 1

async def user_reply (update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    a= int(update.message.text)
    iterator = pimondrian.pi_generator()
    colors = pimondrian.default_colors()
    my_painting = pimondrian.Painting(a,iterator)
    my_painting.save_png(5, colors, (1000, 1000), "Ваша картина")
    lists = ('Ваша картина.png')  
    picture = lists 
    
    await context.bot.send_photo(update.effective_user.id,photo=open(picture, 'rb'))
    await update.message.reply_text("Твоя картина сгенерирована!")
    return ConversationHandler.END



app = ApplicationBuilder().token("6172418592:AAG6SXMIKVpDLon0WDViA2Q-qiiQM_Gsb-Y").build()
app.add_handler(CommandHandler("start", hello))
app.add_handler(ConversationHandler(entry_points=[CommandHandler("print", question_to_user)],
    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, user_reply)]
    },
    fallbacks=[]
))
print('Hello')
app.run_polling()
