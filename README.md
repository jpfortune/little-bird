#  Little Birds

This project was inspired by the cryptocurrency hype during 2017/2018. I wanted to be able more easily consolidate information from various online platforms such as Twitter and Telegram to determine which coins were being talked about the most. Futhermore, I wanted to determine which coins pump and dump groups were targeting. 

## Getting Started

### Prerequisites
* Python 3.6

* [pipenv](https://pipenv.readthedocs.io/en/latest/)

* [Telegram](https://telegram.org/)
This project utilizes envionment variables for authentication, I use a shell script that I source to export them.

You can get your own set of credentials from here: `https://core.telegram.org/`

Create a file called `telegramcreds.sh` with the following:

```
#!/bin/sh
export TG_PHONE=+1234567890
export TG_API_ID=123456
export TG_API_HASH=your_api_hash_here
export BOT_TOKEN=your_telegram_bot_token
```

Then run `source telegramcreds.sh` in the terminal you wish to run this script in.


### Installing

Clone the repo.
```
git clone https://github.com/jpfortune/littlebirds.git
```

Change the current working directory.
```
cd littlebirds
```

Install dependencies

```
pipenv install
```

### Running
To run, simply execute the following:

```
pipenv run python littlebirds.py
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [TELETHON](https://github.com/LonamiWebs/Telethon) - Used to get a client to Telegram servers.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

