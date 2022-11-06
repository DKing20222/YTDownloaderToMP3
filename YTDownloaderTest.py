from YTDownloaderFunctions import FilterName

testName = "defaultAuthor - defaultName"
testAuthor = "defaultAuthor"

#videoName with ()
def RoundBracketTest(testName, testAuthor):
    testName = "defaultAuthor - defaultName()"
    return FilterName(testName, testAuthor)

#videoName with []
def SquareBracketTest(testName, testAuthor):
    testName = "defaultAuthor - defaultName[]"
    return FilterName(testName, testAuthor)

#videoName with ""
def QuoteTest(testName, testAuthor):
    testName = "defaultAuthor - \"defaultName\""
    return FilterName(testName, testAuthor)

#videoName with | content
def LineTest(testName, testAuthor):
    testName = "defaultAuthor - defaultName | something"
    return FilterName(testName, testAuthor)

#videoAuthor with " - Topic"
def AuthorTopicTest(testName, testAuthor):
    testAuthor = "defaultAuthor - Topic"
    return FilterName(testName, testAuthor)

#videoName without author
def NoAuthorTest(testName, testAuthor):
    testName = "defaultName"
    return FilterName(testName, testAuthor)

 
#videoName: name - author
def SwitchedNamesTest(testName, testAuthor):
    testName = "defaultName - defaultAuthor"
    return FilterName(testName, testAuthor)

#main
#TEST 1
if (RoundBracketTest(testName, testAuthor) == testName):
    print("Test 1: PASSED - Deletes (content)")
else:
    print("Test 1: FAILED - " + RoundBracketTest(testName, testAuthor))
#TEST 2
if (SquareBracketTest(testName, testAuthor) == testName):
    print("Test 2: PASSED - Deletes [content]")
else:
    print("Test 2: FAILED - " + SquareBracketTest(testName, testAuthor))
#TEST 3
if (QuoteTest(testName, testAuthor) == testName):
    print("Test 3: PASSED - Deletes all \"")
else:
    print("Test 3: FAILED - " + QuoteTest(testName, testAuthor))
#TEST 4
if (LineTest(testName, testAuthor) == testName):
    print("Test 4: PASSED - Deletes | content")
else:
    print("Test 4: FAILED - " + LineTest(testName, testAuthor))
#TEST 5
if (AuthorTopicTest(testName, testAuthor) == testName):
    print("Test 5: PASSED - Deletes - Topic form Author")
else:
    print("Test 5: FAILED - " + AuthorTopicTest(testName, testAuthor))
#TEST 6
if (NoAuthorTest(testName, testAuthor) == testName):
    print("Test 6: PASSED - Inserts Author correctly")
else:
    print("Test 6: FAILED - " + NoAuthorTest(testName, testAuthor))
#TEST 7
if (SwitchedNamesTest(testName, testAuthor) == testName):
    print("Test 7: PASSED - Switches names correctly")
else:
    print("Test 7: FAILED - " + SwitchedNamesTest(testName, testAuthor))