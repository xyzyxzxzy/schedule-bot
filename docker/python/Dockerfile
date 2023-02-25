FROM python:3.9

WORKDIR /var/www/bot

RUN pip install vkwave
RUN pip install pydantic

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "/var/www/bot/bot.py" ]
