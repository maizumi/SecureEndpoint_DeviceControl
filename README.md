

This Python script is for adding hundreds of rules into Secure Endpoint "Device Control" Configuration.
At this point in time, Secure Endpoint Device Contorl configuration rules basically be added through GUI or API one by one and there's no bulk deployment.

API for Secure Endpint Device Control uses Secure Endpoint API v3 which means it must be integrated into SecureX.
Please find information for preparation for Secure Endpoint API v3 in "Authentication" section. You also can find API reference in "API Refrence" section.
 > https://developer.cisco.com/docs/secure-endpoint/#!introduction

This script is using "Device Control Rules" POST API ( Secure Endpoint API V3 > API Reference > Device Control Rules > POST)
<br>

<H3>[NOTE]</H3>
URI for Secure Endpoint API V3 is varied according to region. This script is using "APJC" region URI, however if you're using different region, please find <br>
URI information in "Getting Started" section in above document.
<br>
<br>
<h3>[What you need to do before using this API script]</h3>

  1. Generate SecureX API Client ID and password.<br>
  2. encode SecureX API Client ID and password to Base64 format (please find more infomation in script. I mentioned this at authentication code).<br>
  3. You must be added Device Control Configuration before using this script. Because this script is just adding rules and not including configuring Device Control Congiguration. For adding new Configuration, go to Secure Endpoint > Management > Device Control and Click "New Configuration" in upper right corner of the page.<br>
  4. using sample csv file (named rule.csv), replace information what you'd like to add as device control rules.
 
<h3>[Steps using script]</h3>
  1. replace credentials for authentication (script file line 14)
  <br>
  2. replace csv file path (script file line 73)
  <br>
  3. excute python script and if any of rules got an error, then you see which row in csv.file has unacceptable value
  <br>
