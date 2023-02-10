# THINGS TO DO

. final product:
INPUT = https://www.youtube.com/watch?v=aEFXUylhQZQ
OUTPUT = https://bit.ly/3aPlZIv (bitly)
. examples from: bitly, rebrandly, tinyurl and short.io

## User Area

. login and password vefirication
. user dashboard:
. statistics
. customization only for registered users
. customize both before and after / from urls
. input field

### Home page (rebrandly + short.io)

. simple introduction to app together with input field for fast link shortening
. if user is already logged in, homepage displays link to dashboard and enables link branding
and customization, if unlocked
. login and sing up links
. why use this app area (bitly)
. FAQ: how to do this and that, how it works, about brand, analytics
. Links to receive help, features page

### Dashboard

. displays created links
. analitics on links
. create more links and customization

## Admin Area

. password and login verification
. logout
. mainly separated in users and links pages
. information about urls: date created and last used, redirects to and shortened url
. information about users: links, last login, accType, etc
. history of links in asc time order
. all urls currently working
. delete old urls

## Database stuff

. admin extends user
. shortLink extends dbObject
. users, admins(?), links, linkData and accType tables
. tables:
. users: username, hashpassword, accTypeId, createdLinksCount(?)
. links: userId, originLink, shortLink
. linkData: linkId, clickCount, createdAt, lastUsedAt
. accType: monthlyPrice, accBenefits
