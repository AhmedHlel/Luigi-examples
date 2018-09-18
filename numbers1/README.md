# *jobs*.*py*

### Content
- *jobs*.*py*: A file containing two classes Numbers and Letters

### Description 
In this example, we are interested in showing dependency between two classes using Luigi.
*jobs*.*py* includes two classes: Numbers and Letters.
- Numbers: Randomly generate 5 inetegers between 0 and 9 inclusive qnd print them on Numbers.txt.
- Letters: Read Numbers.txt and for each number print it in letters in Letters.txt. For instance if you read 5, we should find 5:Five

### Tools
- Python
- Luigi

### Execution
1)  If you would like to only run Numbers
- Open your terminal
- Go to folder where you saved *jobs*.*py*
- Run the following command:
       *python jobs*.*py Numbers --local-scheduler*
2) If you would like ot run Letters:
- Open your terminal
- Go to folder where you saved  *jobs*.*py*
- Run the following command:
       *python jobs*.*py Letters --local-scheduler*


PS: Letters will force the execution of Numbers if it was not already executed because the output of Numbers is needed as an input for Letters, i.e the class letters depends on the class numbers.


