# Financial Transaction Manager

## Need

I use different types of means for conducting transactions. Credit cards, auto-drafts, debit cards, and checks are some of the most common means I use. Recording all these transactions and checking if my budget is balanced would require me to go through all the credit card statements manually. Some tools like Rocket or formerly Mint do unify transactions from many sources and present a uniform view, they require me to sign in and provide my password and financial information to a third party.

This tool brings together financial transactions from various credit cards and bank accounts and unifies them. The input is given as a sequence of .csv files that contain all the finanical transaction information. The output is the amount of spending categorized monthly. One major challenge is that different credit card companies format the date, amount, financial transaction details, etc., in different formats. This paper unifies all of it and creates a single Entry class that takes into account different formats. This allows us to adapt the tool for a wide variety of purposes.

## Organization

The .csv files are expcted to be put in transactions/ folder. The type specifying the company of origin of these transactions should be either specified in the code directly or given in types.csv file. The custom range for checking the monthly expenses can be given directly in the code.