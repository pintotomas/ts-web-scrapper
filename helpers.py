MALE = "hombre"
MALE_SYMBOL = "H"
FEMALE = "mujer"
FEMALE_SYMBOL = "M"

def get_gender(secret_title):
  if MALE in secret_title:
    return MALE_SYMBOL
  elif FEMALE in secret_title:
    return FEMALE_SYMBOL

AGE_START = -7
AGE_END = -5

def get_age(secret_title):
  return secret_title[AGE_START:AGE_END]