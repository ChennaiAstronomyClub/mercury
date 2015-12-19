# Mercury
### Check for ISS passes and post to your Facebook page.

Mercury is named after the Roman god of messages/communication.

Have you ever forgotten to ping your club members when there is an ISS pass over your city?
Mercury will help you from now on.

#### Requirements

1. facebook-sdk
2. feedparser
3. Access to a server that allows cron jobs.

#### Usage

1. Modify the [feed source](https://github.com/ChennaiAstronomyClub/mercury/blob/master/mercury/chennai.py#L11)
   to your city. You can find it at [this website](http://spotthestation.nasa.gov/). Click on Location lookup,
   enter the details and click on the RSS button to get the feed.
2. Set up a cron job to run this script periodically. Once in a day would be a good choice.
   Do this in the terminal:
   1. `crontab -e`
   2. `0 10 * * * python mercury/mercury/chennai.py` -> this runs the script at 10 AM everyday(change the city as per your needs).
3. You need to specify an access token to post to the page. To do so,
   1. Create a file named access_token in the mercury directory. Do not give it a file extension.
   2. Create a new app on Facebook and generate a long lived access token. Refer [this](http://stackoverflow.com/questions/12168452/long-lasting-fb-access-token-for-server-to-pull-fb-page-info)
   3. Enter the access token obtained in the file that you created in step 3.1

#### License

MIT © [Chennai Astronomy Club](http://chennaiastronomyclub.org)