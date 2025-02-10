var cp = prompt("Enter Cost Price:");
if (cp < 0) {
    console.log("Cost Price cannot be negative.");
} else {
    var sp = prompt("Enter Selling Price:");
    if (sp - cp > 0) {
        console.log("Your Profit is:", sp - cp);
    } else if (sp == cp) {
        console.log("You don't have any profit or loss (0)");
    } else {
        console.log("Your Loss is:", cp - sp);
    }
}
