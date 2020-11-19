## Submission
- The solution MUST compile and give proper results for ANY given input.
- The program WILL take lines, one by one, by reading console input.
- The file SampleInput.txt contains an example of input. However, remember that input is NOT file-based but console-based.
- The program must output the result by writing a SINGLE line of text to the console with a comma-separated list of numbers, with no spaces.

## Problem

At **Enodo** we need to take steps to prevent credit fraud. Given a set of transactions, your task is to identify the records that are susceptible to be illicit.
A record is flagged as fraudulent if any of the following conditions apply:

* Two records have the same email address and deal id, but different credit card, regardless of street address.
* Two records have the same Address/City/State/Zip and deal id, but different credit card, regardless of email address.

Remember, all records have manual inputs. Your code must be able to handle the following:

* Email and addresses (including city and state) are case insensitive: user1@test.com is the same as User1@test.COM and 130 S Jefferson St. is the same as 130 S Jefferson St.
* The username portion of an email address can have ignored characters. A "." in an email is flat out ignored, so user1@test.com, and user.1@test.com are the same email address. A "+" in an email means the plus and everything after is ignored, so user@test.com and user+1@test.com are the same email address.
* Street addresses often have abbreviated words. 130 S Jefferson St. and 130 S Jefferson Street are the same address. IL and Illinois are the same state. You can assume that the only abbreviated words to consider are the following:
  *  Street/St.
  *  Road/Rd.
  *  IL/Illinois
  *  CA/California
  *  NY/New York
* Zip code may or may not contain dash "-".

We need this detection code to run quickly. That said, please remember that this system is part of a larger system that can change over time. Your code should reflect that fact.

**Input**

First line will contain a integer N denoting the number of records, followed by N lines with one record per line.
Each record contains the following information separated by commas:
 * Order id (numeric)
 * Deal id (numeric)
 * Email address
 * Street address
 * City
 * State
 * Zip Code
 * Credit Card #

*Example*
```
3
1,1,user1@test.com,130 S Jefferson St.,Chicago,IL,60661,12345678901
2,1,user2@test.com,130 S Jefferson St.,Chicago,IL,60661,10987456321
3,2,user1@test.com,130 S Jefferson St.,Chicago,IL,60661,12345678901
```


**Output**
A single line listing all order ids that can be consider fraudulent

```
1,2
```
