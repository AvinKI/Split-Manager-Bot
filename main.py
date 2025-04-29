from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("7585488498:AAHsGC3Vu0mNHS6bDvBYvuZBrsbKukVzz9M").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
