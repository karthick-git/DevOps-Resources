#What is BDD?

BDD is an approach that collaboratively specifies the system's desired behaviour. Each time a piece of behaviour is agreed, we use that specification to "drive" the development of the code that will implement that behaviour.

#What are the three practices of BDD, and in what order do you apply them to a story?

We start by collaboratively discovering the scope of the behaviour required by the story. Once we have agreed on that behaviour, we formulate the specification in business-readable language. Finally, we automate the formulated specification to verify that the system actually behaves as expected.

#How are Cucumber and BDD related?

Cucumber is a tool that understands your documentation and turns it into automated tests.
BDD is a collaborative approach, made up of three practices. BDD practitioners may use Cucumber to automate their documentation.

#What do we mean by “living documentation”
"Living documentation" automatically tells us when the system and the documentation are out of sync. This may be for one of several reasons:
the behaviour specified has not yet been implemented
the implementation contains a defect
the documentation is out of date
BDD is a collaborative activity. Living documentation is a secondary, valuable, output of applying BDD practices.

#What’s the relationship between BDD and agile?
BDD is a collection of practices that build upon agile ways of working, helping teams succeed. For these practices to deliver value, you'll need to be working in an agile way.

#What is it about User Stories that helps a team to do BDD?
User stories were created to be "placeholders for a conversation." They allow us to defer detailed analysis until we're confident that the behaviour they describe actually needs to be developed.

#Why do we call it “Three Amigos” (The sprint planning)?
The goal of a three amigos meeting is to ensure that the team fully understand the scope of the story being discussed. For this to be effective, we need to have at least three different perspectives represented at the meeting.
More than three people might attend a three amigos meeting, because:
some stories are broad enough to require the input of more than three perspectives
more than one representative of each perspective may attend

The whole purpose of the three amigos meeting is to discover things about the story that weren't previously obvious. We should expect to learn new things during a three amigos meeting.

#Who are the three amigos?
The essential three perspectives required are:
customer / business perspective - usually provided by the Product Owner
development perspective - usually provided by a Developer
test perspective - usually provided by a Tester

#Why are questions a valuable output from a discovery session?
We want to discover our areas of ignorance before we start developing the next piece of functionality. If we still have unanswered questions about a piece of functionality, it's unlikely that we're in a position to start working on it.

Before the discovery workshop, the question hadn't been asked. That means it was an unknown unknown - it was something that we were completely unaware of. Now that we have asked the question, it is a known unknown - we are aware that it is an area that we need to learn more about.

Having discovered the question, the team now has a concrete area to investigate, learning more about the problem they're being asked to solve.

#Why are testing skills valuable during discovery?
The test perspective is essential during the discovery process. It allows us to ask difficult "what if " style questions that ensure that we have thought about the story in detail. The team use concrete examples to test their understanding of what they're being asked to deliver, while also testing the product owner's understanding of the functionality they're asking for.

#What is Gherkin?
Gherkin is a simple syntax that allows teams to write business readable, executable specifications. 
Some of the Gherkin keywords are Given, When, and Then, but not all text that uses these words is Gherkin.
Gherkin is understood by a large number of tools, notably Cucumber and Specflow, that effectively turn the specification into automated tests.

#What’s the relationship between a scenario and an example?
During three amigos the team uses concrete examples to ensure that they have a shared understanding of the functionality they're about to develop. Those concrete examples are formulated into Gherkin scenarios.
So, each scenario is an example.
Scenario and Example are both keywords in Gherkin.

#What’s an advantage of using Gherkin to express our examples in BDD?
Gherkin is just one way of expressing examples of how you want your system to behave. The advantage of using this particular format is that you can use Cucumber to test them for you, making them into Living Documentation.

#Keywords
Given is the context for the scenario. We’re putting the system into a specific state, ready for the scenario to unfold.
When is an action. Something that happens to the system that will cause something else to happen: an outcome.
Then is the outcome. It’s the behaviour we expect from the system when this action happens in this context.
Step definitions are Java methods that actually do what's described in each step of a Gherkin scenario.When it tries to run each step of a scenario, Cucumber will search for a step definition that matches. If there's a matching step definition, it will call the method to run it.

#Why should we always make sure that we see a scenario fail before we make it pass?
Behaviour-driven development follows the same process as test-driven development, which is sometimes described as red-green-refactor.

red - write a scenario/test and see it fail
green - make it pass (as simply as possible)
refactor - improve your code, while keeping all the tests/scenarios green
It's surprisingly easy to write scenarios and step definitions that don't do anything. It's the transition from red to green that gives us confidence that the scenario and the implementation actually do what we expect.

If a scenario passes as soon as we write it, that means that either it's not doing what we think it should or the behaviour that it describes has already been implemented. In that case, we're not developing using behaviour-driven development.

## Building a cucumber project

#Points to remember

* mvn clean test from cmd to run the feature files. Maven will now download Cucumber, compile your code and tell Cucumber to run your feature file.
* When we run the feature file which contains steps that are still undefined, we get PendingException() and it wil display the count of undefined scenarios and steps.Cucumber tells us that a step (and by inference the Scenario that contains it) is Pending when the automation code throws a PendingException.
The PendingException is a special type of exception provided by Cucumber to allow the development team to signal that automation for a step is a work in progress. This makes it possible to tell the difference between steps that aren't finished yet and steps that are failing due to a defect in the system.
For example, when we run our tests in a Continuous Integration (CI) environment, we can choose to ignore pending scenarios.
* Pressing Alt+Enter creates import statements
* There is a small bug in InteliJ’s Cucumber integration. Sometimes it doesn’t tell Cucumber where to find step definitions. This is easy to work around. Just edit the run configuration and make sure the Glue field contains the value of your package.
* If a step contains a word with apostrophe, skip that in the step definition file by adding a \ before the apostrophe
* In Cucumber, one of the ways to access the same instance of an object from different step definition methods, is to store it on an instance variable.
* When you need to assert for a specific value coming out of your system in a Then step, you can use an instance variable to store it where it goes into the system (in a Given or When) step. This means you can avoid duplicating the value in multiple places in your code.
* Cucumber Expressions look for a match of the whole step text EXCLUDING the Gherkin keyword (Given/When/Then/And/But). The match is case sensitive and matches whitespace as well.
* Cucumber supports parameter types like int,float,word,string
* Below example is used to demonstrate the usage of optional parameter texts
    @Given("Lucy is located/standing {int} metre(s) from Sean")
    public void lucy_is_metres_from_Sean(Integer distance) {
Any text in a Cucumber Expression that is surrounded by parentheses `()` is considered optional.
Words in a Cucumber Expression that are separated by a slash `/` are considered alternates. There must be no whitespace between the word and the slash.
The above step matches both metre and metres as well as located and standing

Points to remember:
Cucumber Options:
dryRun = true will check if all the steps in feature file have corresponding steps defined. default value is false. If it is true it won't run test cases, it will just check if the corresponding steps are present. Even If step definitions are missing, it won't throw error. just the step mapping won't be displayed in the console. If it is false, it will run the test cases.

monochrome = true will display the console output in readable format by removing the unnecessary characters. Best to have it as true always. even if it false it will still run the test cases properly.

format = pretty, html:test-output, json:json_output/cucumber.json, junit:junit_output/cucumber.xml etc. pretty for displaying the console output neatly and for generating html outputs use the sencond option and for json output file use the third option, for xml output use the fourth option

features = feature file/folder path
glue = path of the package that consists the step definitions

strict = true will fail the execution if there are any pending steps. this is useful if dryrun is false.

Example keyword is applicable for the entire test case. For each row in examples, all the steps of the scenaro outline will be run. Any step can be parameterized and the value can be given directly in the example.

Datatable with list object:
Datatable is applicable for a particular line below which the pipes are present.In case of using data table, no need of parameterizing the fields with angular brackets.The step definition of the particular step should contain the Datatable parameter.The datatable value should be first stored in a List<List<String>> data = variable.raw(); Headers are not given for this approach.
The values can be set like data.get(0).get(0), data.get(0).get(1) etc. This particular method is not preferred. Examples is preferred.

Datatable with map object:
Maps can also be used instead of Datatables. Headers can be used in this case. The step definition of the particular step should contain the Datatable parameter again.
for(Map<String,String> data: variable.asMaps(String.class,String.class)){}
The values can be set like data.get(key)

Tags can be provided for features also. In tags , is like OR operator.Eg: tag1,tag2 and AND operator can be mentioned like tag1 and tag2. NOT is like ~tag. also called ignoring. Can be combined with AND or OR
E.g - OR - "tag1,tag2"
      AND - "tag1","tag2" or "tag1 and tag2"
      NOT - "~tag1"

Hooks - Similar to Before and After method in TestNG. Before contains the setup method and after contains the teardown method. Make sure to import the cucumber before and after instead of Junit annotations.
Before and After will be executed after each and every scenario. -> Before() and After(). These are also called global hooks.
There are special kind of hooks called tagged hooks. --> Before("tag1") and After("tag1"). This hook will be executed only for those scenarios with the tag "tag1". They are similar to BeforeMethod and AfterMethods. These are called local hooks. This is used incase we need to add special precondition for a particular scenario.
Global will be executed before Local normally.We can have more than one global hook or local hook. We can specify the order in which the hooks will be executed by specifying the order like @Before(order=0) etc.

Cucumber with TestNG:
To convert a Junit project to TestNG, just add the TestNG depenedencies in pom.xml. Add a TestRunner class with the available template on the internet and just update the paths. Add a TestNG.xml file and provide the TestRunner class inside it.
Best to execute it as Maven from cmd instead of Running the TestNG xml file.