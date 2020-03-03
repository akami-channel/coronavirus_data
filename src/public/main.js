




window.addEventListener('load', function() {
    console.log('All assets are loaded')
    // replace single quotes with double quotes for valid JSON
    dataString = dataString.replace(/'/g, '"');
    // remove extra ", " at the end
    dataString = dataString.slice(0,dataString.length - 3)
    dataString = dataString + "}"
    console.log(IsJsonString(dataString))
})




function IsJsonString(str) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}



