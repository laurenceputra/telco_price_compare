var phoneArr = {}

//do the following 3 times after loading all the phones, once for each price tier
var phones = document.getElementsByClassName("phoneItem");
for (let i = 0; i < phones.length; i++) {
    var name = phones[i].getElementsByClassName("phoneModel")[0].innerHTML.trim().replace(" <br>", "");
    var price = phones[i].getElementsByClassName("phoneCost")[0].innerHTML.trim();
    if (!phoneArr[name]) {
        phoneArr[name] = []
    }
    phoneArr[name].push(price)
}

//at the end, export the phoneArr object into json, and paste into a price_list.json file. and use the price_exporter.py to generate the excel