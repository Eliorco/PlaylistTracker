<h1>Hi Trackers!</h1>
<h3>Now you can follow and extract your favorite music categories without doing NOTHING!</h3><br>
<article>
<h4>Prerequisites</h4>
- in order to access spotify and db set these key in your envrionment 
<br><code>MUST!<br>
SPOTIFY_CLIENT_ID={get_it_from_spotify_api}<br>
SPOTIFY_CLIENT_SECRET={get_it_from_spotify_api}<br>
<br>NOT MANDATORY<br>
SECRET_KEY=Blablabalbalbalablabla<br>
SQLALCHEMY_DATABASE_URI=sqlite:///{name_your_db}.db
</code>
<br>
- clone repo
<br><code>
clone https://github.com/Eliorco/PlaylistTracker.git
</code><br>
- install python packages
<br><code>
pip install - r requirements.txt</code>
<br>
- set cron job for tracker script
<code>
crontab -e
</code> and add this line <br>
<code>*    15    *    *    * /bin/full/path/of/python3 /path/to/Playlisttracker/track_daily.py</code> => 15:00 PM every day

<h4>Usage</h4>
This service is activated by request, any tool is ok as long you'll send post to:<br>
<code>http://localhost:5000/track/<category><br>
http://localhost:5000/entity/create/<category><br>
http://localhost:5000/entity/remove/<category>
</code><br>
I use curl:
<code>curl -X POST http://localhost:5000/entity/create/dance</code>
<br>
You can perform dry run just add param to uri to indicate the tracker<br>
<code> curl -X POST http://localhost:5000/track/hiphop?dry_run=true</code><br>
<br>
enjoy
</article>
