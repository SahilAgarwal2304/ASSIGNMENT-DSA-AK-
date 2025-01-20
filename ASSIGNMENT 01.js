var cp=prompt("Enter Cost Price:");
var sp=prompt("Enter Selling Price:");
if(sp-cp>0)
    console.log("Your Profit is:",sp-cp);
else if(sp==cp)
    console.log("You dont have any pofit or loss(0)");
else
    console.log("Your Loss is:",cp-sp);
