## Postman Tricks and Tips

* More than one instance of postman can be created and different workspaces can be easily managed
* Bulk edit option can be used to export/copy large headers from one request to another instead of manually adding headers
* Params tab can be used to add parameters easily as it is in key value table format
* Parameters can be appended with : symbol and it will be added to the params table
* Tests can also be written in Pre-request scripts tab
* Arrow functions can be used to write functions instead of generic funcitons
* ES6 (ECMAScript) provides more features as the tests are written in Javascript
* Chai assertions are used in postman, so any chai assert can be prefixed with pm. to make it a postman compatible assertion
* Use jsonpath.com to practice/verify the correctness of json paths

## auto build a job in jenkins if there is any change in code on Github repository

Go to: Manage Jenkins > Configure System
Under GitHub Plugin Configuration, Click on ‘Advanced' tab. 
Check 'Specify another hook url' for GitHub configuration. 
A textbox will appear with a hook URL. This is the Hook URL at which Jenkins will listen for POST requests. Copy this URL and go to the next step.

Open your repository on GitHub.
Click ‘Settings’ on the navigation bar on the right-hand side of the screen.
Click ‘Webhooks ’ on the navigation bar on the left-hand side of the screen.
Click ‘Add webhook’ to add the webhook. 
Paste the URL you copied in the previous step as the ‘Payload URL’.
You can select the events for which you want the Jenkins build to be triggered. We will select ‘Just the push event’ because we want to run the build when we push our code to the repository.
Click ‘Add webhook’. 

In Jenkins, go to the project configuration of the project for which you want to run an automated build.
In the ‘Build Triggers’ section, select 'Github hook trigger for GITScm Polling'. 

## Importing requests from your browser (Chrome) into Postman

Dev Tools --> Inspect --> Netwoek --> XHR --> Preserve log
Open the application side by side and perform any operation
If you click on the request generated, there will be details of the request present
RC on Request--> Copy as cURL
Go to Postman --> Import--> Import as Raw text--> paste and import
Postman should automatically fill the details and generate a request


## Reuse Postman scripts and tests among different test cases

Write the tests and enclose them inside a fucntion, for example

var commonTests = () => {
pm.test("Is valid response with json array in body", function () {
    
    // assert that the status code is 200
    pm.response.to.be.ok; // info, success, redirection, clientError,  serverError, are other variants
     
    // assert that the response has a valid JSON body
    pm.response.to.be.withBody;
     
    pm.response.to.be.json; // this assertion also checks if a body  exists, so the above check is not needed
     
    //make sure we have a valid json array
    //pm.expect(pm.response.json()).to.be.an('array').but.not.an('object');
    
});

pm.test("Has Content-Type header", function () {
    pm.expect(responseHeaders.hasOwnProperty("Content-Type"));
});

pm.test("Is response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});

}

//Create an environment first and add a variable named "commonTests before executing the below line"
pm.environment.set("commonTests", commonTests.toString());

move everything from tests to pre requisite tab
In tests, use eval function to run the tests, like below
eval(pm.environment.get("commonTests"))();

Just use the above line in all the following scripts. 

//Generating a random value for a field during runtime
We can use the prerequisite scripts or {{$randonInt}} in place of the value for integer values
