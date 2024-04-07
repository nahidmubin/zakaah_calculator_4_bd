# Zakaah Calculator for Bangladeshi People
This program was built as a final project of "CS50's Introduction to Python" course. Note that this program may be used for rough calculations of one's Zakaah. But for decisive amount of Zakaah one should consult with an expert.
#### Video Demo:  https://youtu.be/X-SSyZJ9sxQ
#### Description:
Zakaah is one of the pillars in Islam. Zakaah is obligatory upon every wealthy Muslim subject to certain conditions.

Conditions for paying Zakaah are- 

1.	Wealth must reach the nisab (minimum threshold).
2.	One lunar year has passed since the wealth reached the Nisab (minimum threshold).

If the money is less than the Nisab, then no Zakaah is due on it. If it reaches the Nisab, and one lunar year has passed since the time when it reached the Nisab, then Zakaah becomes due at that point. The Nisab is the equivalent of 20 Mithkal of gold (Apprx. 85 grams) or 140 Mithkal of silver (Apprx. 595 grams). The rate that must be paid for Zakah is one quarter of one tenth (2.5%).

“Zakaah Calculator” program helps people from Bangladesh to calculate his or her zakaah easily. The program works in several steps.

First, it retrieves the current gold and silver price from the Bangladesh Jeweller’s Association (BAJUS)’s website. The website don’t provide the price of 24k gold and 24k silver (Pure Gold and Silver). The program extrapolates the price for 24k gold and 24k silver from 22k gold and 22k silver price. The price provided in the website is the buying price. To calculate zakaah selling price is required. The program calculates the selling price which is 20% less than the buying price.

Then the program calculates the threshold price that one need to surpass to be eligible to pay Zakaah. Threshold price is calculated by multiplying the 24k gold and 24k silver price with respective threshold weight mentioned above and then taking the minimum price of the two.

Then the program calculates ones asset and debt. First, it take input of 5 type of gold and 5 type of silver that one owns in gram namely, 24k, 22k, 21k, 18k and Traditional, either in bars or ornaments or any other form. Then it takes input combined amount of bank deposits (current, savings, fixed etc), cash in hand, stocks that were purchased to be sold in stock market or any other liquid asset etc. Then it takes input the present selling value of assets that were purchased at the intention of selling again in Taka. Then it takes input of all debts in Taka that are payable within next one lunar year.

Then it calculates the monetary value of all the gold and silver asset in taka by multiplying with the selling price that were extracted earlier. It also add the money assets, subtracts the debts and results the net asset in terms of taka.

Finally, the program compares the net asset with the threshold price. If the net asset is lower than the price then the program says that the user isn’t eligible to pay zakaah. If the net asset is greater than or equal to the threshold price then the program says that if exactly one year ago user had wealth that surpassed the threshold price of that time then he have to pay zakaah this year and then the program calculates and shows the zakaah which is 2.5% of the net asset.

The program also shows current buying and selling price of Gold and Silver.