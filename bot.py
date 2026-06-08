 # -*- coding: utf-8 -*-
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8853590618:AAHzt9ksSvCjw1goYugyw_T5NHPNs3xXUBM"

CLINIC_INFO = {
    "اوقات": "اوقات العمل:\nكل ايام الاسبوع من الساعة 8 صباحا حتى 8 مساء",
    "خدمات": "خدماتنا:\n- تنظيف الاسنان\n- تبييض الاسنان\n- تركيب التقويم\n- خلع الاسنان\n- حشوات الاسنان\n- زراعة الاسنان",
    "اسعار": "الاسعار:\n- كشف وفحص: 5000 جنيه\n- تنظيف: 15000 جنيه\n- تبييض: 80000 جنيه\n- حشوة: 20000 جنيه\n- خلع: 40000 جنيه",
    "موقع": "موقعنا:\nالخرطوم، السودان",
    "موعد": "لحجز موعد او التواصل:\n0115140206\n0115140266",
    "تواصل": "للتواصل معنا:\n0115140206\n0115140266"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "اهلا بك في عيادة اوراس لطب الاسنان!\n\n"
        "يمكنني مساعدتك في:\n"
        "- اوقات\n"
        "- خدمات\n"
        "- اسعار\n"
        "- موقع\n"
        "- موعد\n"
        "- تواصل\n\n"
        "اكتب اي كلمة من القائمة"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    response = None
    for keyword, reply in CLINIC_INFO.items():
        if keyword in text:
            response = reply
            break
    if not response:
        response = "عذرا، لم افهم سؤالك\nاكتب: اوقات / خدمات / اسعار / موقع / موعد / تواصل"
    await update.message.reply_text(response)

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("البوت يعمل الآن...")
    app.run_polling()

if __name__ == "__main__":
    main() 
