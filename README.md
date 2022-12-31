

This Python script is for adding hundreds of rules into Secure Endpoint "Device Control" Configuration.
At this point in time, Secure Endpoint Device Contorl configuration rules basically be added through GUI or API one by one and there's no bulk deployment.

API for Secure Endpint Device Control uses Secure Endpoint API v3 which means it must be integrated into SecureX.
Please find information for preparation for Secure Endpoint API v3 in "Authentication" section. You also can find API reference in "API Refrence" section.
 > https://developer.cisco.com/docs/secure-endpoint/#!introduction

This script is using "Device Control Rules" POST API ( Secure Endpoint API V3 > API Reference > Device Control Rules > POST)


<NOTE>
URI for Secure Endpoint API V3 is varied according to region. This script is using "APJC" region URI, however if you're using different region, please find URI information in "Getting Started" section in above document.
  
<What you need to do before using this API script>
  1. Generate SecureX API Client ID and password.
  2. encode SecureX API Client ID and password to Base64 format (please find more infomation in script. I mentioned this at authentication code).
  3. You must be added Device Control Configuration before using this script. Because this script is just adding rules and not including configuring Device Control Congiguration. For adding new Configuration, go to Secure Endpoint > Management > Device Control and Click "New Configuration" in upper right corner of the page.
 
