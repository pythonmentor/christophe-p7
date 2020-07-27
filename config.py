import os


class Config:
    AVATAR = "ressources/GranpyBot.png "
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-die"
    BOT_CREATOR = "Christophe Dupin"
    BASE_LINE = "Bienvenue sur Grandpybot Application"
    GITHUB = ""
    LINKEDIN = "https://www.linkedin.com/in/christophedupin/"

