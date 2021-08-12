Feature: contact with the owner

    Feature Description
    As user I want to be contacted by sending a message

Scenario: Sending the correct message
Given open chrome browser on store site
When click on contact us button
And choose subject heading
And write email address
And write order reference
And attach file
And write message
And click send button
Then mail send successfully