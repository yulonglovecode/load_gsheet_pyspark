# Summary

This is a code snippt to load the google sheet from google drive and convert it to dataframe , manipulate it with pyspark for learning purpose 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip3 install pyspark
pip3 install google-api-python-client
pip3 install virtualenv
pip3 install google-auth google-auth-oauthlib google-auth-httplib2
```

## preparation

1. create a google cloud account https://console.cloud.google.com/ linked to your google drive
2. go to https://console.cloud.google.com/iam-admin/iam?project={your project} followed by service accounts , click on the create service account button .
4. click on the service account you have created , go to keys section , click add keys , then click on create new keys  , choose JSON format
5. move the Crendential keys in the same directory of your code . 
3. enable the google worksheet api https://console.cloud.google.com/apis/api/sheets.googleapis.com/metrics?project=tidal-fusion-391707
4. go back to the googlesheet you have created , click on the share button and place the client_email , which can be found in the json file .

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
