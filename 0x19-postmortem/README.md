# Mock Postmortem

## Issue Summary

From Wednesday, May 11, 2023, 10:15 AM to 12 PM the Apache GET request received a failure of 500. So the mistake was related to PHP or MySQL.

## Timeline

On May 11, 2023, 10:00 AM: The DevOps Junior engineer updated the web server.

At 11–05–2023, 10:15 AM, beginning of the program.

At 11–05–2023, 10:40 AM, find the neglect which is a riddle mistake.

At 11–05–2023, 10:43 AM, reform laziness manually and while correcting using and nauseating statute 200.

At 11–05–2023, 10:50 AM, creating a 0-strace_is_your_friend.pp file to rearrange the mistake and containing Puppet rules.

At 11–05–2023, 11:55 AM, First post to GitHub, however there was a red mark.

At 11–05–2023, 11:57 AM, sentence all problems and submission completed to GitHub.

## Root cause and resolution

The problem was the DevOps Junior engineer didn't know that The “/var/www/html/wp-settings.php” file was missing the religious education characters. The missing tangent is “require_once(ABSPATH.WPINC.’/Class-wp-locale.phpp’);”. , 
then the location of the classifier “class-wp-locale.phpp” would be .php instead of .phpp.

## Corrective and preventative measures  

To avoid this type of error it is recommended to change the permissions of the /var/www/html/wp-settings.php to only be handled by the DevOps Senior engineer and do not let the Junior engineers make the deploy of the project.

To address this king of issues you can follow the below steps.

-   Check the server is up, so use a request to it. Example: curl -sI 127.0.0.1
    
-   Check all the processes involved are up
    
-   Debug the web server process when a request arrives
    
-   Read each message displayed.
    
-   Solve the problem.
