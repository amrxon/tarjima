from googletrans import Translator

translator = Translator()
def trans_bot(text):
  try:
    result = translator.translate(text)
    return result.text
  except:
   return "bu sozni tarjima qila olmaymiz"