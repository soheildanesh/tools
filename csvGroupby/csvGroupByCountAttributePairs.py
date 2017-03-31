
# coding: utf-8

# In[12]:


# prupose of code here is to see how variable our vendor predictions are, baiscally it is a group by vendor_name, final_vendro_pred
import csv



inputFileName = "/home/s.danesh.bahreini/projects/SpendCategorization/invoice_items_MRO_3.8.17.scores.20170308194000.csv"
attributeColName = "VENDOR_NAME"
predictionColName = 'FINAL_VENDOR_PRED'

def groupBy(inputFileName, attributeColName, predictionColName, maxRowsToRead = -1):
    maxRowsToRead = -1 #set to -1 to read whole file
    rowsRead = 0
    attributePredictionsDict = {}

    attributeValueCounts = {} #this is just for observation, to see how many times each vendor occures in the file - ignoring predictions for now


    with open(inputFileName, 'rb') as csvfile:

        #inputCsv = csv.reader(csvfile, delimiter=',', quotechar='"') #read csv rows by index as opposed to column name - maybe useful for headerless csv files
        csvReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in csvReader:
            if(maxRowsToRead < 0 or rowsRead < maxRowsToRead):
                attributeValue = row[attributeColName]

                if(attributeValue not in attributeValueCounts):
                    attributeValueCounts[attributeValue] = 1
                else:
                    attributeValueCounts[attributeValue] += 1



                predictedValue = row[predictionColName]
                #print("attibute = "+ attributeValue + ", predicted value = " +predictedValue)
                rowsRead += 1

                #update the number fof times in the dict where this attributeValue is mapped to this predictedValue
                if attributeValue not in attributePredictionsDict:
                    attributePredictionsDict[attributeValue] = {}
                    attributePredictionsDict[attributeValue][predictedValue] = 0 
                attributePredictionsDict[attributeValue][predictedValue] += 1

            else:
                break



    #todo take out of main execution later on 
    #this is just to see how many times each attribute value occurs
    attributeValueCountsFileName = "/home/s.danesh.bahreini/projects/SpendCategorization/invoice_items_MRO_3.8.17.scores.20170308194000.csv_attributeValueCounts.txt"
    attributeValueCountsFile = open(attributeValueCountsFileName, 'w')
    for attributeValue in attributeValueCounts:
        if(attributeValueCounts[attributeValue] > 1): #print only attribute values seen more than once
            attributeValueCountsFile.write(attributeValue+":"+attributeValueCounts[attributeValue])
    attributeValueCountsFile.close()

    #outputFileName = "/home/s.danesh.bahreini/projects/SpendCategorization/invoice_items_MRO_3.8.17.scores.20170308194000.csv_entropyCalculator.txt"
    outputFileName = inputFileName+"grouped_"+attributeColName+"_by_"+predictionColName+".txt"
    indent = "   "
    outputFile = open(outputFileName, 'w')
    for attributeValue in attributePredictionsDict:
        print("\n\n")
        #get all predicted values for this attribute value and sort them by frequency
        predictedValueCountTuples=[]
        dictOfPredictedValuesAndCountsForThisAttributeValue = attributePredictionsDict[attributeValue]

        #first put them all in an array
        for predictedValue in dictOfPredictedValuesAndCountsForThisAttributeValue:
            count = dictOfPredictedValuesAndCountsForThisAttributeValue[predictedValue] #number of times this prediction value was made for this attribute value
            predictedValueCountTuples.append((predictedValue, count))

        #now sort predicted values by count
        predictedValuesCountsSortedByCount = sorted(predictedValueCountTuples, key=lambda predictedValueCountTuple: predictedValueCountTuple[1], reverse=True)

        outputFile.write(attributeValue+"\n")
        for valueCount in predictedValuesCountsSortedByCount:
            outputFile.write(indent+valueCount[0]+":"+str(valueCount[1])+"\n")




    outputFile.close()
    
    
        

    


# In[13]:

groupBy(inputFileName, attributeColName, predictionColName)


# In[ ]:

if False:

    #outputFileName = "/home/s.danesh.bahreini/projects/SpendCategorization/invoice_items_MRO_3.8.17.scores.20170308194000.csv_entropyCalculator.txt"
    outputFileName = inputFileName+"grouped.txt"
    indent = "   "
    outputFile = open(outputFileName, 'w')
    for attributeValue in attributePredictionsDict:
        print("\n\n")
        #get all predicted values for this attribute value and sort them by frequency
        predictedValueCountTuples=[]
        dictOfPredictedValuesAndCountsForThisAttributeValue = attributePredictionsDict[attributeValue]

        #first put them all in an array
        for predictedValue in dictOfPredictedValuesAndCountsForThisAttributeValue:
            count = dictOfPredictedValuesAndCountsForThisAttributeValue[predictedValue] #number of times this prediction value was made for this attribute value
            predictedValueCountTuples.append((predictedValue, count))

        #now sort predicted values by count
        predictedValuesCountsSortedByCount = sorted(predictedValueCountTuples, key=lambda predictedValueCountTuple: predictedValueCountTuple[1], reverse=True)

        outputFile.write(attributeValue+"\n")
        for valueCount in predictedValuesCountsSortedByCount:
            outputFile.write(indent+valueCount[0]+":"+str(valueCount[1])+"\n")




    outputFile.close()   
    
    
        
        
        
    #outputFile.write(attributeValue+"\n") todo delete
    



# In[ ]:




# In[ ]:



