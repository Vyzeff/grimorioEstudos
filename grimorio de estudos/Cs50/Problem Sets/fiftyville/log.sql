-- Keep a log of any SQL queries you execute as you solve the mystery.
firstly, .schema to get a general grip of the tables
theft: 07/28, Humphrey Street
who did it
where are they
who helped
Tables
airports              crime_scene_reports   people
atm_transactions      flights               phone_calls
bakery_security_logs  interviews
bank_accounts         passengers
schema intervews
frind a crime report from the day in which the theft happened.
  FROM crime_scene_reports
 WHERE month = 7 AND day = 28 AND street = "Humphrey Street";

O roubo do pato aconteceu as 10:15am na padaria da Humphrey Street. Foram 3 entrevistas com testemunhas que
estavam presentes no lugar.

SELECT * FROM interviews WHERE month = 7 AND day  = 28 AND transcript LIKE "%bakery%";

ID    Name               Date
 161 | Ruth    | 2021 | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
 162 | Eugene  | 2021 | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at
Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
 163 | Raymond | 2021 | As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
The thief then asked the person on the other end of the phone to purchase the flight ticket. |
 193 | Emma    | 2021 | I'm the bakery owner, and someone came in, suspiciously whispering into a phone for about half an hour.
They never bought anything.

SELECT * FROM flights WHERE origin_airport_id = 8 AND day = 29;
--Earliest flight out was flight id# 36 - Destination LaGuardia Airport, New York City

SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36);
-pessoas no voo
+--------+
|  name  |
+--------+
| Kenny  |
| Sofia  |
| Taylor |
| Luca   |
| Kelsey |
| Edward |
| Bruce  |
| Doris  |
+--------+

SELECT account_number, transaction_type, amount FROM atm_transactions WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street";
--contas dos suspeitos
| 28500762
| 28296815
| 76054385
| 49610011
| 16153065
| 86363979
| 25506511
| 81061156
| 26013199

SELECT id, caller, receiver, year, duration FROM phone_calls WHERE month = 7 AND day  = 28 AND duration < 60;

+-----+----------------+----------------+------+-----------+
| id  |     caller     |    receiver    | year  | duration |
+-----+----------------+----------------+------+-----------+
| 221 | (130) 555-0289 | (996) 555-8899 | 2021  | 51       |
| 224 | (499) 555-9472 | (892) 555-8872 | 2021  | 36       |
| 233 | (367) 555-5533 | (375) 555-8161 | 2021  | 45       |
| 251 | (499) 555-9472 | (717) 555-1342 | 2021  | 50       |
| 254 | (286) 555-6063 | (676) 555-6554 | 2021  | 43       |
| 255 | (770) 555-1861 | (725) 555-3243 | 2021  | 49       |
| 261 | (031) 555-6622 | (910) 555-3251 | 2021  | 38       |
| 279 | (826) 555-1652 | (066) 555-9701 | 2021  | 55       |
| 281 | (338) 555-6650 | (704) 555-2131 | 2021  | 54       |
+-----+----------------+----------------+-------+----------+

SELECT * FROM bank_accounts WHERE account_number IN (
SELECT account_number FROM atm_transactions WHERE month = 7 AND day  = 28 AND atm_location = "Leggett Street");

+----------------+-----------+---------------+
| account_number | person_id | creation_year |
+----------------+-----------+---------------+
| 49610011       | 686048    | 2010          |
| 86363979       | 948985    | 2010          |
| 26013199       | 514354    | 2012          |
| 16153065       | 458378    | 2012          |
| 28296815       | 395717    | 2014          |
| 25506511       | 396669    | 2014          |
| 28500762       | 467400    | 2014          |
| 76054385       | 449774    | 2015          |
| 81061156       | 438727    | 2018          |
+----------------+-----------+---------------+
--contas para pessoas

SELECT name FROM people WHERE id IN (
SELECT person_id FROM bank_accounts WHERE account_number IN (
SELECT account_number FROM atm_transactions WHERE  day  = 28 AND month = 7 AND atm_location = "Leggett Street"))
AND phone_number IN (SELECT caller FROM phone_calls WHERE day  = 28 AND month = 7 AND duration < 60);
--pessoas que estavam na lista de ligações e atm ao mesmo tempo

+---------+
|  name   |
+---------+
| Kenny   |
| Benista |
| Taylor  |
| Diana   |
| Bruce   |
+---------+

--pessoas que estavam no voo, no atm e nas ligações ao mesmo tempo
SELECT * FROM people WHERE name = "Kenny" OR name = "Taylor" OR name = "Bruce";
+--------+--------+----------------+-----------------+---------------+
|   id   |  name  |  phone_number  | passport_number | license_plate |
+--------+--------+----------------+-----------------+---------------+
| 395717 | Kenny  | (826) 555-1652 | 9878712108      | 30G67EN       |
| 449774 | Taylor | (286) 555-6063 | 1988161715      | 1106N58       |
| 686048 | Bruce  | (367) 555-5533 | 5773159633      | 94KL13X       |
+--------+--------+----------------+-----------------+---------------+

SELECT * FROM bakery_security_logs WHERE license_plate IN (
SELECT license_plate FROM people WHERE name = "Kenny" OR name = "Taylor" OR name = "Bruce")
AND day = 28;
+-----+------+-------+-----+------+--------+----------+---------------+
| id  | year | month | day | hour | minute | activity | license_plate |
+-----+------+-------+-----+------+--------+----------+---------------+
| 232 | 2021 | 7     | 28  | 8    | 23     | entrance | 94KL13X       |
| 237 | 2021 | 7     | 28  | 8    | 34     | entrance | 1106N58       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58       |
+-----+------+-------+-----+------+--------+----------+---------------+
--Tanto Taylor quanto Bruce estavam no voo, fizeram uma ligação curta, dirigiram da padaria e fizeram transações no atm
--MAS o bruce é o unico que saiu do estacionamento num periodo de tempo de 10min

--(375) 555-8161 é quem recebeu uma ligação de Bruce

SELECT * FROM people WHERE phone_number = "(375) 555-8161";
--Robin é o cumplice