Convert Date and Time to New Timezone
=====================================

A simple command-line utility for converting a date and time to a new 
timezone.

Examples::

    > totz tomorrow 1pm MST
    given  : Saturday 10 December 2016, 1:00pm -07:00 (MST).
    desired: Saturday 10 December 2016, 12:00pm -08:00 (US/Pacific), in a day.

    > totz 1969 July 20 13:32:00 UTC
    given  : Sunday 20 July 1969, 1:32pm +00:00 (UTC).
    desired: Sunday 20 July 1969, 6:32am -07:00 (US/Pacific), 47 years ago.

    > totz --to est today 4pm local
    given  : Friday 9 December 2016, 4:00pm -08:00 (US/Pacific).
    desired: Friday 9 December 2016, 7:00pm -05:00 (EST), in 5 hours.

    > totz -t America/Chicago mon 9am local
    given  : Monday 12 December 2016, 9:00am -08:00 (US/Pacific).
    desired: Monday 12 December 2016, 11:00am -06:00 (America/Chicago), in 2 days.

Use 'tzselect' (a shell command) for help with finding the names of timezones.

Usage::

   mytz [options] [--] <specification>...


Options::

   -t TZ, --to TZ   Convert to specified timezone.

The specification must include a date, a time, and a timezone.

You can specify the date with the following formats:

|   *YYYY-M-D*, ex. 1969-07-20
|   *YYMMDD*, ex. 690720
|   *YY MMM D*, ex. 69 Jul 20
|   *YY MMMM D*, ex. 69 July 20
|   *YYYY MMM D*, ex. 1969 Jul 20
|   *YYYY MMMM D*, ex. 1969 July 20
|   **today**, given literally, this represents today
|   **tomorrow**, given literally, this represents tomorrow
|   *DOW*, ex. Mon, represents the next upcoming Monday (cannot be today)
|

You can specify the time with the following formats:

|   *hA*, ex. 1PM or 1pm
|   *h:mmA*, ex. 1:30PM, 1:30pm
|   *h:mm A*, ex. 1:30 PM, 1:30 pm
|   *h:mm:ssA*, ex. 1:30:00PM, 1:30:00pm
|   *h:mm:ss A*, ex. 1:30:00 PM, 1:30:00 pm
|   *HH:mm*, ex. 13:00
|   *HH:mm:ss*, ex. 13:00:00
|

You can specify the timezone with the following formats:

|   *ZZZ*, ex. MST or US/Central or America/Phoenix
|   *Z*, ex. 0700 or 0700-
|   **local**, given literally, this represents local timezone
|

You can specify the timezone as a negative offset in two ways. One way is to 
place the sign after the offset to avoid the offset from being confused as an 
option. The other way is to terminate the option processing by placing '--' 
before the specification.


Installation
------------

Clone from GitHub with::

    git clone https://github.com/KenKundert/totz.git

Then install with::

    cd totz
    pip install . --user

Requires Python3.4 or later.

| Released: 2017-02-03
| Version: 1.1.6
